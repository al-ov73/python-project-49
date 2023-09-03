#!/usr/bin/env python3
from random import randint


def definition_game_var():
    start_question = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_question = randint(1, 1000)
    if game_question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return start_question, game_question, right_answer


def main():
    definition_game_var()


if __name__ == '__main__':
    main()
