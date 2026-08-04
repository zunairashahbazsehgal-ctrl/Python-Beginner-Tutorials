# Number Guessing Game

## Description

A simple command-line guessing game built in Python for beginners.
The computer picks a secret number between 1 and 10, and you get
5 attempts to guess it. After each guess you're told whether you
were too high or too low.

## Features

- Random secret number generated each time you play
- 5 attempts per game
- Hints after every guess (too high / too low)
- Handles text typed where a number was expected
- Reveals the answer if you run out of attempts

## Concepts Used

- Variables
- User input with `input()`
- Converting text to numbers with `int()`
- The `random` module (`random.randint()`)
- `if` / `elif` / `else`
- `for` loop with `range()`
- `for` / `else`
- `break` and `continue`
- Error handling with `try` / `except`
- f-strings

## How to Run

```bash
python guessing_game.py
```

## How It Works

`random.randint(1, 10)` picks the secret number before the loop
starts, so it stays the same for the whole game.

The `for` loop runs 5 times, once per attempt. If the guess is
correct, `break` ends the loop early.

The `else` attached to the `for` loop is a Python feature that
only runs if the loop finished **without** hitting a `break` —
in other words, only when the player used up all 5 attempts
without guessing right.

## What I Learned

- Generating random numbers with the `random` module
- Using a loop to limit the number of attempts
- Comparing values to give the player hints
- Catching errors with `try` / `except` so the program doesn't crash
- Ending a loop early with `break`
- Using `for` / `else` to detect when a loop ran out naturally

## Ideas for Later

- Let the player choose the difficulty (1–10, 1–50, 1–100)
- Ask "play again?" at the end instead of exiting
- Keep score across multiple rounds

## Author

**Zunaira Shahbaz**

Aspiring Data Scientist | Python Learner
