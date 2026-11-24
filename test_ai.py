import unittest

from ai import best_move
from board import available_moves, is_over, new_board, other, render, winner


def board_from(text):
    return [" " if c == "." else c for c in text]


class BoardTest(unittest.TestCase):

    def test_winner_row(self):
        self.assertEqual(winner(board_from("XXX......")), "X")

    def test_winner_diagonal(self):
        self.assertEqual(winner(board_from("O...O...O")), "O")

    def test_no_winner(self):
        self.assertIsNone(winner(board_from("XOX......")))

    def test_render_shows_numbers_for_empty_cells(self):
        self.assertIn("5", render(new_board()))


class BestMoveTest(unittest.TestCase):

    def test_takes_winning_move(self):
        board = board_from("OO.XX....")
        self.assertEqual(best_move(board, "O"), 2)

    def test_blocks_opponent_win(self):
        board = board_from("XX..O....")
        self.assertEqual(best_move(board, "O"), 2)

    def test_does_not_mutate_board(self):
        board = board_from("X........")
        best_move(board, "O")
        self.assertEqual(board, board_from("X........"))

    def test_raises_on_full_board(self):
        with self.assertRaises(ValueError):
            best_move(board_from("XOXXOOOXX"), "X")


class UnbeatableTest(unittest.TestCase):
    """Play every possible sequence of opponent moves; the AI must never lose."""

    def explore(self, board, turn, ai):
        if is_over(board):
            self.assertNotEqual(winner(board), other(ai), render(board))
            return
        if turn == ai:
            board[best_move(board, ai)] = ai
            self.explore(board, other(turn), ai)
            return
        for move in available_moves(board):
            child = board.copy()
            child[move] = turn
            self.explore(child, other(turn), ai)

    def test_ai_never_loses_as_o(self):
        self.explore(new_board(), "X", ai="O")

    def test_ai_never_loses_as_x(self):
        self.explore(new_board(), "X", ai="X")


if __name__ == "__main__":
    unittest.main()
