"""
An implementation of the plain Burrows Wheeler Transform
and a bijective variant using Lyndon Factors of the word.
"""

import cla_util as util
import datastructures as ds

#Computes the Burrows Wheeler Transform based on a Suffix Array
def BWT(omega):
    alpha = omega + "$" + omega
    sa = ds.SuffixArray(omega + "$")
    eta = ""
    i = 0
    n = len(omega)
    #Compute the preceding letters of the sorted letters
    while(i <= n):
        eta += alpha[sa[i] + n]
        i+=1
    return eta

#Computes Permutation Table to reverse the Burrows Wheeler Transform
def Permutation(eta):
    n = len(eta)
    pi = [0]*n
    alphabet = util.word_alphabet(eta)
    Lambda = [0]*len(alphabet)
    alphabet = sorted(alphabet)
    sigma = util.dictionary(alphabet)
    Lambda = util.letter_count(eta, sigma, alphabet)
    theta = [0]*len(Lambda)
    i = 1
    #Compute how many letters occure before in the sorted list
    while(i < len(theta)):
        theta[i] = theta[i-1] + Lambda[i-1]
        i += 1
    #Compute the final Permutation
    for i in range(n):
        letter = sigma[eta[i]]
        pi[i] = theta[letter]
        theta[letter] += 1
    return(pi)

#Retrive the original word from the transformed word
def BWT_inv(eta):
    pi = Permutation(eta)
    omega = ""
    n = len(eta)
    k = 0
    i = 0
    #Backtrack the original word with help of the permutation table
    for i in range(n-1):
        omega += eta[k]
        k = pi[k]
    return omega[::-1]

#Implementation of Duval's Algorithm for Lyndon Factors
def duval(w):
  i = 0
  n = len(w)
  factors = []
  while(i < n):
    j = i + 1
    k = i
    while(j < n and w[k] <= w[j]):
      if(w[k] < w[j]):
        k = i
      else:
        k += 1
      j += 1
    while(i <= k):
      factors.append(w[i:i+j-k])
      i += j-k
  return(factors)

#Computes the bijective Wheeler Transform with Lyndon factors
def BBWT(omega):
    #Compute all Lyndon factors
    factors = duval(omega)
    chi = util.cyclic_shifts(factors)
    #Sorting based on comparing infinite periodic repetitions
    tau = util.ipr_sort(chi)
    eta = ""
    #Strip last Characters of all sorted shiffted factors
    for i in range(len(tau)):
        eta += tau[i][-1]
    return(eta)

#Retrive the original word of the bijective transformed string
def BBWT_inv(eta):
    pi = Permutation(eta)
    omega = ""
    n = len(eta)
    nu = [False]*n
    k = 0
    j = 0
    #Backtrack the original word with help of the permutation table
    for i in range(n):
        #If letter has been used proceed to the next factor
        while(nu[k] != False):
            j += 1
            k = j
        omega += eta[k]
        nu[k] = True
        k = pi[k]
    return omega[::-1]
