"""Minimax with alpha-beta pruning for tic-tac-toe."""

import math

from board import EMPTY, available_moves, is_full, other, winner

WIN_SCORE = 10


def minimax(board, player, ai, depth=0, alpha=-math.inf, beta=math.inf):
    """Score the position from the AI's point of view with `player` to move."""
    won = winner(board)
    if won == ai:
        return WIN_SCORE - depth
    if won is not None:
        return depth - WIN_SCORE
    if is_full(board):
        return 0

    maximizing = player == ai
    best = -math.inf if maximizing else math.inf
    for move in available_moves(board):
        board[move] = player
        score = minimax(board, other(player), ai, depth + 1, alpha, beta)
        board[move] = EMPTY
        if maximizing:
            best = max(best, score)
            alpha = max(alpha, score)
        else:
            best = min(best, score)
            beta = min(beta, score)
        if beta <= alpha:
            break
    return best


def best_move(board, ai):
    """Return the index (0-8) of the best move for `ai` on `board`."""
    moves = available_moves(board)
    if not moves:
        raise ValueError("no moves available")
    best_score, choice = -math.inf, moves[0]
    for move in moves:
        board[move] = ai
        score = minimax(board, other(ai), ai, depth=1)
        board[move] = EMPTY
        if score > best_score:
            best_score, choice = score, move
    return choice
