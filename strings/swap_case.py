""" sWAP cASE

 You are given a string S. Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

 For Example:
 Www.HackerRank.com → wWW.hACKERrANK.COM
 Pythonist 2 → pYTHONIST 2

 Input Format
 A single line containing a string S.

 Constraints
 0 < len(S) <= 1000

 Output Format
 Print the modified string S.

 Enter your code here. Read input from STDIN. Print output to STDOUT

 """


def swap_case(s):
    swapped = "".join(case.lower() if case.isupper() else case.upper() for case in s)
    return swapped


s = input()
result = swap_case(s)
print(result)