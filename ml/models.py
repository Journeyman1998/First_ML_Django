from django.db import models
import pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Create your models here.

def predict(s_list):

    linreg = pickle.load(open('ml/ml', 'rb'))
    arr = np.array(s_list).reshape(1,-1)
    X = PolynomialFeatures(2).fit_transform(arr)

    y_pred = linreg.predict(X)
    y_pred = round(y_pred[0], ndigits=3)
    return round(y_pred[0], 3)