"""
Simple test for Vector Qunatization.
"""


import vector_quantization as vq

def vq_clustering_test():
  sample_data = [[25,34,22,27,33,33,31,22,35,34,67,54,57,43,50,57,59,52,65,47,49,48,35,33,44,45,38,43,51,46],[79,51,53,78,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,25,20,14,12,20,5,29,27,8,7]]
  sample_data_transformed = np.array(sample_data).T
  clustering, vector_values = vq.vector_quantization(sample_data_transformed, vectors=3)
  j = 2
  k = 0
  for i in range(len(clustering)-1):
    if(clustering[i] != clustering[i+1]): j -= 1
    else: k+=1
  assert(j == 0 and k == 27)
  return clustering
  
if __name__ == '__main__':
  vq_clustering_test()
    
