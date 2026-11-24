# AI Tic-Tac-Toe (Minimax)

Play tic-tac-toe in the terminal against an **unbeatable AI** that uses the
minimax algorithm with alpha-beta pruning. Uses only the Python standard library.

## Features

- Minimax search with alpha-beta pruning
- Prefers faster wins and slower losses (depth-aware scoring)
- Play as X (go first) or O (AI goes first)
- Simple numbered-board input (1-9)

## Usage

```bash
# You play X and move first
python3 game.py

# Let the AI move first
python3 game.py --play-as O
```

Cells are numbered like a phone keypad:

```
1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9
```

## How the AI works

`ai.py` explores every possible continuation of the game with **minimax**: the AI
picks the move that maximizes its score assuming the opponent always picks the move
that minimizes it. A win scores `10 - depth` and a loss `depth - 10`, so the AI wins
as fast as possible and delays losses. **Alpha-beta pruning** skips branches that
cannot change the result, which keeps the search fast.

## Tests

```bash
python3 -m unittest test_ai.py
```

The test suite plays every possible opponent strategy against the AI and checks
that it never loses.
