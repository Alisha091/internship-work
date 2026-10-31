# Intern Profile CLI

## Setup

python -m venv .venv

## Activate (windows)

.venv\Scripts\activate

## Run

python intern_profile.py

## Day 2: Calculator

### Run

python Calculator.py

### Features

- Addition, subtraction, multiplication, division
- Floor division, remainder, exponentiation
- Rejects invalid menu choices and non-numeric input
- Prevents division by zero
- Menu repeats until Exit (8) is chosen

### Day 3: Expense Tracker

### Run

python expense_tracker.py

### Features

- Add expenses (description,amount, category)
- list expenses with numbers
- Summary overall total and total category
- show used categories
- Rejects blank categories and invalid choices

## Day 4: Modular Expense Tracker

### Run

python main.py

### Structure

- tracker.py: expense logic (validation, totals, categories), no input/print
- main.py: menu and user interaction
