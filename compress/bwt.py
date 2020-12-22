"""
An implementation of the plain Burrows Wheeler Transform
and a bijective variant using Lyndon Factors of the word.
"""


#Creates of Suffix Array
def SuffixArray(w):
    SA =sorted(range(len(w)), key=lambda i: w[i:])
    return(SA)

#Computes the Burrows Wheeler Transform based on a Suffix Array
def BWT(omega):
    alpha = omega + "$" + omega
    sa = SuffixArray(omega + "$")
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
    Lambda = []
    eta_sorted = sorted(eta)
    c = ""
    j = -1
    sigma = {}
    #Compute the occurences of all letters
    for i in range(n):
        if(eta_sorted[i] != c):
            c = eta_sorted[i]
            Lambda.append(1)
            j+=1
            sigma[c] = j
        else: Lambda[j] += 1
    theta = [0]*len(Lambda)
    i = 1
    #Compute how many letters occure before in the sorted list
    while(i < len(theta)):
        theta[i] = theta[i-1] + Lambda[i-1]
        i += 1
    #Compute the final Permutation
    for i in range(n):
        pi[i] = theta[sigma[eta[i]]]
        theta[sigma[eta[i]]] += 1
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
    m = len(factors)
    chi = []
    #Compute all Cyclic shifts
    for i in range(m):
        concat = factors[i] + factors[i]
        n = len(factors[i])
        for j in range(n):
            chi.append(concat[j:j+n])
    #TODO implement a propper sorting based on comparinginfinite periodic repetitions
    tau = sorted(chi)
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
