'''
Implementation of Boosting via Decision Tree Stumps
'''

import decisiontree as dt
import math
import util
import numpy as np


MAX = 999999999999999999999999999

#Weak classifier with decision strenght based on weight
class weak_learner():
    """Weak learner classifier to for boosted algorithm.

    Args:
        n_feat : int or string
            feature on which classifier takes decision
        threshold : double
            the value on which classifier takes decision
        left : array
            classes with feature value lower than threshold
        right : array
            classes with feature value greater than threshold
        weight : double
            weight decicdes strength of classifier

    Attributes:
        n_feat : int or string
            feature on which classifier takes decision
        threshold : double
            the value on which classifier takes decision
        left : array
            classes with feature value lower than threshold
        right : array
            classes with feature value greater than threshold
        weight : double
            weight decicdes strength of classifier
    """
    def __init__(self,n_feat, threshold, left, right, weight):
        self.n_feat = n_feat
        self.threshold = threshold
        self.left_class = np.argmax(np.bincount(left))
        self.right_class = np.argmax(np.bincount(right))
        self.weight = weight
    def weak_prediction(self, X):
        feat = self.n_feat
        if(X[feat] < self.threshold):
            return self.left_class
        else:
            return self.right_class

#Iteration of n_learner classifiers creating n weak learners
def weak_learners(X, y, n_learner):
    labels = len(np.unique(y))
    learners = []
    n = len(X)
    weights = [1/n]*n
    for t in range(n_learner):
        best_feat= -1
        best_split = 0.0
        smallest_error = MAX
        for n_feat in range(X.shape[1]):
            x_candidates = dt.define_candidates(X.T[n_feat])
            n = X.shape[0]
            #Find best candidate value
            for i in range(len(x_candidates)):
                # split column into left and right
                row =  X.T[n_feat]
                left, right = dt.left_right_split(value = x_candidates[i], row=row, y=y)
                if(len(left) == 0): left_decision = np.argmin(np.bincount(right))
                else: left_decision = np.argmax(np.bincount(left))
                if(len(right) == 0): right_decision = np.argmin(np.bincount(left))
                else: right_decision = np.argmax(np.bincount(right))
                weighted_error, miss = compute_weighted_error(left, right, left_decision, right_decision, y, weights)
                if(weighted_error < smallest_error):
                    smallest_error = weighted_error
                    misses = miss
                    best_feat = n_feat
                    best_split = x_candidates[i]
                    best_left = left
                    best_right = right
        frac = (1-weighted_error)/weighted_error
        classifier_weight = 0.5*math.log(frac) + math.log(labels-1)
        for i in range(n):
            if(misses[i] == True): weights[i] = weights[i]*math.exp(classifier_weight)
        normalize = sum(weights)
        weights = [weight / normalize for weight in weights]
        learners.append(weak_learner(best_feat, best_split, best_left, best_right, classifier_weight))
    return learners

#Compute Error based on weights
def compute_weighted_error(left, right, left_decision, right_decision, y, weights):
    weighted_error = 0
    miss = [False]*len(weights)
    for i in range(len(left)+len(right)):
        if(i < len(left)):
            if(left_decision == y[i]): miss[i] = False
            else:
                weighted_error += weights[i]
                miss[i] = True
        else:
            if(right_decision == y[i]): miss[i] = False
            else:
                weighted_error += weights[i]
                miss[i] = True
    return weighted_error, miss

#Train boosted clasifieres on Data
def train_boosting(X, y, n_learner=25):
    experts = weak_learners(X, y, n_learner)
    return experts

#Predict with voting based on boosted learners
def predict_boosting(X, learner):
    y_prediction = []
    for x in X:
        dict = {}
        for i in range(len(learner)):
            weak_predictor = learner[i].weak_prediction(x)
            if(not(weak_predictor in dict)): dict[weak_predictor] = learner[i].weight
            else: dict[weak_predictor] += learner[i].weight
        max_value = max(dict.values())
        ensemble_prediction = [k for k, v in dict.items() if v == max_value]
        y_prediction.append(ensemble_prediction[0])
    return y_prediction
