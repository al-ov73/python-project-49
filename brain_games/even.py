#!/usr/bin/env python3
from random import randint
from brain_games.cli import welcome_user

def even_game():
    print('Welcome to the Brain Games!')
    name=welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i=0
    while i<3:
        random_number=randint(1,1000)
        print(f'Question: {random_number}')
        answer=input('Your answer: ')
        if random_number%2==0:
            if answer=='yes':
                print('Correct!')
                i+=1
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'yes'.")
                print(f"Let's try again, {name}!")
                break
        else:
            if answer=='no':
                print('Correct!')
                i+=1
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'no'.")
                print(f"Let's try again, {name}!")
                break
    if i==3:
        print(f'Congratulations, {name}!')

def main():
    even_game()


if __name__ == '__main__':
    main()
