"""
You are given a string S.
Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.

Input Format

A single line containing the string S and integer value K separated by a space.

Output Format

Print the different combinations of string S on separate lines.

Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
"""
from itertools import combinations

S = input().split()
for i in range(1, int(S[1]) + 1):
    l = sorted(list(combinations(sorted(inpt[0]), i)))
    print('\n'.join(''.join(a) for a in l))
