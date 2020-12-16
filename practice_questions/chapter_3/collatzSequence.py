import sys
def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return 3 * number + 1


print("Enter a number: ")
number = input()
try:
    collatzNumber = collatz(int(number))
    print(collatzNumber)

    while True:
        if collatzNumber == 1:
            sys.exit()
        collatzNumber = collatz(collatzNumber)
        print(collatzNumber)
except  ValueError:
    print('Error: You did not enter integer.' )
 
        



