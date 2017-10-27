"""
Consider a list (list = []). You can perform the following commands:

    insert i e: Insert integer at position .
    print: Print the list.
    remove e: Delete the first occurrence of integer e.
    append e: Insert integer e at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.

Initialize your list and read in the value of n followed by lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints

    The elements added to the list must be integers.

Output Format

For each command of type print, print the list on a new line.

"""


def list_manipulation(list1, operation):
    if operation[0] == 'insert':
        list1.insert(int(operation[1]), int(operation[2]))
    elif operation[0] == 'print':
        print(list1)
    elif operation[0] == 'remove':
        list1.remove(int(operation[1]))
    elif operation[0] == 'append':
        list1.append(int(operation[1]))
    elif operation[0] == 'sort':
        list1.sort()
    elif operation[0] == 'pop':
        list1.pop()
    elif operation[0] == 'reverse':
        list1.reverse()


n = int(input())
list1 = []
for a in range(0, n):
    spliter = [str(i) for i in input().strip().split()]
    list_manipulation(list1, spliter)