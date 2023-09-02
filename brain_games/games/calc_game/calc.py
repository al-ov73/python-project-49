#!/usr/bin/env python3
from random import randint, choice
from brain_games.engine import game_engine


start_question='What is the result of the expression?'

def game_question_def():
    first_num=randint(1,10)
    math_action=choice(["+","-","*"])
    last_num=randint(1,10)
    game_question=str(first_num)+" "+math_action+" "+str(last_num)
    return game_question

def right_answer_def(game_question):
    question_strip=game_question.replace(" ","")
    for index, char in enumerate(question_strip):
        if char in ['+','-','*']:
            if char=='+':
                answer=int(question_strip[:index])+int(question_strip[index+1:])
            elif char=='-':
                answer=int(question_strip[:index])-int(question_strip[index+1:])
            else:
                answer=int(question_strip[:index])*int(question_strip[index+1:])
            break
    return str(answer)


def main():
    print(start_question)
    game_question_def()
    right_answer_def()


if __name__ == '__main__':
    main()

