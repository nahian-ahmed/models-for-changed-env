


ds_plots_metadata = {
    'k=30_train=0.4_separated=0.2_test=0.4_test2train=0.5_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.4,
        "Separated Ratio" : 0.2,
        "Test Ratio" : 0.4,        
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.0,
    },
    'k=30_train=0.4_separated=0.2_test=0.4_test2train=0.75_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.4,
        "Separated Ratio" : 0.2,
        "Test Ratio" : 0.4,        
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.0,
    },
    'k=30_train=0.4_separated=0.2_test=0.4_test2train=1.25_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.4,
        "Separated Ratio" : 0.2,
        "Test Ratio" : 0.4,        
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.0,
    },
    'k=30_train=0.4_separated=0.2_test=0.4_test2train=1.0_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.4,
        "Separated Ratio" : 0.2,
        "Test Ratio" : 0.4,        
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.0,
    },

    'k=30_train=0.4_separated=0.4_test=0.2_test2train=0.5_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.4,
        "Separated Ratio" : 0.4,
        "Test Ratio" : 0.2,        
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.0,
    },
    'k=30_train=0.4_separated=0.4_test=0.2_test2train=0.75_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.4,
        "Separated Ratio" : 0.4,
        "Test Ratio" : 0.2,        
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.0,
    },
    'k=30_train=0.4_separated=0.4_test=0.2_test2train=1.25_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.4,
        "Separated Ratio" : 0.4,
        "Test Ratio" : 0.2,        
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.0,
    },
    'k=30_train=0.4_separated=0.4_test=0.2_test2train=1.0_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.4,
        "Separated Ratio" : 0.4,
        "Test Ratio" : 0.2,        
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.0,
    },

}

dsdist_plots_metadata = {
    'k=30_train=0.4_separated=0.4_test=0.2_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.4,
        "Separated Ratio" : 0.4,
        "Test Ratio" : 0.2,        
        "FN cost" : 1.0,
    },

    'k=30_train=0.2_separated=0.4_test=0.4_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.2,
        "Separated Ratio" : 0.4,
        "Test Ratio" : 0.4,        
        "FN cost" : 1.0,
    },

    'k=30_train=0.4_separated=0.2_test=0.4_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.4,
        "Separated Ratio" : 0.2,
        "Test Ratio" : 0.4,        
        "FN cost" : 1.0,
    },

    'k=30_train=0.2_separated=0.2_test=0.6_fnc=1.0': {
        "K" : 30,
        "Train Ratio" : 0.2,
        "Separated Ratio" : 0.2,
        "Test Ratio" : 0.6,        
        "FN cost" : 1.0,
    },

}


selected_varying_plots = {
    'cost_fncost_k=30_train=0.4_test=0.4_test2train=1.0.png',
    'cost_k_train=0.4_test=0.2_test2train=0.5_fnc=1.0.png',
    'cost_separated_k=30_test=0.2_test2train=0.5_fnc=1.0.png',
    'cost_test2train_k=30_train=0.4_test=0.4_fnc=1.0.png',
    'cost_test_k=30_test=0.2_test2train=0.5_fnc=1.0.png',
    'dist_fncost_k=30_train=0.4_test=0.4_test2train=1.0.png',
    'dist_k_train=0.4_test=0.2_test2train=0.5_fnc=1.0.png',
    'dist_separated_k=30_test=0.2_test2train=0.5_fnc=1.0.png',
    'dist_test2train_k=30_train=0.4_test=0.4_fnc=1.0.png',
    'dist_test_k=30_test=0.2_test2train=0.5_fnc=1.0.png',
}



