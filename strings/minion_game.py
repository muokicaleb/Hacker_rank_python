"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string S .

For Example:
String S= BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 
"""


def minion_game(s):
    vow = 'AEIOU'
    kevinScore = 0
    StuartScore = 0
    for i in range(len(s)):
        if s[i] in vow:
            kevinScore += (len(s) - i)
        else:
            StuartScore += (len(s) - i)

    if kevinScore > StuartScore:
        print ("Kevin", kevinScore)
    elif kevinScore < StuartScore:
        print ("Stuart", StuartScore)
    else:
        print ("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)