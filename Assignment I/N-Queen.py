def solve_n_queens(n):
    def backtrack(row, diagonals, anti_diagonals, columns, current_board):
        # Base case: if we've placed queens on all rows
        if row == n:
            result.append([col for col in current_board])
            return

        for col in range(n):
            curr_diag = row - col
            curr_anti_diag = row + col

            # Check if the current position is under attack
            if (col in columns or
                curr_diag in diagonals or
                curr_anti_diag in anti_diagonals):
                continue

            # Place the queen
            columns.add(col)
            diagonals.add(curr_diag)
            anti_diagonals.add(curr_anti_diag)
            current_board.append(col)

            # Move to the next row
            backtrack(row + 1, diagonals, anti_diagonals, columns, current_board)

            # Backtrack: remove the queen
            columns.remove(col)
            diagonals.remove(curr_diag)
            anti_diagonals.remove(curr_anti_diag)
            current_board.pop()

    result = []
    backtrack(0, set(), set(), set(), [])
    return result