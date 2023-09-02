#!/usr/bin/env python3
from random import randint
from re import findall
from brain_games.engine import game_engine


start_question='What is the result of the expression?'

def game_question_def():
    question=[randint(1,100),randint(1,100)]
    question_str=str(question)
    game_question=question_str[1:len(question_str)-1:]
    return game_question

def right_answer_def(game_question):
    num1,num2=findall(r'\d+',game_question)
    num1=int(num1)
    num2=int(num2)
    devisor=0
    if num1<num2:
        for number in range(1,num1+1):
            if num1%number==0 and num2%number==0:
                devisor=number
    else:
        for number in range(1,num2+1):
            if num1%number==0 and num2%number==0:
                devisor=number
    return str(devisor)


def main():
    print(start_question)
    game_question_def()
    right_answer_def()


if __name__ == '__main__':
    main()
