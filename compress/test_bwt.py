'''
Testing of the Burrows Wheeler Transform
'''

import bwt

#check if string does not change after transform and inversion
def BWT_test():
    string =  "ananasibananamamissisipi"
    assert(bwt.BWT_inv(bwt.BWT(string)) == string), ('Plain BWT does not recover original string')
    assert(bwt.BBWT_inv(bwt.BBWT(string)) == string), ('Bijective BWT does not recover original string')

if __name__ == '__main__':
    BWT_test()
