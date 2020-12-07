# Chapter 2 - Question 9.
# 9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

print('HELLO, HOWDY, GREETINGS')

print('Enter an integer: ')
spam = int(input())

if spam == 1:
    print('HELLO!')
elif spam == 2:
    print('HOWDY!')
else:
    print('GREETINGS!')
    
