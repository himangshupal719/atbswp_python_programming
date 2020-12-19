import random

messages = ['It is certain',
           'It is decidedly so',
           'Yes definitely',
           'Reply hazy try again',
           'Ask again later',
           'Concentrate and ask again',
           'My reply is no',
           'Outlook not so good',
           'Very doubtful']

### numberOfMessages = len(messages) - 1
### messageNumber = random.randint(0, numberOfMessages)
### print(messages[messageNumber])


print(messages[random.randint(0, len(messages) - 1)])
           
