import unittest
from contextlib import redirect_stdout
from io import StringIO

from board import new_board
from game import ask_move, play


def scripted(*answers):
    """Return an input function that replies with `answers` in order."""
    feed = iter(answers)
    return lambda prompt: next(feed)


class AskMoveTest(unittest.TestCase):

    def test_converts_cell_number_to_index(self):
        self.assertEqual(ask_move(new_board(), scripted("5")), 4)

    def test_reprompts_until_valid_empty_cell(self):
        board = new_board()
        board[0] = "X"
        out = StringIO()
        with redirect_stdout(out):
            move = ask_move(board, scripted("", "abc", "0", "10", "1", " 2 "))
        self.assertEqual(move, 1)
        self.assertEqual(out.getvalue().count("Invalid move"), 5)

    def test_rejects_digit_like_characters_int_cannot_parse(self):
        out = StringIO()
        with redirect_stdout(out):
            self.assertEqual(ask_move(new_board(), scripted("²", "3")), 2)
        self.assertIn("Invalid move", out.getvalue())


class PlayTest(unittest.TestCase):
    """The human always picks the lowest-numbered cell; occupied cells are re-prompted."""

    def play_lowest_free_cell(self, human):
        output = []
        with redirect_stdout(StringIO()):
            result = play(human=human, input_fn=scripted(*"123456789"), output_fn=output.append)
        return result, output

    def test_ai_wins_against_bad_play(self):
        result, output = self.play_lowest_free_cell("X")
        self.assertEqual(result, "O")
        self.assertIn("The AI wins!", output)

    def test_ai_moves_first_when_human_plays_o(self):
        result, output = self.play_lowest_free_cell("O")
        self.assertTrue(output[0].startswith("AI plays"))
        self.assertNotEqual(result, "O")


if __name__ == "__main__":
    unittest.main()
