# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']
# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma and a space,
# with and inserted before the last item. For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.

def commaSeparated(inputList):
    commasSeparatedString = ""
    inputList.insert(-1, 'and')
    numberOfElement = len(inputList)
    for index, element in enumerate(inputList):
        if index == 0:
            commasSeparatedString = element
        elif index > 0 and index < (numberOfElement -1):
            commasSeparatedString = commasSeparatedString + ","+" "+element
        else: 
            commasSeparatedString += " "+element
        
    return commasSeparatedString



spam = ['apples', 'bananas', 'tofu', 'cats']
print(commaSeparated(spam))
