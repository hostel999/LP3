def n_queens_with_first_queen(n, fixed_col):
    col = set([fixed_col])
    posDiag = set([0 + fixed_col])  # r + c
    negDiag = set([0 - fixed_col])  # r - c

    res = []
    board = [["0"] * n for _ in range(n)]
    board[0][fixed_col] = "1"  # Place the first queen

    def backtrack(r):
        if r == n:
            copy = [" ".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "1"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "0"

    # Start placing queens from row 1 (since row 0 already has the fixed queen)
    backtrack(1)

    # Print all solutions with the fixed first queen
    for sol in res:
        for row in sol:
            print(row)
        print()

if __name__ == "__main__":
    # Example: Place first queen in column 3 of the 8x8 board
    n_queens_with_first_queen(5, 0)
