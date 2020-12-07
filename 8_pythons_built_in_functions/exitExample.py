import sys

while True:
    print('Type exit tot exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
