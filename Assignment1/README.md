The Problem statement is:
Assignment 1: Prototype.   
Build a prototype for email spam classification.   
     -In prepare.ipynb write the functions to.   
          +load the data from a given file path.  
          +preprocess the data (if needed).  
          +split the data into train/validation/test.   
          +store the splits at train.csv/validation.csv/test.csv.  
     -In train.ipynb write the functions to.  
          +fit a model on train data.  
          +score a model on given data.  
          +evaluate the model predictions.  
          +validate the model.  
                *fit on train.  
                *score on train and validation.  
                *evaluate on train and validation.  
                *fine-tune using train and validation (if necessary).  
                *score 3 benchmark models on test data and select the best one.  

===> 5 Benchmark models have been used in my assignment for comparison
    - Support Vector Classifier
    - AdaBoost Classifier
    - Logistic Regression Classifier
    - Decision Tree Classifier
    - Naive Bayes Classifier.    
The results of the assignment show that the accuracy of the test data is decreasing in the above order.
