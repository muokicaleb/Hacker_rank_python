"""
You are given a string S.
Your task is to print all possible permutations of size K of the string in lexicographic sorted order.

Input Format

A single line containing the space separated string S and the integer value K.


Output Format

Print the permutations of the string S on separate lines.

Sample Input

HACK 2
Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

"""

from itertools import permutations
permstrng = input().split()
for i in sorted((permutations(permstrng[0], int(permstrng[1])))):
    print(''.join(i))
