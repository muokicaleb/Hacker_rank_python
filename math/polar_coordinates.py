"""
Task 
You are given a complex Z. Your task is to convert it to polar coordinates.

Input Format

A single line containing the complex number Z. Note: complex() function can be used in python to convert the input as a complex number.


Given number is a valid complex number

Output Format

Output two lines: 
The first line should contain the value of R. 
The second line should contain the value of $.

Sample Input

  1+2j
Sample Output


 1.1071487177940904
"""
from cmath import sqrt, phase
cnum = complex(input())
print sqrt(pow(cnum.real, 2) + pow(cnum.imag, 2)).real
print phase(complex(cnum.real,cnum.imag))