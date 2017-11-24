"""
Read in two integers, a and b, and print three lines. 
The first line is the integer a//b division  (While using Python2 remember to import division from __future__). 
The second line is the result of the modulo operator:  a%b. 
The third line prints the divmod of  and .

Input Format 
The first line contains the first integer, a, and the second line contains the second integer, b.

Output Format 
Print the result as described above.

Sample Input

177
10
Sample Output

17
7
(17, 7)
"""

a = int(input())
b = int(input())
print(a // b)
print(a % b)
print(divmod(a, b))