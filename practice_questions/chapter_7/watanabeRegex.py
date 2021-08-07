import re
nameList = ['Haruto Watanabe', 'Alice Watanabe', 'RoboCop Watanabe',
        'haruto Watanabe' , 'Mr. Watanabe', 'Watanabe','Haruto watanabe']
nameRegex = re.compile(r'([A-Z])[a-zA-Z]*\sWatanabe')

for  name in nameList:
    mo = nameRegex.search(name)
    if mo ==None:
        print(f'{name} does not match.')
    else:
        print(f'{name} does match.')
