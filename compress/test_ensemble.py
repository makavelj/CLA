'''
Test for ensemble methods.
'''

import decisiontree as dt
import util
from sklearn.datasets import load_wine
from sklearn import tree


#Assert that the decision tree achieves result as good as sk learn tree
def test_decisiontree_accuracy():
    X, t = load_wine(return_X_y=True)
    X_train, X_test, t_train, t_test = util.split_data(X, t)
    dtree = dt.build_tree(X_train, t_train, 0, max_depth=3, n_labels=3)
    count = 0
    for i in range(len(X_test)):
        if(t_test[i] == dt.predict_tree(dtree, X_test[i])):
            count += 1
    dt_score =  count/len(t_test)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, t_train)
    predsk = clf.predict(X_test)
    skcounter = 0
    for i in range(len(predsk)):
        if(predsk[i] == t_test[i]):
            skcounter += 1
    sk_score = skcounter/len(t_test)
    assert(sk_score <= dt_score)


if __name__ == '__main__':
    test_decisiontree_accuracy()
