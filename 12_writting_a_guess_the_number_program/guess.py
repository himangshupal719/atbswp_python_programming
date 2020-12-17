# This is the guess the number game

import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ',' + ' I am thinking of a number between 1 and 20.')

secretNumber = random.randint(1, 20)

# print('DEBUG: The Secret Number is ' + str(secretNumber))

for  guessedNumber in range(1, 7):

    print('Take a guess.')
    guess = int(input())

    if  guess > secretNumber:
        print('Your guess is too high.')
    elif guess < secretNumber:
        print('Your guess is too low.')
    else:
        break  # This condition is the correct guess!

if guess == secretNumber:
    print('Good Job, ' + name + ' You guessed my  number in ' + str(guessedNumber) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber)+ '.')
    


