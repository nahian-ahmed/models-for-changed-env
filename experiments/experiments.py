'''
Experiment: Evaluate practicality and applicability of the ROC Convex Hull Method.

'''

import tqdm
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, matthews_corrcoef, roc_auc_score
from scipy.stats import wasserstein_distance, energy_distance, cramervonmises_2samp
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.preprocessing import StandardScaler

# from datasets import ds_meta
from preprocess import split_data


import sys, os
sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rocchmethod')))

from rocchmethod import rocch_method, classifiers_on_rocch, impose_class_distr, unique_cls_distr, expected_cost

# from plot_descriptions import selected_causal_graphs

# Experiment over different values of K (No of repeats/splits)
K_range = [3, 5, 10, 20, 30] 

# split_ratios[i] = [train_ratio, separated_ratio, test_ratio]
split_ratio_range = [ 
    [0.2, 0.6, 0.2], # train=20%, separated=60%, test=20%
    [0.4, 0.4, 0.2], # train=40%, separated=40%, test=20%
    [0.6, 0.2, 0.2], # train=60%, separated=20%, test=20%
    [0.4, 0.2, 0.4], # train=40%, separated=20%, test=40%
    [0.2, 0.2, 0.6], # train=20%, separated=20%, test=60%
    [0.2, 0.4, 0.4], # train=20%, separated=40%, test=40%
]


# environment = ["%/100 of original clas distr.", "FP cost", "FN cost"]
# "%/100 of original clas distr." represents the scaled percentage of the original class distribution (of training set) in the imprecise environment/test set
# A value of 1.0 indicates that the test set has the same class distriution as the original/training set.
# A value of 0.5 indicates that the test set is equal to the original class distribution multiplied by 0.5 (divided by 2).
# A value of 1.25 indicates that the test set is equal to the original class distribution mulitplied by 1.25 (divided by 4/5)  

# Set of class and cost distributions (imprecise environments) we will be testing on,
environments = [

    [1.0, 1.0, 1.0], # control, same class distribution as training data, uniform cost distribution
    [1.0, 1.0, 1.5], # same class distribution as training data, FN cost is 1.5 times FP cost
    [1.0, 1.0, 3.0], # same class distribution as training data, FN cost is 3 times FP cost

    [0.5, 1.0, 1.0], # halved class distribution, uniform cost distribution
    [0.5, 1.0, 1.5], # halved class distribution,  FN cost is 1.5 times FP cost
    [0.5, 1.0, 3.0], # halved class distribution,  FN cost is 3 times FP cost

    [0.25, 1.0, 1.0], # quartered class distribution, uniform cost distribution 
    [0.25, 1.0, 1.5], # quartered class distribution,  FN cost is 1.5 times FP cost
    [0.25, 1.0, 3.0], # quartered class distribution,  FN cost is 3 times FP cost
    
    [0.75, 1.0, 1.0], # 3/4 times class distribution, uniform cost distribution 
    [0.75, 1.0, 1.5], # 3/4 times class distribution,  FN cost is 1.5 times FP cost
    [0.75, 1.0, 3.0], # 3/4 times class distribution,  FN cost is 3 times FP cost
    
    [1.25, 1.0, 1.0], # 5/4 times class distribution, uniform cost distribution
    [1.25, 1.0, 1.5], # 5/4 times class distribution,  FN cost is 1.5 times FP cost
    [1.25, 1.0, 3.0], # 5/4 times class distribution,  FN cost is 3 times FP cost
    
]

oversampling_undersampling_methods = [
    ['Random', 'Random'],
    ['SMOTE', 'NearMiss'],
]

random_state = 0




# ----------------------------------------------------------------------------------------
# For temporary experimentation only
# ----------------------------------------------------------------------------------------

K_range = [3]

split_ratio_range = [ 
    [0.4, 0.4, 0.2], # train=40%, separated=20%, test=40%
]
environments = [

    [0.5, 1.0, 1.0], # halved class distribution, uniform cost distribution
    [1.25, 1.0, 1.0], # halved class distribution, uniform cost distribution
   
]
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------



environments_cls_distr = unique_cls_distr(environments)


output_table_dir = './experiments/tables/'



