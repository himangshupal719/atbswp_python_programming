## Input validation

print('How many cats  do you have?')
numCats = input()
try:
    if int(numCats)<0:
        print('You did not enter a valid number.')
    elif int(numCats) >= 4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')
except:
   print('You did not enter a number.')
