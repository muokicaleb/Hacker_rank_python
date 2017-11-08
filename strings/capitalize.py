"""
You are given a string . Your task is to capitalize each word of .

Input Format

A single line of input containing the string, .

Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

hello world

Sample Output

Hello World
"""


def capitalize(string):
    stringsplit = string.split(' ')
    ans =(' '.join((i.capitalize() for i in stringsplit)))
    return ans

if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)