#!/usr/bin/env python3
from random import randint
#from brain_games.cli import welcome_user
from brain_games.engine import game_engine


#def even_var():
start_question='Answer "yes" if the number is even, otherwise answer "no".'
    #return start_question

#def game_question_dev():
random_number=randint(1,1000)
game_question=random_number

#def right_answer():
if random_number%2==0:
    right_answer='yes'
else:
    right_answer='no'




def even_game():
    even_var()
    other()
    #start_question=even_var()
    #game_engine()

def main():
    even_game()


if __name__ == '__main__':
    main()
