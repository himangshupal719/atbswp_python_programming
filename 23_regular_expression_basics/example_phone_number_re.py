import re

message = 'Call me 415-555-1211 tomorrow, or at 415-555-9299 for my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #specifying the pattern - create RegX object. \d represnts digit numeric character. 

mo = phoneNumRegex.search(message) #search the string with search method. this returns mtch object.
print(mo.group()) #match object has group method to get the matched string. printing out the results

mo = phoneNumRegex.findall(message) #find all  method retuerns list of strings for the matching pattern. 
print(mo)