"""
Written by Jindong Wang
Retrieved from https://github.com/jindongwang/transferlearning
transferlearning/code/distance/mmd_numpy_sklearn.py 
"""

def mmd_linear(X, Y):
    """MMD using linear kernel (i.e., k(x,y) = <x,y>)
    Note that this is not the original linear MMD, only the reformulated and faster version.
    The original version is:
        def mmd_linear(X, Y):
            XX = np.dot(X, X.T)
            YY = np.dot(Y, Y.T)
            XY = np.dot(X, Y.T)
            return XX.mean() + YY.mean() - 2 * XY.mean()
    Arguments:
        X {[n_sample1, dim]} -- [X matrix]
        Y {[n_sample2, dim]} -- [Y matrix]
    Returns:
        [scalar] -- [MMD value]
    """
    delta = X.mean(0) - Y.mean(0)
    return delta.dot(delta.T)


def average_wasserstein_distance(X_1, X_2):
    
    n_features = X_1.shape[1]

    avg_w_dist = 0
    for i in range(n_features):
        avg_w_dist += wasserstein_distance(X_1[:,i], X_2[:,i])
    
    avg_w_dist /= n_features

    return avg_w_dist 

def average_energy_distance(X_1, X_2):
    
    n_features = X_1.shape[1]

    avg_w_dist = 0
    for i in range(n_features):
        avg_w_dist += energy_distance(X_1[:,i], X_2[:,i])
    
    avg_w_dist /= n_features

    return avg_w_dist


def average_auc_phi (X_1, X_2, repeats=3, test_ratio=0.2, random_state=0):
    
    min_samples = min(X_1.shape[0], X_2.shape[0])
    X_1, X_2 = X_1[:min_samples, :], X_2[:min_samples, :]
    X_1 = np.hstack((X_1, np.zeros((min_samples,1), dtype=np.int8)))
    X_2 = np.hstack((X_2, np.ones((min_samples,1), dtype=np.int8)))
    data = np.vstack((X_1,X_2))
    X = data[:, :-1]
    y = data[:, -1]

    auc_avg = 0
    phi_avg = 0

    sss = StratifiedShuffleSplit(n_splits=repeats, test_size=test_ratio, random_state=random_state)
        
    for (train_index, test_index) in sss.split(X, y):
        # Split into training and testing data
        X_train, X_test, y_train, y_test = X[train_index].copy(), X[test_index].copy(), y[train_index].copy(), y[test_index].copy()
        
        # Scale features
        scaler = StandardScaler().fit(X_train)
        X_train = scaler.transform(X_train)
        X_test = scaler.transform(X_test)

        model = RandomForestClassifier(random_state=0)
        model.fit(X_train, y_train)
        y_score = model.predict_proba(X_test)[:,1]
        y_hat = model.predict(X_test)

        phi_avg += matthews_corrcoef(y_test, y_hat)
        auc_avg += roc_auc_score(y_test, y_score)
        
    auc_avg /= repeats
    phi_avg /= repeats

    return auc_avg, phi_avg

# def kldiv (X_1, X_2):
    
#     return 


def average_cramervonmises (X_1, X_2):
    n_features = X_1.shape[1]

    avg_cramervonmises_criterion = 0
    for i in range(n_features):
        res = cramervonmises_2samp(X_1[:,i], X_2[:,i])
        avg_cramervonmises_criterion += res.statistic
    
    avg_cramervonmises_criterion /= n_features

    return avg_cramervonmises_criterion 

