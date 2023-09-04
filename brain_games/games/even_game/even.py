#!/usr/bin/env python3
from random import randint


def def_even_var():
    start_quest = 'Answer "yes" if the number is even, otherwise answer "no".'
    game_quest = randint(1, 1000)
    if game_quest % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return start_quest, game_quest, right_answer


def main():
    def_even_var()


if __name__ == '__main__':
    main()
