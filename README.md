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

## Day 5: JSON Persistence

### Run

python main.py

### Data file

Expenses are stored in expenses.json as a list of records:
[{"description": "Lunch", "amount": 850.0, "category": "Food"}]

- A missing file starts an empty tracker
- Malformed JSON or permission errors show a clear warning
- Files: storage.py (load/save), tracker.py (logic), main.py (menu)

## Day 6: Comprehensions and Built-ins

### Run

python transactions_report.py

### Where things are used

- all(): has_required_fields, has_positive_amounts
- any(): has_high_value (configurable HIGH_VALUE_THRESHOLD)
- List comprehension: filter_by_category, clean_descriptions
- Set comprehension: unique_categories
- Dict comprehension: totals_by_category
- sorted() with key and reverse: sort_by_amount, sort_by_description (original list unchanged)
- enumerate(): numbered ranking in main()
- zip(): compare_budgets (category names with budgets)
- assert checks: run_assertions
