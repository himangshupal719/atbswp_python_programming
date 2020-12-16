def spam():
    eggs = 'spam local'
    print(eggs)  # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs)

eggs = 'global'
bacon()
print(eggs) # prints 'global'




# Output
# bacon local
# spam local
# bacon local
# global
