import random


instruction = """ 
Welcome to Rock, Paper, Scissors!
---------------------------------
"""

print(instruction)
print()

options= ['rock', 'paper', 'scissors']
print('Your options are: \n') # \n can be added either at the beginning or the end of the syntax

for item in options:
    output = (f'- {item}').title()
    print(output)

print()

human = input("Enter your selection: ").lower() # user enters data. used method function (.title()) to ensure user data turns lower case
print(human)
computer = random.choice(options)


if human not in options:
    print('Oops! What happened?')

else:
     print(f'computer picked: {computer}')

if human == 'rock' and computer == 'scissors':
    print('You wins')
elif human == 'rock' and computer == 'paper':
    print('computer wins')

elif human == 'paper' and computer == 'rock':
    print('You wins')
elif human == 'paper' and computer == 'scissors':
    print('computer wins')

elif human == 'scissors' and computer == 'rock':
    print('computer wins')
elif human == 'scissors' and computer == 'paper':
    print('You wins')

elif human == computer:
    print('Tie')