'''
Implementation of Principal Component Analysis.
'''

import numpy as np
import pickle

#Principal Component Analysis based on Eigenvector and Eigenvalues
def compute_PCs(X):
    #Step 1: Center Data arround 0
    X_centered = (X - np.mean(X, axis=0))
    #Step 2: Compute Covariance Matrix
    covariance_matrix = np.cov(X_centered.T)
    #Step 3: Compute eigenvector and eigenvalues for the Covariance Matrix
    eig_vals, eig_vecs = np.linalg.eig(covariance_matrix)
    #Step 4: Sort Eigenvalues based on highest inforamtion gain
    fraction_variance_explained = eig_vals / np.sum(eig_vals)
    idx = np.argsort(-fraction_variance_explained)
    principal_components = eig_vecs[:, idx].T
    return principal_components, fraction_variance_explained

#Select Principal Components based on percentage of information explained
def select_PCs(principal_components, variance_explained, percent_variance=0.90):
    #Computing the amount of Components necessary to explain the desired percent
    i = 0
    var_expl = 0
    while(var_expl < percent_variance):
      var_expl += variance_explained[i]
      i+=1
    variance_explained_kept = np.array(variance_explained[0:i])
    principal_components_kept = np.array(principal_components[0:i])
    return principal_components_kept, variance_explained_kept

#Compute PCA scores based on principal Components
def compute_PCA(X, principal_components):
    pc_scores = np.dot(principal_components, X.T)
    return pc_scores

#Complete PCA projection for Data
def PCA(X, information_explained=0.90):
    principal_components, variance_explained = compute_PCs(X)
    selected_pcs, information = select_PCs(principal_components, variance_explained)
    pc_scores = compute_PCA(X, selected_pcs)
    return pc_scores
