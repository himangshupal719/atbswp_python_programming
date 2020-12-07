# Chapter 2 Question 13
# 13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

print('Print 1 to 10 - Usng for loop')

for i in range(1, 11):
    print(i)

print(' ')
print('Print 1 to 10 - Usng while loop')

j = 0
while True:
    j = j + 1
    print(j)
    if j == 10:
        break
