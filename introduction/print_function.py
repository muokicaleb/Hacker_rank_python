"""
Read an integer n.

Without using any string methods, try to print the following:
123...n
Note that "..." represents the values in between.

Input Format
The first line contains an integer n. 
"""
if __name__ == '__main__':
    n = int(input())
    i = 1
    while (i <= n):
        print(i, end="")
        i = i + 1
