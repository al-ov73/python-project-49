#!/usr/bin/env python3
from brain_games.games.prime import generate_question_answer, start_question
from brain_games.engine import game_engine


def main():
    game_engine(start_question, generate_question_answer)


if __name__ == '__main__':
    main()
