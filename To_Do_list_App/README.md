# To-Do List App

## Description

A simple command-line to-do list built in Python for beginners.
You can add tasks, view them, and save them to a text file.
The program keeps running until you choose to exit.

## Features

- Add as many tasks as you like
- View all your tasks at once
- Save your tasks to `tasks.txt`
- Tells you when the list is empty
- Rejects invalid menu choices

## Concepts Used

- Variables
- Strings and string concatenation (joining text with `+`)
- The newline character `\n`
- User input with `input()`
- `if` / `elif` / `else`
- `while` loop
- `break`
- Writing to a file with `open()`, `write()` and `close()`

## How to Run

```bash
python todo.py
```

A file called `tasks.txt` will be created in the same folder
when you choose "Save Tasks".

## How It Works

All the tasks are stored in one variable called `tasks`, which
starts out as an empty string `""`.

Every time you add a task, it gets joined onto the end:

```python
tasks = tasks + "- " + task + "\n"
```

The `\n` is a newline character. It doesn't show up as text —
it tells Python to start a new line at that point. So after
adding two tasks the variable holds:
Buy milk
Finish homework

That's why viewing the tasks only needs a single `print(tasks)`,
and saving only needs a single `file.write(tasks)`.

Opening the file with `"w"` means *write mode*, which replaces
whatever was in the file before. So saving twice doesn't create
duplicates — the newest version simply overwrites the old one.

## What I Learned

- Building up a string piece by piece as a program runs
- Using `\n` to put text on separate lines
- Keeping a menu running with a `while` loop
- Ending a loop with `break`
- Writing text to a file and closing it properly

## Ideas for Later

- Load saved tasks back in when the program starts
- Number the tasks (1, 2, 3...) as they're added
- Add a "delete a task" option
- Save automatically instead of needing menu option 3