while True:
    print('Enter yout age:')
    age = input()
    if age.isdecimal():
        break
    else:
        print('Print enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    else:
        print('Password can only have letters and numbers.')
