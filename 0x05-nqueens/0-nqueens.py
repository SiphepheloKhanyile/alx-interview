#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem.
"""
import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed at board[row][col].
    This function checks if a queen can be placed at board[row][col]
    without being attacked by another queen.
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, solutions):
    """
    Solve N Queens problem using Backtracking.
    """
    N = len(board)

    # Base case: If all queens are placed, then print the solution
    if col >= N:
        solutions.append([list(map(list, zip(*board)))[i].index(1)
                         for i in range(N)])
        return True

    # Consider this column and try placing queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_n_queens(board, col + 1, solutions)

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0

    return False


def n_queens(N):
    """
    Main function to solve N Queens problem.
    """
    # Initialize the board with zeros
    board = [[0]*N for _ in range(N)]
    solutions = []

    # Start solving from the first column
    solve_n_queens(board, 0, solutions)

    # Print all found solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    n_queens(N)
