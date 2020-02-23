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


def checkio(game_result: List[str]):
    board_size = len(game_result)
    rows = game_result
    columns = list(map(''.join, zip(*rows)))
    diagonals = list(map(''.join, zip(*[(row[i], row[board_size - 1 - i])
                                        for i, row in enumerate(rows)])))

    for player_char in ['X', 'O']:
        win_line = player_char * board_size
        if win_line in rows or win_line in columns or win_line\
                in diagonals:
            return player_char

    return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))
    assert checkio([
        "O.X",
        "XX.",
        "XO."]) == "X", "Xs wins again"
    assert checkio([
        "X.O",
        "XX.",
        "OOX"]) == "X", "Xs wins again"

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
