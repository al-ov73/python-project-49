#!/usr/bin/env python3
from random import randint


start_question = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    question = [randint(1, 100), randint(1, 100)]
    num1, num2 = question
    right_answer = 0
    if num1 < num2:
        for number in range(1, num1 + 1):
            if num1 % number == 0 and num2 % number == 0:
                right_answer = str(number)
    else:
        for number in range(1, num2 + 1):
            if num2 % number == 0 and num1 % number == 0:
                right_answer = str(number)
    # преобразовываем ответ в строку без [] и ','
    game_question = str(question)[1:len(str(question)) - 1:]
    game_question = game_question.replace(',', '')
    return game_question, right_answer
