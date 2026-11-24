"""Tic-tac-toe board helpers. A board is a list of 9 cells: 'X', 'O' or ' '."""

EMPTY = " "
LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


def new_board():
    return [EMPTY] * 9


def available_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]


def winner(board):
    """Return 'X' or 'O' if someone has three in a row, else None."""
    for a, b, c in LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def is_full(board):
    return EMPTY not in board


def is_over(board):
    return winner(board) is not None or is_full(board)


def other(player):
    return "O" if player == "X" else "X"


def render(board):
    """Return the board as text, showing cell numbers 1-9 for empty cells."""
    cells = [cell if cell != EMPTY else str(i + 1) for i, cell in enumerate(board)]
    rows = [" | ".join(cells[r:r + 3]) for r in (0, 3, 6)]
    return "\n---------\n".join(rows)
