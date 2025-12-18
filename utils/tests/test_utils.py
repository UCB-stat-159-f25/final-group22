import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
import sklearn.linear_model as lm
from sklearn.metrics import mean_squared_error
from utils import compute_CV_error, rmse
import pytest

def test_rmse():
    x = pd.Series([1,2,3,4,5])
    y = pd.Series([2,4,6,8,10])
    err = rmse(x,y)
    answer = np.sqrt(11)
    assert np.isclose(err, answer) 

def test_cv_error():
    model = lm.LinearRegression()
    X_train = pd.DataFrame({'x1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],'x2': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    Y_train = pd.Series([1.1, 1.9, 3.0, 4.1, 4.9, 5.0, 6.1, 7.0, 8.1, 9.0])
    CVerr = compute_CV_error(model, X_train, Y_train)
    assert isinstance(CVerr, float)

