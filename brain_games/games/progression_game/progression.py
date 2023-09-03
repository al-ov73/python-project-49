#!/usr/bin/env python3
from random import randint


def game_var():
    start_question='What number is missing in the progression?'
    first_num=randint(1,10)
    rand_step=randint(2,5)
    list=[]
    n=10
    for i in range(n):
        list.append(first_num+(rand_step*i))
    rand_elem=randint(0,n-1)
    right_answer=str(list[rand_elem])
    list[rand_elem]=".."
    list_str=str(list)
    game_question=list_str[1:len(list_str)-1:]
    game_question=game_question.replace("'","")
    return start_question, game_question, right_answer


def main():
    game_var()


if __name__ == '__main__':
    main()
