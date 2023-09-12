from random import randint


"""
Ошибка, если конец диапазона - 2

Traceback (most recent call last):
  File "main.py", line 19, in <module>
    start_question, game_question, right_answer=game_var()
  File "main.py", line 16, in game_var
    return start_question, game_question, right_answer
UnboundLocalError: local variable 'right_answer' referenced before assignment
"""


start_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    MAX_NUMBER = 100
    game_question = randint(2, MAX_NUMBER)
    for i in range(2, game_question):
        if game_question % i == 0:
            right_answer = 'no'
            break
        else:
            right_answer = 'yes'
    return game_question, right_answer
