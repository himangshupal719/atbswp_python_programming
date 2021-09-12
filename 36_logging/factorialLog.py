import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

logging.debug('Start of the program')

def factorial(n):
    logging.debug(f'Start of factorial ({n})')
    total = 1
    #for i in range(n+1): # with issue
    for i in range(1, n+1): #with fix
        total *= i
        logging.debug(f'i is {str(i)}, total is {str(total)} ')
    logging.debug(f'End of factorial ({5})')
    return total


print(f'{factorial(5)}')
logging.debug('End of program')


