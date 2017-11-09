"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format

The first line of input contains an integer, M.
The second line contains M space-separated integers.
The third line contains an integer, N .
The fourth line contains N space-separated integers.

"""
a, b = [set(input().split()) for _ in range(4)][1::2]
print ('\n'.join(sorted(a ^ b, key=int)))
