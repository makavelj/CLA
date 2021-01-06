'''
Implementation of Random Forest Algorithm based on Decision DecisionTrees.
'''

import decisiontree as dt
import random as rdm
import numpy as np
import math
import cla_util as util


#Sample from the given set data points
def boots_trap(X, y, sample_size=None):
    samples = len(X)
    if(sample_size is None): sample_size = int(samples/2) + 1
    set = []
    target = []
    for i in range(sample_size):
        pick = rdm.randrange(samples)
        set.append(X[pick])
        target.append(y[pick])
    return set, target

#Create a forest of boots trap samples
def bagged_trees(X, y, tree_number=10, tree_depth=2, sample_size=None, split=util.entropy, random_forest_mode=False, boots_trapping = True):
    forest = []
    for tree in range(tree_number):
        if(boots_trapping): sample_set, target_set = boots_trap(X, y, sample_size)
        else: sample_set, target_set = X, y
        dtree = dt.build_tree(np.array(sample_set), target_set,
                                0, max_depth=tree_depth, split=split,
                                random_forest=random_forest_mode)
        forest.append(dtree)
    return forest

#Use forest of decision trees to predict data via majority vote
def forest_predict(X, forest):
    y_prediction = []
    for x in X:
        vote = [None]*len(forest)
        for tree in range(len(forest)):
            vote[tree] = dt.predict_tree(forest[tree], x)
        decision = np.argmax(np.bincount(vote))
        y_prediction.append(decision)
    return y_prediction

#Create random forest using limited size of features for each split
def random_forest(X, y, tree_number=10, tree_depth=2, sample_size=None, split=util.entropy, random_forest_mode=True, boots_trapping=True):
    forest = bagged_trees(X, y, tree_number=tree_number,
                        tree_depth=tree_depth, sample_size=None,
                        split=util.entropy, random_forest_mode=False,
                        boots_trapping=boots_trapping)
    return forest
