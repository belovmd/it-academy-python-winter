BOARD_SIZE = 8


def under_attack(col, queens2):
    left = right = col

    for r, c in reversed(queens2):
        left, right = left - 1, right + 1

        if c in (left, col, right):
            return True
    return False


def solve(n):
    if n == 0:
        return [[]]

    smaller_solutions = solve(n - 1)

    return [solution + [(n, j + 1)]
            for j in range(BOARD_SIZE)
            for solution in smaller_solutions
            if not under_attack(j + 1, solution)]


for answer in solve(BOARD_SIZE):
    print(answer)
