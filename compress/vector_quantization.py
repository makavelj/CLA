"""
Implementation of Vector Quantization based on simple K-Means Clustering.
"""

import numpy as np
import random 


MAX = 9999999999999999

#Vector Quantization algorithm for clustering
def vector_quantization(X, vectors=5, epsilon=1E-4, max_iteration=100, distance=euclidean):
  X = np.array(X)
  n = len(X[0])
  m = len(X)
  min, max = [], []
  #Setup 1: Get min and max values for all attributes
  for i in range(n):
    min.append(np.amin(X[:,i]))
    max.append(np.amax(X[:,i]))
  means = []
  #Setup 2: Initialize random starting points based on random samples
  for i in range(vectors):
    mean = []
    for j in range(n):
      mean.append(random.uniform(min[j], max[j]))
    means.append(mean)
  clusters = [0]*m
  iterations = 0
  eps = MAX
  #Start main process of clustering points
  while(iterations < max_iteration and eps > epsilon):
    #Step 1: Cluster points to closest vector
    for i in range(m):
      min = MAX
      for j in range(vectors):
        dist = distance(X[i],means[j])
        if(dist < min):
          min = dist
          clusters[i] = j
    #Step 2: Optimize distance of vector to clustered points
    eps = 0
    for i in range(vectors):
      epsilon_diff = 0
      indices = [j for j, x in enumerate(clusters) if x == i]
      sum = [0]*n
      for j in range(len(indices)):
        sum += X[indices[j]]
      if(len(indices) > 0):
        means_old = means[i]
        means[i] = [x / len(indices) for x in sum]
        epsilon_diff = distance(means[i], means_old)
      eps += epsilon_diff
    iterations += 1
  return clusters, means

#Compute distance of two vectors based on euclidean metric
def euclidean(x, y):
  return np.linalg.norm(np.array(x)-np.array(y))

#Compute distance of two vectors based on city block metric
def manhattan(x, y):
  return np.linalg.norm(np.array(x)-np.array(y),1)
