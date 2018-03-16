# ai...
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
def train():
    data=pd.read_csv('train.csv')
    clf = DecisionTreeClassifier(max_depth=3)
    label = data['Decision'].values
    feature = data.ix[:,1:6]
    clf = clf.fit(feature,label)
    return clf


def predict(clf, data):
    return clf.predict(data)
