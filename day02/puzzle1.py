from enum import Enum
import os


SCORE_LOSE = 0
SCORE_DRAW = 3
SCORE_WIN = 6


class Play(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def get_play_from_text(play: str):
    if play in ("A", "X"):
        return Play.ROCK
    elif play in ("B", "Y"):
        return Play.PAPER
    elif play in ("C", "Z"):
        return Play.SCISSORS
    raise ValueError(f"Unsupported play, {play}")


def calculate_game_score(opponent_play: Play, my_play: Play):
    if opponent_play == my_play:
        return SCORE_DRAW
    if opponent_play == Play.ROCK:
        if my_play == Play.PAPER:
            return SCORE_WIN
        elif my_play == Play.SCISSORS:
            return SCORE_LOSE
    elif opponent_play == Play.PAPER:
        if my_play == Play.ROCK:
            return SCORE_LOSE
        elif my_play == Play.SCISSORS:
            return SCORE_WIN
    elif opponent_play == Play.SCISSORS:
        if my_play == Play.ROCK:
            return SCORE_WIN
        elif my_play == Play.PAPER:
            return SCORE_LOSE
    raise ValueError(f"Unsupported combination of {opponent_play} and {my_play}")


def get_play_score(play: Play):
    return play.value


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    read_data = f.read()


total_score = 0


for game_play in read_data.splitlines():
    opponent_play = get_play_from_text(game_play.split()[0])
    my_play = get_play_from_text(game_play.split()[1])
    game_score = calculate_game_score(opponent_play, my_play)
    play_score = get_play_score(my_play)
    total_score += (game_score + play_score)


print(total_score)
