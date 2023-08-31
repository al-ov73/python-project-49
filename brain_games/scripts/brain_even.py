#!/usr/bin/env python3
from brain_games.even_game.even import start_question, game_question, right_answer
from brain_games.engine import game_engine


def main():
    #even_game()
    game_engine(start_question, game_question, right_answer)


if __name__ == '__main__':
    main()
