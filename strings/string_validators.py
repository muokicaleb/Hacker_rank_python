"""
You are given a string s .
Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints
0<len(s)<1000

Output Format

In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
In the second line, print True if s has any alphabetical characters. Otherwise, print False.
In the third line, print True if s has any digits. Otherwise, print False.
In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
In the fifth line, print True if s has any uppercase characters. Otherwise, print False.

Sample Input

qA2

Sample Output

True
True
True
True
True


"""

s = input()
print (any(i.isalnum() for i in s))
print (any(i.isalpha() for i in s))
print (any(i.isdigit() for i in s))
print (any(i.islower() for i in s))
print (any(i.isupper() for i in s))