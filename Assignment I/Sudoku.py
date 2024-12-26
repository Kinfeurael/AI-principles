def solve_sudoku(board):
    def is_valid(board, row, col, num):
        # Check the row
        for i in range(9):
            if board[row][i] == num:
                return False

        # Check the column
        for i in range(9):
            if board[i][col] == num:
                return False

        # Check the 3x3 sub-grid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:  # Find an empty cell
                    for num in range(1, 10):  # Try numbers 1 to 9
                        if is_valid(board, row, col, num):
                            board[row][col] = num  # Place the number

                            if solve():  # Recursively solve the rest
                                return True

                            board[row][col] = 0  # Backtrack if needed

                    return False  # No valid number found for this cell

        return True  # Solved successfully

    return solve()
