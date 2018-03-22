# ai...
from sklearn.externals import joblib
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
def train():
    data=pd.read_csv('train.csv')
    clf = DecisionTreeClassifier(max_depth=3)
    label = data['Decision'].values
    feature = data.ix[:,1:6]
    clf = clf.fit(feature,label)
    #joblib.dump(clf, 'decisionTree.pkl')
    #when u use it, clf = joblib.load('decisionTree.pkl'), y=clf.predict(x)


def predict(clf, data):
    data=np.arrays(data)
    return int(clf.predict(data.reshape(1,-1)))
