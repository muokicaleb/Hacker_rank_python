from collections import OrderedDict


def merge_the_tools(string, k):
    a = len(string)
    b = int(a / k)
    for i in range(b):
        start = i * k
        end = start + k
        print("".join(OrderedDict.fromkeys(string[start:end])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)