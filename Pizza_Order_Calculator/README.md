# Pizza Order Calculator

## Description

A simple command-line ordering program built in Python for beginners.
It shows a pizza menu, asks which size you want and how many, then
prints a receipt with the total bill.

## Features

- Menu with three pizza sizes and prices
- Calculates the total from price × quantity
- Rejects invalid menu choices
- Prints a formatted receipt

## Concepts Used

- Variables
- Functions with `def`
- Function parameters and `return`
- User input with `input()`
- Converting text to numbers with `int()`
- `if` / `elif` / `else`
- Arithmetic operators
- Escape characters (`\n`)

## How to Run

```bash
python pizza.py
```

## How It Works

The program is split into three functions, each with one job:

- `show_menu()` prints the menu
- `get_price()` takes a menu choice and returns the matching price,
  or 0 if the choice isn't valid
- `main()` runs the program and ties the other two together

Because `get_price()` returns 0 for anything unrecognised, `main()`
can check for 0 to decide whether to print a receipt or an error.

## What I Learned

- Writing functions to split a program into smaller pieces
- Passing values into a function and getting a value back with `return`
- Using a return value as a signal (0 means "invalid choice")
- Doing calculations with user input
- Formatting output to look like a receipt

## Ideas for Later

- Add `try` / `except` so typing text for the quantity doesn't crash
- Loop back to the menu instead of exiting after one order
- Let the customer order more than one size in a single receipt
- Add toppings with extra charges
- Apply a discount for large orders