import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
import sklearn.linear_model as lm

def rmse(x, y):
    """
    Computes Root mean squared error 
    
    Parameters:
    x: series of values
    y: series of values
    
    Returns: Root mean squared error of x and y
    """
    error = np.sqrt(mean_squared_error(x,y))
    return error
    
def compute_CV_error(model, X_train, Y_train):
    """
    Computes CV error from 10-fold CV on training set 
    
    Parameters:
    model: model used to predict Y 
    X_train: dataframe of training features 
    Y_train: dataframe of response variable 
    
    Returns: RMSE across all folds 
    """
    kf = KFold(n_splits=10)
    validation_errors = []
    for train_idx, valid_idx in kf.split(X_train):
        split_X_train, split_X_valid = X_train.iloc[train_idx], X_train.iloc[valid_idx]
        split_Y_train, split_Y_valid = Y_train.iloc[train_idx], Y_train.iloc[valid_idx]
        model.fit(split_X_train, split_Y_train)
        error = np.sqrt(mean_squared_error(split_Y_valid, model.predict(split_X_valid)))
        validation_errors.append(error)  
    return np.mean(validation_errors)

