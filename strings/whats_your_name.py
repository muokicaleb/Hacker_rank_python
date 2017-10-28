"""
You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

    Hello firstname lastname! You just delved into python.

Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last name ≤ .

Output Format

Print the output as mentioned above.

Sample Input

Guido
Rossum

Sample Output

Hello Guido Rossum! You just delved into python.

"""


def print_full_name(a, b):
    name = print("Hello %s %s! You just delved into python." % (a, b))
    return name


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)