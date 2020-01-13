# Tic-Tac-Toe, sometimes also known as Xs and Os,
# is a game for two players (X and O) who take turns
# marking the spaces in a 3×3 grid. The player who succeeds
# in placing three respective marks in a horizontal,
# vertical, or diagonal rows (NW-SE and NE-SW) wins the game.
#
# But we will not be playing this game. You will be the referee
# for this games results. You are given a result of a game and
# you must determine if the game ends in a win or a draw as well
# as who will be the winner. Make sure to return "X" if the
# X-player wins and "O" if the O-player wins.
# If the game is a draw, return "D".
#
# A game's result is presented as a list of strings,
# where "X" and "O" are players' marks and "." is the empty cell.


from typing import List


def checkio(game_result: List[str]) -> str:
    for i in range(3):
        if game_result[i][0] == game_result[i][1] == game_result[i][2]\
                and game_result[i][0] != ".":
            return game_result[i][0]
        elif game_result[0][i] == game_result[1][i] == game_result[2][i]\
                and game_result[0][i] != ".":
            return game_result[0][i]
        elif game_result[0][0] == game_result[1][1] == game_result[2][2]\
                and game_result[0][0] != ".":
            return game_result[1][1]
        elif game_result[0][2] == game_result[1][1] == game_result[2][0]\
                and game_result[0][2] != ".":
            return game_result[1][1]
    return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
