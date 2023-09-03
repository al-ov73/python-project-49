#!/usr/bin/env python3
from random import randint


def definition_game_var():
    start_question = 'What is the result of the expression?'
    question = [randint(1, 100), randint(1, 100)]
    num1, num2 = question
    right_answer = 0
    if num1 < num2:
        for number in range(1, num1 + 1):
            if num1 % number == 0 and num2 % number == 0:
                right_answer = str(number)
    else:
        for number in range(1, num2 + 1):
            if num1 % number == 0 and num2 % number == 0:
                right_answer = str(number)
    # преобразовываем ответ в строку без []
    game_question = str(question)[1:len(str(question)) - 1:]
    return start_question, game_question, right_answer


def main():
    definition_game_var


if __name__ == '__main__':
    main()
