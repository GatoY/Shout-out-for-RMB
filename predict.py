from sklearn.externals import joblib
import numpy as np

def predict(info):
    clf = joblib.load('decisionTree.pkl')
    result = clf.predict(np.array(info).reshape(1,-1))
    return result
