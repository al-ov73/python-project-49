#!/usr/bin/env python3
from brain_games.cli import welcome_user


def game_engine(game_var):
    print('Welcome to the Brain Games!')
    name=welcome_user()
    start_question, _, _=game_var()
    print(start_question)
    i=0
    while i<3:
        _, game_question, right_answer=game_var()
        print(f'Question: {game_question}')
        answer=input('Your answer: ')
        if answer==right_answer:
            print('Correct!')
            i+=1
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}.")
            print(f"Let's try again, {name}!")
            break
    if i==3:
        print(f'Congratulations, {name}!')


def main():
    even_game()


if __name__ == '__main__':
    main()
