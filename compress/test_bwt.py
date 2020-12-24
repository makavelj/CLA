'''
Tests for the Burrows Wheeler Transform
'''

import bwt


string =  "ananasibananamamissisipi"

#check if string does not change after transform and inversion
assert(bwt.BWT_inv(bwt.BWT(string)) == string)
assert(bwt.BBWT_inv(bwt.BBWT(string)) == string)
