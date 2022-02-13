import random

def rock_paper_scissors():
    while True:
        guess = input("rock, paper or scissors? ")
        if guess == 'stop':
            break
        if guess != 'rock' or guess != 'paper' or guess != 'scissors':
            print('you must enter one of the choices')
            continue
        computer_guess = random.choice(['rock', 'paper', 'scissors'])
        
        if guess == computer_guess:
            print(f'{guess} vs {computer_guess} is a tie')

        elif (guess == 'rock' and computer_guess =='paper') or (guess == 'paper' and computer_guess == 'scissors') or (guess == 'scissors' and computer_guess == 'rock'):
            print(f'{guess} vs {computer_guess} is a loss')

        else:
            print(f'{guess} vs {computer_guess} is a win')

rock_paper_scissors()