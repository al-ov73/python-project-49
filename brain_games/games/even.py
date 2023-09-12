#!/usr/bin/env python3
from random import randint


start_question = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    game_quest = randint(1, 1000)
    if game_quest % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return game_quest, right_answer
