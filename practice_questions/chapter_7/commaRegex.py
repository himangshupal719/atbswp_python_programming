import re

commaRegex = re.compile(r'(^\d{1,3}(,\d{3})*$)')
match = commaRegex.findall('1,123,232,999')
#match = commaRegex.findall('42')
#match = commaRegex.findall('1,234')
#match = commaRegex.findall('6,368,745')
#match = commaRegex.findall('12,34,567')
#match = commaRegex.findall('1234')
#
#'1234'


print(match)
for numbers in match:
    print(numbers[0])

