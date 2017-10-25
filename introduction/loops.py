"""
Loops

Task 
Read an integer n. For all non-negative integers i < n, print i**2. See the sample for details.

Input Format
The first and only line contains the integer, n.

Constraints
1 <= n <= 20

Output Format
Print n lines, one corresponding to each i.
"""
n = int(input())
if (n >= 1 and n <= 20):
    for n in range(0, n):
        print (n**2)