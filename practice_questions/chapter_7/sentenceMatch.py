import re

testList = ['Alice eats apples.',
'Bob pets cats.',
'RoboCop eats apples.',
'ALICE THROWS FOOTBALLS.',
'Carol throws baseballs.',
'Alice throws Apples.',
 'Carol eats 7 cats.',
'BOB EATS CATS.']

sentenceRegex = re.compile(r'(alice|bob|carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.IGNORECASE)
for sentence in testList:
    mo = sentenceRegex.search(sentence)
    if mo == None:
        print(f'\'{sentence }\' is not a match.')
    else:
        print(f'\'{sentence }\' is a match.')
        
        
