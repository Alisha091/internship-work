"""Expense logic: validation and calculations. No input() or print() here."""

CATEGORIES = ("Food", "Transport", "Bills", "Others")


def is_valid_description(description):
    """Return True if the description is not blank."""
    return description.strip() != ""


def parse_amount(text):
    """Convert text to a positive float. Return None if invalid."""
    try:
        amount = float(text)
    except ValueError:
        return None
    if amount <= 0:
        return None
    return amount


def normalize_category(text):
    """Return the matching category (e.g. 'food' -> 'Food'), or None if invalid."""
    category = text.strip().title()
    if category in CATEGORIES:
        return category
    return None


def create_expense(description, amount, category):
    """Return an expense dictionary."""
    return {"description": description.strip(), "amount": amount, "category": category}


def add_expense(expenses, expense):
    """Return a new list containing the old expenses plus the new one."""
    return expenses + [expense]


def calculate_total(expenses):
    """Return the sum of all expense amounts."""
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total


def calculate_category_totals(expenses):
    """Return a dictionary of {category: total amount}."""
    totals = {}
    for expense in expenses:
        name = expense["category"]
        totals[name] = totals.get(name, 0) + expense["amount"]
    return totals


def get_used_categories(expenses):
    """Return a sorted list of unique categories that have been used."""
    used = set()
    for expense in expenses:
        used.add(expense["category"])
    return sorted(used)