import random
import pprint
numberOfStreaks = 0
#coinFlipList =[['H','H','T','T','H','H','H','H','H','H'], ['T','T','T','T','T','T','H','H','H','H']]

streaks = 0
NumberofExperiments = 10000
for experimentNumber in range(NumberofExperiments):
    #print('\n\n This is list #: ' + str(experimentNumber) + '\n')
    coinFlipList =[]
    # Code that creates a list of 100 'heads' or 'tails' values.
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
        
        #print(str(i)+' ' +  myList[i] +' count:' + str(count))
        if count == 6:
            streaks += 1
            count = 0
            #print('Count Reset')
           
     
        #print('-->' + 'Streak: ' + str(streaks))

chanceOfStreak = (streaks/(len(myList)*NumberofExperiments))*100
print('Total streaks: ' + str(streaks))
print('Chance of streak: ' + str(chanceOfStreak))
