# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails.
# Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it.
# Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. 

import random
import pprint
numberOfStreaks = 0

streaks = 0
NumberofExperiments = 10000
for experimentNumber in range(NumberofExperiments):
    
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlipList =[]
    for coinFlip in range(100):
        coinFlipList.append(random.choice(['H','T']))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    count = 1
    myList = coinFlipList
    for i in range(len(myList)):
        if i == 0:
            pass
        elif myList[i] == myList[i-1]:
            count += 1
        else:
            count = 1
        
        if count == 6:
            numberOfStreaks += 1
            count = 0

chanceOfStreak = (numberOfStreaks/(len(myList)*NumberofExperiments))*100
print('Total streaks: ' + str(numberOfStreaks))
print('Chance of streak: ' + str(round(chanceOfStreak,4)))
