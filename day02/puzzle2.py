from enum import Enum
import os


class Play(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class Result(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6


def get_play_from_text(play: str):
    if play == "A":
        return Play.ROCK
    elif play == "B":
        return Play.PAPER
    elif play == "C":
        return Play.SCISSORS
    raise ValueError(f"Unsupported play, {play}")


def get_result_from_text(result: str):
    if result == "X":
        return Result.LOSE
    elif result == "Y":
        return Result.DRAW
    elif result == "Z":
        return Result.WIN
    raise ValueError(f"Unsupported result, {result}")


def calculate_my_play(opponent_play: Play, desired_result: Result):
    if desired_result == Result.DRAW:
        return opponent_play
    elif desired_result == Result.WIN:
        if opponent_play == Play.ROCK:
            return Play.PAPER
        elif opponent_play == Play.PAPER:
            return Play.SCISSORS
        elif opponent_play == Play.SCISSORS:
            return Play.ROCK
    elif desired_result == Result.LOSE:
        if opponent_play == Play.ROCK:
            return Play.SCISSORS
        elif opponent_play == Play.PAPER:
            return Play.ROCK
        elif opponent_play == Play.SCISSORS:
            return Play.PAPER
    raise ValueError(f"Unsupported combination of opponent_play {opponent_play} and desired_result {desired_result}")


def get_game_score(result: Result):
    return result.value


def get_play_score(play: Play):
    return play.value


with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    read_data = f.read()


total_score = 0


for round in read_data.splitlines():
    opponent_play = get_play_from_text(round.split()[0])
    desired_result = get_result_from_text(round.split()[1])
    my_play = calculate_my_play(opponent_play, desired_result)
    game_score = get_game_score(desired_result)
    play_score = get_play_score(my_play)
    total_score += (game_score + play_score)


print(total_score)
