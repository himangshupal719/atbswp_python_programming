#  Local variables cannot be used in global scope

def spam():
    eggs = 31337

spam()
print(eggs)


##  Output of the above program
# Traceback (most recent call last):
 # File "C:\Users\himan\OneDrive\Documents\Interview_Prep\My_Learning_Cognizant\atbswpython\atbswp_python_programming\10_global_and_local_scopes\global_local_example1.py", line 7, in <module>
 #   print(eggs)
#NameError: name 'eggs' is not defined
