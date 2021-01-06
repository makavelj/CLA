'''
Implementation of decision tree with splitting based on entropy.
'''

import numpy as np
import util


MAX = 999999999999999999999999999

#Node of decision tree indicating which subset to consider in next level
class Node:
    def __init__(self, left, right, n_feat, threshold):
        self.left = left
        self.right = right
        self.n_feat = n_feat
        self.threshold = threshold
    def getInfo(self):
      return(self.n_feat, self.threshold)
    def hasChild(self):
      return True
    def predict_tree(self, x):
      if(self.hasChild()):
        feat_n, thresh = self.getInfo()
        feat_x = x[feat_n]
        if(feat_x < thresh):
          return self.left.predict_tree(x)
        else:
          return self.right.predict_tree(x)
      else:
        return self.getInfo()

#Leaf at the end of the tree making the decision
class Leaf:
    def __init__(self, label):
        self.label = label
    def getInfo(self):
      return(self.label)
    def hasChild(sef):
      return False

#Build decision tree based on dataset
def build_tree(X, y, y_inv=None, depth=0, max_depth=3, n_labels=2, split=util.entropy):
    if len(y) < 1:
        return Leaf(np.argmin(np.bincount(y_inv)))
    if depth == max_depth:
        return Leaf(np.argmax(np.bincount(y)))
    best_information = MAX
    best_feat= -1
    best_split = 0.0
    #Iterate threw all features
    for n_feat in range(X.shape[1]):
        x_candidates = define_candidates(X.T[n_feat])
        n = X.shape[0]
        #Find best candidate value
        for i in range(len(x_candidates)):
             # split column into left and right
             row =  X.T[n_feat]
             left, right = left_right_split(value = x_candidates[i], row=row, y=y)
             # calculate entropy coeficients for left and right
             left_entropy, right_entropy = split(left), split(right)
             # calculate wighted entropy
             information_gain = (len(left)/n)*left_entropy + (len(right)/n)*right_entropy
             # save split with best information gain
             if information_gain < best_information:
                 best_information = information_gain
                 best_split = x_candidates[i]
                 best_left = left
                 best_right = right
                 best_feat = n_feat

    left_X = []
    right_X = []
    #Based on best candidate and feature split set
    for j in range(X.shape[0]):
        row = X.T[best_feat]
        if row[j] < best_split:
            left_X.append(X[j])
        else:
            right_X.append(X[j])

    node = Node(None,None,best_feat,best_split)
    node.left = build_tree(np.array(left_X), best_left, best_right, depth+1, max_depth, n_labels)
    node.right = build_tree(np.array(right_X), best_right, best_left, depth+1, max_depth, n_labels)
    return node

#Split data based on on threshold value
def left_right_split(value, row, y):
    left, right = list(), list()
    n = len(row)
    for i in range(n):
        if row[i] < value:
            left.append(int(y[i]))
        else:
            right.append(int(y[i]))
    return np.array(left), np.array(right)


#Traverse tree to make a decision for x
def predict_tree(node, x):
  if(node.hasChild()):
    feat_n, thresh = node.getInfo()
    feat_x = x[feat_n]
    if(feat_x < thresh):
      return predict_tree(node.left, x)
    else:
      return predict_tree(node.right, x)
  else:
      return node.getInfo()

#Defines candidates for possible splitts
def define_candidates(X):
    X_sorted = sorted(X)
    x_candidates = []
    cmp1 = X_sorted[0]
    #find suitable candidates
    for i in range(1, len(X)):
        cmp2 =  X_sorted[i]
        candidate = (cmp1 + cmp2)/2
        x_candidates.append(candidate)
        cmp1 =  X_sorted[i]
    return x_candidates