def run_experiments(ds_meta):
    '''
    '''
    dataset_descriptions = pd.read_csv(f'{output_table_dir}dataset_descriptons.csv') # Saved during preprocessing
    original_cls_distr = dict(zip(dataset_descriptions['Data Set'], dataset_descriptions['Class Balance']))
    ds_keys = list(dataset_descriptions['Data Set'])
    
    performance_df = pd.DataFrame(columns=(
        'K',
        'Train Ratio',
        'Separated Ratio',
        'Test Ratio',
        'Data Set',
        'Test Size',
        'Train Class Distr.',
        'Test to Train Class Distr. Ratio',
        'Test Class Distr.',
        'FP cost',
        'FN cost',
        'Oversampling Method',
        'Undersampling Method',
        'Avg. Wasserstein Dist.',
        'Avg. Energy Dist.',
        'Avg. MMD',
        'Avg. AUC (COVSHIFT)',
        'Avg. Phi',
        'Avg. Cramer-von Mises Criterion',
        'No. Test Instances',
        'Split No.',
        'Optimal FPR (ROCCH Method)',
        'Optimal TPR (ROCCH Method)',
        'Isoperformance_df Line Slope',
        'Isoperformance_df Line Intercept',
        'Classifier',
        'Threshold',
        'FPR',
        'TPR',
        'Cost',
        'Accuracy',
        'F1-score',
        'Accuracy (Separated, T=0.5)',
        'F1-score (Separated, T=0.5)',
        )
    )
    c = 0

    print("\nExperiment: Evaluate practicality and applicability of the ROC Convex Hull Method.")


    for K in K_range:

        for split_ratio in split_ratio_range:

            train_ratio, separated_ratio, test_ratio = split_ratio[0], split_ratio[1], split_ratio[2] 

            print(f'\nK: {K}, Train Ratio: {train_ratio}, Separated Ratio: {separated_ratio}, Test Ratio: {test_ratio}')    
            
            preprocessed_ds = split_data(ds_meta, K, train_ratio, separated_ratio, test_ratio, random_state=random_state)
            
            for ds_key in (pbar := tqdm.tqdm(preprocessed_ds.keys())):
                
                pbar.set_description(f'Running experiment on "{ds_key}"')


                for split_num in range(K):

                    X_train, X_test, X_separated, y_train, y_test, y_separated = preprocessed_ds[ds_key][split_num]
                    
                     

                    # print('Split No.',split_num,
                    #     'train_ratio',train_ratio,'train_size',y_train.shape[0],
                    #     'separated_ratio',separated_ratio,'separated_size',y_separated.shape[0],
                    #     'test_ratio',test_ratio,'test_size',y_test.shape[0]
                    # )

                    # Train classifiers and predict on (existing) test set
                    models = { 
                        # Default parameters used for models from sklearn 1.2.0
                        # same random state across splits, but different training and test data across splits
                        'A' : RandomForestClassifier(random_state=0),
                        'B' : LogisticRegression(random_state=0),
                        'C' : KNeighborsClassifier(),
                    }

                    y_hats = []

                    for m in models:
                        
                        models[m].fit(X_train, y_train)
                        
                        y_hats.append(models[m].predict_proba(X_separated)[:,1])
                        
                        
                    fpr_list, tpr_list, threshold_list, rocch_fpr, rocch_tpr, optimals = rocch_method(
                                                                                                y_separated,
                                                                                                y_hats,
                                                                                                environments
                                                                                            )
                    rocch_classifiers, rocch_thresholds = classifiers_on_rocch(fpr_list,tpr_list, threshold_list, rocch_fpr, rocch_tpr)
                    



                    for os_us in oversampling_undersampling_methods:

                        test_cls_distr = {cls_distr : impose_class_distr(X_test, y_test, (original_cls_distr[ds_key] * cls_distr), os_us[0], os_us[1], random_state) for cls_distr in environments_cls_distr}


                        for i, environment in enumerate(environments):

                            X_test_env, y_test_env = test_cls_distr[environment[0]]

                            avg_w_dist = average_wasserstein_distance(X_train, X_test_env)
                            avg_e_dist = average_energy_distance(X_train, X_test_env)
                            

                            avg_mmd = mmd_linear(X_train, X_test_env)/X_train.shape[1]
                            avg_auc, avg_phi = average_auc_phi(X_train, X_test_env)
                            
                            
                            avg_cvmc = average_cramervonmises(X_train, X_test_env)

                            
                            for j, rocch_fpr_t in enumerate(rocch_fpr):
                                
                                for k, clfs in enumerate(rocch_classifiers[j]):
                                    predictions = models[list(models.keys())[k]].predict_proba(X_test_env)[:,1]
                                    predictions_hard = np.where(1, predictions>=rocch_thresholds[j][k], 0)

                                    predictions_sep = models[list(models.keys())[k]].predict_proba(X_separated)[:,1]
                                    predictions_sep_hard = np.where(1, predictions_sep>=0.5, 0)

                                    cost = expected_cost(y_test_env, predictions_hard, environment[1], environment[2])
                                    acc = accuracy_score(y_test_env, predictions_hard)
                                    f1_s = f1_score(y_test_env, predictions_hard)

                                    acc_sep = accuracy_score(y_separated, predictions_sep_hard)
                                    f1_s_sep = f1_score(y_separated, predictions_sep_hard)

                                    performance_df.loc[c] = [
                                        K,
                                        train_ratio,
                                        separated_ratio,
                                        test_ratio,
                                        ds_key,
                                        predictions_hard.shape[0],
                                        original_cls_distr[ds_key],
                                        environment[0],
                                        original_cls_distr[ds_key] * environment[0],
                                        environment[1], 
                                        environment[2],
                                        os_us[0],
                                        os_us[1],
                                        avg_w_dist,
                                        avg_e_dist,
                                        avg_mmd,
                                        avg_auc,
                                        avg_phi,
                                        avg_cvmc,
                                        y_test_env.shape[0],
                                        split_num,
                                        optimals[i][0],
                                        optimals[i][1],
                                        optimals[i][2],
                                        optimals[i][3],
                                        list(models.keys())[clfs],
                                        rocch_thresholds[j][k],
                                        rocch_fpr_t,
                                        rocch_tpr[j],
                                        cost,
                                        acc,
                                        f1_s,
                                        acc_sep,
                                        f1_s_sep,
                                        ]
                                    c += 1
        
        
    performance_df = performance_df.round(4)
    performance_df.to_csv(f'{output_table_dir}performance.csv')

    # performance_df = pd.read_csv(f'{output_table_dir}performance.csv')

    
    performance_summarized_df = pd.DataFrame(columns=(
        'K',
        'Train Ratio',
        'Separated Ratio',
        'Test Ratio',
        'Data Set',
        'Train Class Distr.',
        'Test to Train Class Distr. Ratio',
        'Test Class Distr.',
        'FP cost',
        'FN cost',
        'Oversampling Method',
        'Undersampling Method',
        'Avg. Wasserstein Dist.',
        'Avg. Energy Dist.',
        'Avg. MMD',
        'Avg. AUC (COVSHIFT)',
        'Avg. Phi',
        'Avg. Cramer-von Mises Criterion',
        'Split No.',
        'Optimal FPR (ROCCH Method)',
        'Optimal TPR (ROCCH Method)',
        'Avg. Optimal Point Cost (ROCCH Method)',
        'Optimal FPR (Accuracy-Max)',
        'Optimal TPR (Accuracy-Max)',
        'Avg. Optimal Point Cost (Accuracy-Max)',
        'Optimal FPR (F1-score-Max)',
        'Optimal TPR (F1-score-Max)',
        'Avg. Optimal Point Cost (F1-score-Max)',
        'Optimal FPR (Actual)',
        'Optimal TPR (Actual)',
        'Avg. Optimal Point Cost (Actual)',
        'Distance between ROCCHM and Actual',
        'Distance between Accuracy-Max and Actual',
        'Distance between F1-score-Max and Actual',
        )
    )

    c = 0

    print("\nSummarizing and saving results.")
    for K in K_range:
        for split_ratio in split_ratio_range:

            train_ratio, separated_ratio, test_ratio = split_ratio[0], split_ratio[1], split_ratio[2] 
            
            for ds_key in ds_keys:
                for split_num in range(K):

                    for os_us in oversampling_undersampling_methods:
                        for i, environment in enumerate(environments):   
                            current_slice_idx = (
                                            (performance_df['K'] == K) & 
                                            (performance_df['Train Ratio'] == train_ratio) &
                                            (performance_df['Separated Ratio'] == separated_ratio) &
                                            (performance_df['Test Ratio'] == test_ratio) &
                                            (performance_df['Data Set'] == ds_key) &
                                            (performance_df['Split No.'] == split_num) &
                                            (performance_df['Test to Train Class Distr. Ratio'] == environment[0]) &
                                            (performance_df['FP cost'] == environment[1]) &
                                            (performance_df['FN cost'] == environment[2])
                                        ) 

                            current_df = performance_df.loc[current_slice_idx]


                            # Cost of Optimal Point selected by ROCCH Method
                            current_optimal_df = current_df[
                                            (current_df['Optimal FPR (ROCCH Method)'] == current_df['FPR']) & 
                                            (current_df['Optimal TPR (ROCCH Method)'] == current_df['TPR'])
                                        ]
                            rocchm_optimal_point_cost = current_optimal_df['Cost'].min()
                                                
                            # Accuracy maximizing FPR and TPR
                            accumax_idx = current_df['Accuracy (Separated, T=0.5)'].idxmax()
                            accumax_optimal = [current_df['FPR'].loc[accumax_idx], current_df['TPR'].loc[accumax_idx]]

                            # Cost of accuracy maximizing FPR and TPR
                            accumax_optimal_point_cost = current_df['Cost'].loc[accumax_idx]

                            # F1-score maximizing FPR and TPR
                            fonemax_idx = current_df['F1-score (Separated, T=0.5)'].idxmax()
                            fonemax_optimal = [current_df['FPR'].loc[fonemax_idx], current_df['TPR'].loc[fonemax_idx]]

                            # Cost of F1-score maximizing FPR and TPR
                            fonemax_optimal_point_cost = current_df['Cost'].loc[fonemax_idx]

                            # Actual FPR and TPR
                            actual_min_cost_idx = current_df['Cost'].idxmin()
                            actual_optimal = [current_df['FPR'].loc[actual_min_cost_idx], current_df['TPR'].loc[actual_min_cost_idx]]
                            
                            # Cost of Actual Optimal Point
                            actual_optimal_point_cost = current_df['Cost'].loc[actual_min_cost_idx]

                            # Distance (in ROC space) between Optimal Point selected by ROCCH Method and Actual Optimal Point
                            rocchm_optimal = [current_df['Optimal FPR (ROCCH Method)'].iloc[0], current_df['Optimal TPR (ROCCH Method)'].iloc[0]] 
                            distance_rocchm_actual = np.linalg.norm (np.array(rocchm_optimal)-np.array(actual_optimal))

                            # Distance (in ROC space) between Optimal Point based Accuracy-Max and Actual Optimal Point
                            distance_accumax_actual = np.linalg.norm (np.array(accumax_optimal)-np.array(actual_optimal))

                            # Distance (in ROC space) between Optimal Point based Accuracy-Max and Actual Optimal Point
                            distance_fonemax_actual = np.linalg.norm (np.array(fonemax_optimal)-np.array(actual_optimal))

                            # Test set size, for calculating avg. exp. cost
                            test_size = current_df['Test Size'].iloc[0]
                            

                            performance_summarized_df.loc[c] = [
                                        K,
                                        current_df['Train Ratio'].iloc[0],
                                        current_df['Separated Ratio'].iloc[0],
                                        current_df['Test Ratio'].iloc[0],
                                        ds_key,
                                        original_cls_distr[ds_key],
                                        environment[0],
                                        original_cls_distr[ds_key] * environment[0],
                                        environment[1], 
                                        environment[2],
                                        os_us[0],
                                        os_us[1],
                                        current_df['Avg. Wasserstein Dist.'].iloc[0],
                                        current_df['Avg. Energy Dist.'].iloc[0],
                                        current_df['Avg. MMD'].iloc[0],
                                        current_df['Avg. AUC (COVSHIFT)'].iloc[0],
                                        current_df['Avg. Phi'].iloc[0],
                                        current_df['Avg. Cramer-von Mises Criterion'].iloc[0],
                                        split_num,
                                        current_df['Optimal FPR (ROCCH Method)'].iloc[0],
                                        current_df['Optimal TPR (ROCCH Method)'].iloc[0],
                                        rocchm_optimal_point_cost/test_size,
                                        accumax_optimal[0],
                                        accumax_optimal[1],
                                        accumax_optimal_point_cost/test_size,
                                        fonemax_optimal[0],
                                        fonemax_optimal[1],
                                        fonemax_optimal_point_cost/test_size,
                                        actual_optimal[0],
                                        actual_optimal[1],
                                        actual_optimal_point_cost/test_size,
                                        distance_rocchm_actual,
                                        distance_accumax_actual,
                                        distance_fonemax_actual,

                                        
                                    ]
                            c += 1


    performance_summarized_df = performance_summarized_df.round(4)
    performance_summarized_df.to_csv(f'{output_table_dir}performance_summarized.csv')


    print("Experiment completed.")



