'''
Example of using the implemented Burrows Wheeler Transform.
'''

import bwt

#Read in the book Ulysses of James Joyce as a string
file = open("sample_data/ulysses.txt")
string = file.read().replace("\n", " ")
file.close()

#Use the first 50000 characters of the complete book
string = string[0:50000]

#Transform string based on bijective Burrows Wheeler Transform
enc = bwt.BBWT(string)
#Recover original string using the transformed string
dec = bwt.BBWT_inv(enc)

#write transformed string as text file
text_file = open("sample_data/encoded.txt", "wt")
n = text_file.write(enc)
text_file.close()

#write recovered string as text file
text_file = open("sample_data/decoded.txt", "wt")
n = text_file.write(dec)
text_file.close()
