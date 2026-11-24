"""Play tic-tac-toe in the terminal against the minimax AI."""

import argparse

from ai import best_move
from board import EMPTY, is_over, new_board, other, render, winner


def ask_move(board, input_fn=input):
    while True:
        raw = input_fn("Your move (1-9): ").strip()
        if raw.isdigit() and 1 <= int(raw) <= 9 and board[int(raw) - 1] == EMPTY:
            return int(raw) - 1
        print("Invalid move, pick an empty cell number from 1 to 9.")


def play(human="X", input_fn=input, output_fn=print):
    """Run one game and return the winner ('X', 'O') or None for a draw."""
    board = new_board()
    ai = other(human)
    turn = "X"
    while not is_over(board):
        if turn == human:
            output_fn("\n" + render(board) + "\n")
            board[ask_move(board, input_fn)] = human
        else:
            move = best_move(board, ai)
            board[move] = ai
            output_fn(f"AI plays {move + 1}")
        turn = other(turn)

    output_fn("\n" + render(board) + "\n")
    result = winner(board)
    if result is None:
        output_fn("It's a draw!")
    elif result == human:
        output_fn("You win! (that shouldn't happen...)")
    else:
        output_fn("The AI wins!")
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description="Play tic-tac-toe against an unbeatable AI.")
    parser.add_argument("--play-as", choices=["X", "O"], default="X",
                        help="X moves first (default: X)")
    args = parser.parse_args(argv)
    try:
        play(human=args.play_as)
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
