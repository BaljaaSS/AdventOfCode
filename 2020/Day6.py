from re import search
import collections

file1 = open('AdventOfCode/2020/Input/Input6.txt', 'r')
lines = file1.read().splitlines()
lines.append("")
lines.append("123")

Alphabet = 'abcdefghijklmnopqrstuvwxyz'

# %% Part-1
def CountAllYes(answers):
    count = 0
    for letter in Alphabet:
        if (search(letter, answers)):
            count += 1
    return count

# %% Part-2
def CountSameYes(answers, numberOfPerson):
    count = 0
    countResult = collections.Counter(answers)
    for letter in Alphabet:
        if (countResult[letter] == numberOfPerson):
            count += 1
    return count


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
