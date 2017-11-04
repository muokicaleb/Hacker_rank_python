"""Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

    Mat size must be X. ( is an odd natural number, and is times .)
    The design should have 'WELCOME' written in the center.
    The design pattern should only use |, . and - characters.

Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------

Input Format

A single line containing the space separated values of and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27

Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

Note:
More than lines of code will result in a score of . Comment lines are counted. Blank lines are not counted.
"""
N, M = map(int, input().split())
form = [('.|.' * (2 * i + 1)).center(M, '-') for i in range(N // 2)]
print('\n'.join(form + ['WELCOME'.center(M, '-')] + form[::-1]))