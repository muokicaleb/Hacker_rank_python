 """
  Task
  You are given a string S.
  Your task is to print all possible size k replacement combinations of the string in lexicographic sorted order.

  Input Format
  A single line containing the string S and integer value k separated by a space.

  Constraints
  0 < k <= len(S)
  The string contains only UPPERCASE characters.

  Output Format
  Print the combinations with their replacements of string S on separate lines.


  Enter your code here. Read input from STDIN. Print output to STDOUT
  """

from itertools import combinations_with_replacement

S = input().split(' ')

for i in combinations_with_replacement(sorted(S[0]), int(S[1])):
    print (''.join(i))
