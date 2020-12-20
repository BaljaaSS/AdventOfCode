from re import search
import collections

file1 = open('AdventOfCode/2020/Input/Input6.txt', 'r')
lines = file1.read().splitlines()
lines.append("")
lines.append("123")

Alphabet = 'abcdefghijklmnopqrstuvwxyz'

# %% Part-1
def CountAllYes(answers):
    return sum(1 for letter in Alphabet if search(letter, answers))

# %% Part-2
def CountSameYes(answers, numberOfPerson):
    countResult = collections.Counter(answers)
    return sum(1 for letter in Alphabet if countResult[letter] == numberOfPerson)

# %% Main
groupAnswers = ""
countAllYes = 0
countSameYes = 0
numberOfPerson = 0
alphabet = Alphabet
for line in lines:
    if (line == ''):
        countAllYes += CountAllYes(groupAnswers)
        countSameYes += CountSameYes(groupAnswers, numberOfPerson)
        groupAnswers = ""
        numberOfPerson = 0
    else:
        groupAnswers += line
        numberOfPerson += 1

print("Part-1: A sum of questions answered by anyone YES :", countAllYes)
print("Part-2: A sum of questions answered by everyone YES :", countSameYes)
