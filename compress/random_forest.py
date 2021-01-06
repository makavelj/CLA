'''
Implementation of Random Forest Algorithm based on Decision DecisionTrees.
'''

import decisiontree as dt
import random as rdm
import numpy as np
import math
import util
from sklearn.datasets import load_wine

def boots_trap(X, y, sample_size=None):
    samples = len(X)
    if(sample_size is None): sample_size = samples
    set = []
    target = []
    for i in range(sample_size):
        pick = rdm.randrange(samples)
        set.append(X[pick])
        target.append(y[pick])
    return set, target

def bagged_trees(X, y, tree_number=10, tree_depth=2, sample_size=None):
    forest = []
    for tree in range(tree_number):
        sample_set, target_set = boots_trap(X, y, sample_size)
        dtree = dt.build_tree(np.array(sample_set), target_set, 0, max_depth=tree_depth, n_labels=3)
        forest.append(dtree)
    return forest

def forest_predict(X, forest):
    y_prediction = []
    for x in X:
        vote = [None]*len(forest)
        for tree in range(len(forest)):
            vote[tree] = dt.predict_tree(forest[tree], x)
        decision = np.argmax(np.bincount(vote))
        y_prediction.append(decision)
    return y_prediction

def random_forest(sample_set, target_set, sample_size=None):
    if(sample_size is None): sample_size = int(math.sqrt(len(sample_set))) + 1
    return sample_size
