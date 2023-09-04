#!/usr/bin/env python3
from random import randint


def def_progression_var():
    start_question = 'What number is missing in the progression?'
    first_num = randint(1, 10)
    step = randint(2, 5)
    list = []
    n = 10
    for i in range(n):
        list.append(first_num + (step * i))
    rand_elem = randint(0, n - 1)
    right_answer = str(list[rand_elem])
    list[rand_elem] = ".."
    list_str = str(list)
    # убираем квадратные скобки
    game_question = list_str[1:len(list_str) - 1:]
    # убираем '' вокруг исключенного элемента
    game_question = game_question.replace("'", "")
    # убираем ,
    game_question = game_question.replace(",", "")
    return start_question, game_question, right_answer


def main():
    def_progression_var()


if __name__ == '__main__':
    main()
