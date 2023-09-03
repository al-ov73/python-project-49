#!/usr/bin/env python3
from random import randint, choice


def definition_game_var():
    start_question = 'What is the result of the expression?'
    first_num = randint(1, 10)
    math_action = choice(["+", "-", "*"])
    last_num = randint(1, 10)
    game_question = str(first_num) + " " + math_action + " " + str(last_num)
    if math_action == '+':
        right_answer = str(first_num + last_num)
    elif math_action == '-':
        right_answer = str(first_num - last_num)
    else:
        right_answer = str(first_num * last_num)
    return start_question, game_question, right_answer


def main():
    definition_game_var()


if __name__ == '__main__':
    main()
