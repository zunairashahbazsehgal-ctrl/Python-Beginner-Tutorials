# ATM Simulator

## Description

A simple command-line ATM simulation built in Python for beginners.
The program allows users to enter a starting balance, check their
balance, deposit money, withdraw money, and exit the application.

## Features

- Set an initial account balance
- Check the current balance
- Deposit money into the account
- Withdraw money from the account
- Prevent withdrawals greater than the available balance
- Prevent negative deposits and withdrawals
- Handle invalid numeric input
- Run continuously until the user chooses to exit

## Concepts Used

- Variables
- User input with `input()`
- Converting text to numbers with `int()`
- `while` loops
- `if` / `elif` / `else`
- Comparison operators
- Arithmetic operators
- `try` / `except` for error handling
- `break`
- f-strings

## How to Run

```bash
python atm_simulator.py
```

## How It Works

The program first asks the user to enter a starting balance.
The balance is stored in the `balance` variable and can be changed
through deposits and withdrawals.

A `while` loop continuously displays the ATM menu until the user
chooses option `4` to exit.

When depositing money, the amount is added to the current balance.

When withdrawing money, the program first checks that the amount is
positive and that there is enough money in the account. If both
conditions are satisfied, the amount is subtracted from the balance.

The program also uses `try` / `except` to prevent invalid numeric
input from crashing the application.

## What I Learned

- Using a `while` loop to create a menu-driven application
- Updating a variable as the program runs
- Using conditions to control deposits and withdrawals
- Checking whether enough balance is available
- Handling invalid user input with `try` / `except`
- Using `break` to exit a loop
- Building a simple real-world simulation with Python

## Ideas for Later

- Add PIN authentication
- Add transaction history
- Allow multiple accounts
- Add a transfer money option
- Add a maximum withdrawal limit
- Store account information in a file

## Author

**Zunaira Shahbaz**

Aspiring Data Scientist | Python Learner