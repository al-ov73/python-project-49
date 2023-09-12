from random import randint


start_question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    MAX_NUMBER = 100
    game_question = randint(1, MAX_NUMBER)
    right_answer = 'yes'
    for i in range(2, game_question):
        if game_question % i == 0:
            right_answer = 'no'
            break
    return game_question, right_answer
