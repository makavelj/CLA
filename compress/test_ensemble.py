'''
Test for ensemble methods.
'''

import decisiontree as dt
import boosting as boost
import util
import random_forest as rf
from sklearn.datasets import load_wine
from sklearn import tree


#Assert that the decision tree classifier achieves comparable results sk learn tree
def test_decisiontree_accuracy():
    X, t = load_wine(return_X_y=True)
    X_train, X_test, t_train, t_test = util.split_data(X, t)
    dtree = dt.build_tree(X_train, t_train, 0, max_depth=3, n_labels=3)
    count = 0
    for i in range(len(X_test)):
        if(t_test[i] == dt.predict_tree(dtree, X_test[i])):
            count += 1
    dt_score =  count/len(t_test)
    clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
    clf = clf.fit(X_train, t_train)
    predsk = clf.predict(X_test)
    skcounter = 0
    for i in range(len(predsk)):
        if(predsk[i] == t_test[i]):
            skcounter += 1
    sk_score = skcounter/len(t_test)
    assert(sk_score-0.1 <= dt_score), ('Prediction of decision tree score ', dt_score, ' has to be at least int the target score ', sk_score-0.1)

#Assert that boosted classifier achieves fine results
def test_boosting_accuracy():
    X, t = load_wine(return_X_y=True)
    X_train, X_test, t_train, t_test = util.split_data(X, t, seed=0)
    classifier = boost.train_boosting(X_train, t_train, n_learner=25)
    y_predictions = boost.predict_boosting(X_test, classifier)
    count = 0
    for i in range(len(t_test)):
        if(y_predictions[i] == t_test[i]): count +=1
    boost_score = count/len(t_test)
    assert(boost_score > 0.9), ('Prediction of boosted classifier not good enough with ', boost_score, ' accuracy.')

#Assert that bagged trees classifier achieves fine results
def test_bagged_trees_accuracy():
    X, t = load_wine(return_X_y=True)
    X_train, X_test, t_train, t_test = util.split_data(X, t, seed=0)
    forest = rf.bagged_trees(X_train,t_train)
    predictions = rf.forest_predict(X_test, forest)
    count = 0
    for i in range(len(t_test)):
        if(predictions[i] == t_test[i]):
            count += 1
    bagged_score = count/len(t_test)
    assert(bagged_score > 0.8), ('Prediction of bagged trees not good enough with ', bagged_score, ' accuracy.')

#Assert that random_forest classifier achieves fine results
def test_random_forest_accuracy():
    X, t = load_wine(return_X_y=True)
    X_train, X_test, t_train, t_test = util.split_data(X, t, seed=0)
    forest = rf.random_forest(X_train,t_train)
    predictions = rf.forest_predict(X_test, forest)
    count = 0
    for i in range(len(t_test)):
        if(predictions[i] == t_test[i]):
            count += 1
    rf_score = count/len(t_test)
    assert(rf_score > 0.8), ('Prediction of bagged trees not good enough with ', rf_score, ' accuracy.')

if __name__ == '__main__':
    test_decisiontree_accuracy()
    test_boosting_accuracy()
    test_bagged_trees_accuracy()
    test_random_forest_accuracy()
