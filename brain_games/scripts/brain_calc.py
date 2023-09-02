#!/usr/bin/env python3
from brain_games.games.calc_game.calc import game_question_def, start_question, right_answer_def
from brain_games.engine import game_engine


def main():
    game_engine(start_question, game_question_def, right_answer_def)


if __name__ == '__main__':
    main()
