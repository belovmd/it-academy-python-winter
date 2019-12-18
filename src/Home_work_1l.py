BOARD_SIZE = 8


class BailOut(Exception):
    pass


def validate(queens1):
    left = right = col = queens1[-1]
    for r in reversed(queens1[:-1]):
        left, right = left - 1, right + 1
        if r in (left, col, right):
            raise BailOut


def add_queen(queens1):
    for k in range(BOARD_SIZE):
        test_queens = queens1 + [k]
        try:
            validate(test_queens)
            if len(test_queens) == BOARD_SIZE:
                return test_queens
            else:
                return add_queen(test_queens)
        except BailOut:
            pass
    raise BailOut


queens = add_queen([])
print(queens)
print("\n".join(". " * q + "Q " + ". " * (BOARD_SIZE - q - 1) for q in queens))
