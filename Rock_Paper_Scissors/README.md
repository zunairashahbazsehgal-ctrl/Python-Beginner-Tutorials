# Rock Paper Scissors

## Description

A simple command-line game built in Python for beginners.
You pick Rock, Paper or Scissors, the computer picks one at
random, and the program announces the winner.

## Features

- Random computer choice each time you play
- Accepts input in any capitalisation (`rock`, `ROCK`, `Rock`)
- Detects ties
- Rejects choices that aren't one of the three options

## Concepts Used

- Functions with `def`
- Function parameters and `return`
- User input with `input()`
- String methods (`.capitalize()`)
- Lists
- The `random` module (`random.choice()`)
- `if` / `elif` / `else`
- Nested `if` statements

## How to Run

```bash
python rps.py
```

## How It Works

The program is split into four functions, each with one job:

- `welcome()` prints the title
- `player_choice()` asks the player and tidies up their input
- `computer_choice()` picks randomly from a list
- `winner(player, computer)` compares the two and prints the result

`random.choice()` picks one item at random from a list, which is
different from `random.randint()` — that one picks a number from
a range.

`.capitalize()` makes the first letter uppercase and the rest
lowercase, so whatever the player types is turned into the same
format the computer uses. Without it, `rock` would never match
`Rock`.

Inside `winner()`, the tie is checked first. After that, each
branch only needs to ask one question: if the player chose Rock,
the only way to win is if the computer chose Scissors — anything
else means the computer won.

## What I Learned

- Splitting a program into small functions with one job each
- Returning a value from a function and using it later
- Picking a random item from a list with `random.choice()`
- Cleaning up user input so comparisons work reliably
- Using nested `if` statements to check two things in order

## Ideas for Later

- Loop so you can play multiple rounds
- Keep score across rounds
- Play best of 3 or best of 5
- Return the result from `winner()` instead of printing it,
  so the score can be counted