varying_plots_metadata = {

    # Varies "Separated Ratio"/"Train Ratio" while keeping "Test Ratio" constant
    "Separated Ratio 1" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.0,
        "identifier" : "separated_k=10_test=0.2_test2train=0.25_fnc=1.0",
    },
    "Separated Ratio 2" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.0,
        "identifier" : "separated_k=10_test=0.2_test2train=0.5_fnc=1.0",
    },
    "Separated Ratio 3" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.0,
        "identifier" : "separated_k=10_test=0.2_test2train=0.75_fnc=1.0",
    },
    "Separated Ratio 4" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.0,
        "identifier" : "separated_k=10_test=0.2_test2train=1.0_fnc=1.0",
    },
    "Separated Ratio 5" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.0,
        "identifier" : "separated_k=10_test=0.2_test2train=1.25_fnc=1.0",
    },
    "Separated Ratio 6" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.5,
        "identifier" : "separated_k=10_test=0.2_test2train=0.25_fnc=1.5",
    },
    "Separated Ratio 7" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.5,
        "identifier" : "separated_k=10_test=0.2_test2train=0.5_fnc=1.5",
    },
    "Separated Ratio 8" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.5,
        "identifier" : "separated_k=10_test=0.2_test2train=0.75_fnc=1.5",
    },
    "Separated Ratio 9" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.5,
        "identifier" : "separated_k=10_test=0.2_test2train=1.0_fnc=1.5",
    },
    "Separated Ratio 10" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.5,
        "identifier" : "separated_k=10_test=0.2_test2train=1.25_fnc=1.5",
    },
    "Separated Ratio 11" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 3.0,
        "identifier" : "separated_k=10_test=0.2_test2train=0.25_fnc=3.0",
    },
    "Separated Ratio 12" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 3.0,
        "identifier" : "separated_k=10_test=0.2_test2train=0.5_fnc=3.0",
    },
    "Separated Ratio 13" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 3.0,
        "identifier" : "separated_k=10_test=0.2_test2train=0.75_fnc=3.0",
    },
    "Separated Ratio 14" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 3.0,
        "identifier" : "separated_k=10_test=0.2_test2train=1.0_fnc=3.0",
    },
    "Separated Ratio 15" : { 
        "varying" : "Separated Ratio",
        "K" : 10,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 3.0,
        "identifier" : "separated_k=10_test=0.2_test2train=1.25_fnc=3.0",
    },
    "Separated Ratio 16" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.0,
        "identifier" : "separated_k=20_test=0.2_test2train=0.25_fnc=1.0",
    },
    "Separated Ratio 17" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.0,
        "identifier" : "separated_k=20_test=0.2_test2train=0.5_fnc=1.0",
    },
    "Separated Ratio 18" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.0,
        "identifier" : "separated_k=20_test=0.2_test2train=0.75_fnc=1.0",
    },
    "Separated Ratio 19" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.0,
        "identifier" : "separated_k=20_test=0.2_test2train=1.0_fnc=1.0",
    },
    "Separated Ratio 20" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.0,
        "identifier" : "separated_k=20_test=0.2_test2train=1.25_fnc=1.0",
    },
    "Separated Ratio 21" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.5,
        "identifier" : "separated_k=20_test=0.2_test2train=0.25_fnc=1.5",
    },
    "Separated Ratio 22" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.5,
        "identifier" : "separated_k=20_test=0.2_test2train=0.5_fnc=1.5",
    },
    "Separated Ratio 23" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.5,
        "identifier" : "separated_k=20_test=0.2_test2train=0.75_fnc=1.5",
    },
    "Separated Ratio 24" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.5,
        "identifier" : "separated_k=20_test=0.2_test2train=1.0_fnc=1.5",
    },
    "Separated Ratio 25" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.5,
        "identifier" : "separated_k=20_test=0.2_test2train=1.25_fnc=1.5",
    },
    "Separated Ratio 26" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 3.0,
        "identifier" : "separated_k=20_test=0.2_test2train=0.25_fnc=3.0",
    },
    "Separated Ratio 27" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 3.0,
        "identifier" : "separated_k=20_test=0.2_test2train=0.5_fnc=3.0",
    },
    "Separated Ratio 28" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 3.0,
        "identifier" : "separated_k=20_test=0.2_test2train=0.75_fnc=3.0",
    },
    "Separated Ratio 29" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 3.0,
        "identifier" : "separated_k=20_test=0.2_test2train=1.0_fnc=3.0",
    },
    "Separated Ratio 30" : { 
        "varying" : "Separated Ratio",
        "K" : 20,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 3.0,
        "identifier" : "separated_k=20_test=0.2_test2train=1.25_fnc=3.0",
    },
    "Separated Ratio 31" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.0,
        "identifier" : "separated_k=30_test=0.2_test2train=0.25_fnc=1.0",
    },
    "Separated Ratio 32" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.0,
        "identifier" : "separated_k=30_test=0.2_test2train=0.5_fnc=1.0",
    },
    "Separated Ratio 33" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.0,
        "identifier" : "separated_k=30_test=0.2_test2train=0.75_fnc=1.0",
    },
    "Separated Ratio 34" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.0,
        "identifier" : "separated_k=30_test=0.2_test2train=1.0_fnc=1.0",
    },
    "Separated Ratio 35" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.0,
        "identifier" : "separated_k=30_test=0.2_test2train=1.25_fnc=1.0",
    },
    "Separated Ratio 36" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.5,
        "identifier" : "separated_k=30_test=0.2_test2train=0.25_fnc=1.5",
    },
    "Separated Ratio 37" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.5,
        "identifier" : "separated_k=30_test=0.2_test2train=0.5_fnc=1.5",
    },
    "Separated Ratio 38" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.5,
        "identifier" : "separated_k=30_test=0.2_test2train=0.75_fnc=1.5",
    },
    "Separated Ratio 39" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.5,
        "identifier" : "separated_k=30_test=0.2_test2train=1.0_fnc=1.5",
    },
    "Separated Ratio 40" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.5,
        "identifier" : "separated_k=30_test=0.2_test2train=1.25_fnc=1.5",
    },
    "Separated Ratio 41" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 3.0,
        "identifier" : "separated_k=30_test=0.2_test2train=0.25_fnc=3.0",
    },
    "Separated Ratio 42" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 3.0,
        "identifier" : "separated_k=30_test=0.2_test2train=0.5_fnc=3.0",
    },
    "Separated Ratio 43" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 3.0,
        "identifier" : "separated_k=30_test=0.2_test2train=0.75_fnc=3.0",
    },
    "Separated Ratio 44" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 3.0,
        "identifier" : "separated_k=30_test=0.2_test2train=1.0_fnc=3.0",
    },
    "Separated Ratio 45" : { 
        "varying" : "Separated Ratio",
        "K" : 30,
        "Test Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 3.0,
        "identifier" : "separated_k=30_test=0.2_test2train=1.25_fnc=3.0",
    },



    # Vary "Test Ratio"
    "Test Ratio 1" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.0,
        "identifier" : "test_k=10_test=0.2_test2train=0.25_fnc=1.0",
    },
    "Test Ratio 2" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.0,
        "identifier" : "test_k=10_test=0.2_test2train=0.5_fnc=1.0",
    },
    "Test Ratio 3" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.0,
        "identifier" : "test_k=10_test=0.2_test2train=0.75_fnc=1.0",
    },
    "Test Ratio 4" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.0,
        "identifier" : "test_k=10_test=0.2_test2train=1.0_fnc=1.0",
    },
    "Test Ratio 5" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.0,
        "identifier" : "test_k=10_test=0.2_test2train=1.25_fnc=1.0",
    },
    "Test Ratio 6" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.5,
        "identifier" : "test_k=10_test=0.2_test2train=0.25_fnc=1.5",
    },
    "Test Ratio 7" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.5,
        "identifier" : "test_k=10_test=0.2_test2train=0.5_fnc=1.5",
    },
    "Test Ratio 8" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.5,
        "identifier" : "test_k=10_test=0.2_test2train=0.75_fnc=1.5",
    },
    "Test Ratio 9" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.5,
        "identifier" : "test_k=10_test=0.2_test2train=1.0_fnc=1.5",
    },
    "Test Ratio 10" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.5,
        "identifier" : "test_k=10_test=0.2_test2train=1.25_fnc=1.5",
    },
    "Test Ratio 11" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 3.0,
        "identifier" : "test_k=10_test=0.2_test2train=0.25_fnc=3.0",
    },
    "Test Ratio 12" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 3.0,
        "identifier" : "test_k=10_test=0.2_test2train=0.5_fnc=3.0",
    },
    "Test Ratio 13" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 3.0,
        "identifier" : "test_k=10_test=0.2_test2train=0.75_fnc=3.0",
    },
    "Test Ratio 14" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 3.0,
        "identifier" : "test_k=10_test=0.2_test2train=1.0_fnc=3.0",
    },
    "Test Ratio 15" : { 
        "varying" : "Test Ratio",
        "K" : 10,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 3.0,
        "identifier" : "test_k=10_test=0.2_test2train=1.25_fnc=3.0",
    },
    "Test Ratio 16" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.0,
        "identifier" : "test_k=20_test=0.2_test2train=0.25_fnc=1.0",
    },
    "Test Ratio 17" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.0,
        "identifier" : "test_k=20_test=0.2_test2train=0.5_fnc=1.0",
    },
    "Test Ratio 18" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.0,
        "identifier" : "test_k=20_test=0.2_test2train=0.75_fnc=1.0",
    },
    "Test Ratio 19" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.0,
        "identifier" : "test_k=20_test=0.2_test2train=1.0_fnc=1.0",
    },
    "Test Ratio 20" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.0,
        "identifier" : "test_k=20_test=0.2_test2train=1.25_fnc=1.0",
    },
    "Test Ratio 21" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.5,
        "identifier" : "test_k=20_test=0.2_test2train=0.25_fnc=1.5",
    },
    "Test Ratio 22" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.5,
        "identifier" : "test_k=20_test=0.2_test2train=0.5_fnc=1.5",
    },
    "Test Ratio 23" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.5,
        "identifier" : "test_k=20_test=0.2_test2train=0.75_fnc=1.5",
    },
    "Test Ratio 24" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.5,
        "identifier" : "test_k=20_test=0.2_test2train=1.0_fnc=1.5",
    },
    "Test Ratio 25" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.5,
        "identifier" : "test_k=20_test=0.2_test2train=1.25_fnc=1.5",
    },
    "Test Ratio 26" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 3.0,
        "identifier" : "test_k=20_test=0.2_test2train=0.25_fnc=3.0",
    },
    "Test Ratio 27" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 3.0,
        "identifier" : "test_k=20_test=0.2_test2train=0.5_fnc=3.0",
    },
    "Test Ratio 28" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 3.0,
        "identifier" : "test_k=20_test=0.2_test2train=0.75_fnc=3.0",
    },
    "Test Ratio 29" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 3.0,
        "identifier" : "test_k=20_test=0.2_test2train=1.0_fnc=3.0",
    },
    "Test Ratio 30" : { 
        "varying" : "Test Ratio",
        "K" : 20,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 3.0,
        "identifier" : "test_k=20_test=0.2_test2train=1.25_fnc=3.0",
    },
    "Test Ratio 31" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.0,
        "identifier" : "test_k=30_test=0.2_test2train=0.25_fnc=1.0",
    },
    "Test Ratio 32" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.0,
        "identifier" : "test_k=30_test=0.2_test2train=0.5_fnc=1.0",
    },
    "Test Ratio 33" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.0,
        "identifier" : "test_k=30_test=0.2_test2train=0.75_fnc=1.0",
    },
    "Test Ratio 34" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.0,
        "identifier" : "test_k=30_test=0.2_test2train=1.0_fnc=1.0",
    },
    "Test Ratio 35" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.0,
        "identifier" : "test_k=30_test=0.2_test2train=1.25_fnc=1.0",
    },
    "Test Ratio 36" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 1.5,
        "identifier" : "test_k=30_test=0.2_test2train=0.25_fnc=1.5",
    },
    "Test Ratio 37" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.5,
        "identifier" : "test_k=30_test=0.2_test2train=0.5_fnc=1.5",
    },
    "Test Ratio 38" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 1.5,
        "identifier" : "test_k=30_test=0.2_test2train=0.75_fnc=1.5",
    },
    "Test Ratio 39" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 1.5,
        "identifier" : "test_k=30_test=0.2_test2train=1.0_fnc=1.5",
    },
    "Test Ratio 40" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.5,
        "identifier" : "test_k=30_test=0.2_test2train=1.25_fnc=1.5",
    },
    "Test Ratio 41" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.25,
        "FN cost" : 3.0,
        "identifier" : "test_k=30_test=0.2_test2train=0.25_fnc=3.0",
    },
    "Test Ratio 42" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 3.0,
        "identifier" : "test_k=30_test=0.2_test2train=0.5_fnc=3.0",
    },
    "Test Ratio 43" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 0.75,
        "FN cost" : 3.0,
        "identifier" : "test_k=30_test=0.2_test2train=0.75_fnc=3.0",
    },
    "Test Ratio 44" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.0,
        "FN cost" : 3.0,
        "identifier" : "test_k=30_test=0.2_test2train=1.0_fnc=3.0",
    },
    "Test Ratio 45" : { 
        "varying" : "Test Ratio",
        "K" : 30,
        "Separated Ratio" : 0.2,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 3.0,
        "identifier" : "test_k=30_test=0.2_test2train=1.25_fnc=3.0",
    },


    # Vary "K"
    "K 1" : {
        "varying" : "K",
        "Train Ratio" : 0.4,        
        "Test Ratio" : 0.2, # implies "Separated Ratio" : 0.4,
        "Test to Train Class Distr. Ratio" : 0.5,
        "FN cost" : 1.0,
        "identifier" : "k_train=0.4_test=0.2_test2train=0.5_fnc=1.0",
    },
    "K 2" : {
        "varying" : "K",
        "Train Ratio" : 0.4,        
        "Test Ratio" : 0.2, # implies "Separated Ratio" : 0.4,
        "Test to Train Class Distr. Ratio" : 1.25,
        "FN cost" : 1.0,
        "identifier" : "k_train=0.4_test=0.2_test2train=1.25_fnc=1.0",
    },



    # Vary "Test to Train Class Distr. Ratio" 
    "Test to Train Class Distr. Ratio 1" : {
        "varying" : "Test to Train Class Distr. Ratio",
        "K" : 10,
        "Train Ratio" : 0.4,
        "Test Ratio" : 0.2, # implies "Separated Ratio" : 0.4,
        "FN cost" : 1.0,
        "identifier" : "test2train_k=10_train=0.4_test=0.4_fnc=1.0",
    },
    "Test to Train Class Distr. Ratio 2" : {
        "varying" : "Test to Train Class Distr. Ratio",
        "K" : 20,
        "Train Ratio" : 0.4,
        "Test Ratio" : 0.2, # implies "Separated Ratio" : 0.4,
        "FN cost" : 1.0,
        "identifier" : "test2train_k=20_train=0.4_test=0.4_fnc=1.0",
    },
    "Test to Train Class Distr. Ratio 3" : {
        "varying" : "Test to Train Class Distr. Ratio",
        "K" : 30,
        "Train Ratio" : 0.4,
        "Test Ratio" : 0.2, # implies "Separated Ratio" : 0.4,
        "FN cost" : 1.0,
        "identifier" : "test2train_k=30_train=0.4_test=0.4_fnc=1.0",
    },



    # Vary "FN cost"
    "FN cost 1" : {
        "varying" : "FN cost",
        "K" : 30,
        "Train Ratio" : 0.4,
        "Test Ratio" : 0.2, # implies "Separated Ratio" : 0.4,
        "Test to Train Class Distr. Ratio" : 0.5,
        "identifier" : "fncost_k=30_train=0.4_test=0.4_test2train=0.5",
    },
    "FN cost 2" : {
        "varying" : "FN cost",
        "K" : 30,
        "Train Ratio" : 0.4,
        "Test Ratio" : 0.2, # implies "Separated Ratio" : 0.4,
        "Test to Train Class Distr. Ratio" : 1.0,
        "identifier" : "fncost_k=30_train=0.4_test=0.4_test2train=1.0",
    },
    "FN cost 3" : {
        "varying" : "FN cost",
        "K" : 30,
        "Train Ratio" : 0.4,
        "Test Ratio" : 0.2, # implies "Separated Ratio" : 0.4,
        "Test to Train Class Distr. Ratio" : 1.25,
        "identifier" : "fncost_k=30_train=0.4_test=0.4_test2train=1.25",
    },

}


