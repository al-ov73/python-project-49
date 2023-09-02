#!/usr/bin/env python3
from random import randint
from brain_games.engine import game_engine


start_question='Answer "yes" if the number is even, otherwise answer "no".'

def game_question_def():
    game_question=randint(1,1000)
    return game_question

def right_answer_def(game_question):
    if game_question%2==0:
        right_answer='yes'
    else:
        right_answer='no'
    return right_answer


def main():
    print(start_question)
    game_question_def()
    right_answer_def()


if __name__ == '__main__':
    main()
