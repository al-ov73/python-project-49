#!/usr/bin/env python3
from random import randint
from brain_games.scripts.brain_games import welcome_user
import brain_games.cli


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
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
        else:
            if answer=='no':
                print('Correct!')
                i+=1
            else:
                print(f"{answer} is wrong answer ;(. Correct answer was 'no'.")
    print(name)


if __name__ == '__main__':
    main()
print('Welcome to the Brain Games!')
