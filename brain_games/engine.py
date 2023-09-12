#!/usr/bin/env python3
from brain_games.cli import welcome_user


def game_engine(start_question, game_var):
    ROUNDS_QTY = 3
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(start_question)
    i = 0
    while i < ROUNDS_QTY:
        game_question, r_answer = game_var()
        print(f'Question: {game_question}')
        answer = input('Your answer: ')
        if answer == r_answer:
            print('Correct!')
            i += 1
        else:
            print(
                f"{answer} is wrong answer ;(. Correct answer was {r_answer}.")
            print(f"Let's try again, {name}!")
            break
    if i == 3:
        print(f'Congratulations, {name}!')


def main():
    game_engine()


if __name__ == '__main__':
    main()
