# Local scope cannot use variable in other local scopes

def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()

# Output
# 99
