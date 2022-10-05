import random


instruction = """ 
Welcome to Rock, Paper, Scissors!
---------------------------------
Your options are:
- Rock
- Paper
- Scissors
**********************
GOOD LUCK!
"""
print(instruction)


options = 'rock', 'paper', 'scissors'
human = input("Enter your selection: ").lower()


computer = random.choice(options)


# ..........................................................................#

output = 'Tie'
output_2 = 'You win'
output_3 = 'Computer win'



if human in options: # ensures that user picks item from the list
    print(f'computer picked: {computer}')
    while True:
        if computer == human:
            print(output)
            break

    while True:
        if human == 'rock' and computer == 'paper':
            print(output_3)
        break

    while True:
        if human == 'rock' and computer == 'scissors':
            print(output_2)
        break

    while True:
        if human == 'paper' and computer == 'rock':
            print(output_2)
        break

    while True:
        if human == 'paper' and computer == 'scissors':
            print(output_3)
        break

    while True:
        if human == 'scissors' and computer == 'rock':
            print(output_3)
        break

    while True:
        if human == 'scissors' and computer == 'paper':
            print(output_2)
        break

else:
     print('Oops! What happened?')
print('\tWANT TO TRY AGAIN?')

