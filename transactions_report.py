"""Transaction report using comprehensions and built-ins."""

REQUIRED_FIELDS = {"id", "category", "description", "amount", "payment_method"}
HIGH_VALUE_THRESHOLD = 4000
BUDGETS = {"Bills": 5000, "Entertainment": 1500, "Food": 4000,
           "Shopping": 5000, "Transport": 2500}

TRANSACTIONS = [
    {"id": 1, "category": "Food", "description": "  lunch at cafe ", "amount": 850.0, "payment_method": "Card"},
    {"id": 2, "category": "Transport", "description": "Bus fare", "amount": 100.0, "payment_method": "Cash"},
    {"id": 3, "category": "Bills", "description": "Electricity bill", "amount": 3000.0, "payment_method": "Bank Transfer"},
    {"id": 4, "category": "Food", "description": "Pizza night", "amount": 500.0, "payment_method": "Card"},
    {"id": 5, "category": "Shopping", "description": "T-shirt", "amount": 1200.0, "payment_method": "Card"},
    {"id": 6, "category": "Transport", "description": "Taxi ride", "amount": 450.0, "payment_method": "Cash"},
    {"id": 7, "category": "Bills", "description": "Internet bill", "amount": 2000.0, "payment_method": "Bank Transfer"},
    {"id": 8, "category": "Food", "description": "Groceries", "amount": 2200.0, "payment_method": "Cash"},
    {"id": 9, "category": "Entertainment", "description": "Movie ticket", "amount": 700.0, "payment_method": "Card"},
    {"id": 10, "category": "Shopping", "description": "Headphones", "amount": 4500.0, "payment_method": "Card"},
    {"id": 11, "category": "Transport", "description": "Fuel", "amount": 1500.0, "payment_method": "Cash"},
    {"id": 12, "category": "Entertainment", "description": "Streaming subscription", "amount": 600.0, "payment_method": "Card"},
]


def has_required_fields(transactions):
    """Return True if every record has all required fields (uses all())."""
    return all(REQUIRED_FIELDS <= t.keys() for t in transactions)


def has_positive_amounts(transactions):
    """Return True if every amount is a positive number (uses all())."""
    return all(isinstance(t["amount"], (int, float)) and t["amount"] > 0
               for t in transactions)


def has_high_value(transactions, threshold):
    """Return True if any transaction exceeds the threshold (uses any())."""
    return any(t["amount"] > threshold for t in transactions)


def filter_by_category(transactions, category):
    """Return a list of transactions in one category (list comprehension)."""
    return [t for t in transactions if t["category"] == category]


def unique_categories(transactions):
    """Return a set of unique categories (set comprehension)."""
    return {t["category"] for t in transactions}


def totals_by_category(transactions):
    """Return {category: total amount} (dict comprehension)."""
    return {c: sum(t["amount"] for t in transactions if t["category"] == c)
            for c in unique_categories(transactions)}


def clean_descriptions(transactions):
    """Return trimmed, title-case descriptions (list comprehension)."""
    return [t["description"].strip().title() for t in transactions]


def sort_by_amount(transactions):
    """Return a new list sorted by amount, highest first."""
    return sorted(transactions, key=lambda t: t["amount"], reverse=True)


def sort_by_description(transactions):
    """Return a new list sorted A-Z by description."""
    return sorted(transactions, key=lambda t: t["description"].strip().lower())


def compare_budgets(transactions):
    """Return rows (category, budget, spent, status) using zip()."""
    totals = totals_by_category(transactions)
    categories = sorted(totals)
    budgets = [BUDGETS[c] for c in categories]
    return [(c, b, totals[c], "OVER" if totals[c] > b else "OK")
            for c, b in zip(categories, budgets)]


def run_assertions():
    """Plain assert checks for key transformations."""
    totals = totals_by_category(TRANSACTIONS)
    assert totals["Food"] == 3550.0
    assert totals["Shopping"] == 5700.0
    assert sum(totals.values()) == 17600.0
    assert len(filter_by_category(TRANSACTIONS, "Food")) == 3
    assert unique_categories(TRANSACTIONS) == {"Food", "Transport", "Bills", "Shopping", "Entertainment"}
    assert sort_by_amount(TRANSACTIONS)[0]["id"] == 10
    assert sort_by_description(TRANSACTIONS)[0]["id"] == 2
    assert TRANSACTIONS[0]["id"] == 1  # original order preserved
    assert clean_descriptions(TRANSACTIONS)[0] == "Lunch At Cafe"
    assert has_required_fields(TRANSACTIONS) and has_positive_amounts(TRANSACTIONS)
    assert not has_positive_amounts([{"amount": -5}])
    print("All assertions passed.")


def main():
    """Print the full report."""
    print("=== Validation ===")
    print("All records have required fields:", has_required_fields(TRANSACTIONS))
    print("All amounts positive:", has_positive_amounts(TRANSACTIONS))
    print(f"Any amount above {HIGH_VALUE_THRESHOLD}:",
          has_high_value(TRANSACTIONS, HIGH_VALUE_THRESHOLD))

    print("\n=== Filtered: Food ===")
    for t in filter_by_category(TRANSACTIONS, "Food"):
        print(f"#{t['id']} {t['description'].strip()} - {t['amount']:.2f}")

    print("\n=== Unique categories ===")
    print(sorted(unique_categories(TRANSACTIONS)))

    print("\n=== Totals by category ===")
    for name, total in sorted(totals_by_category(TRANSACTIONS).items()):
        print(f"{name}: {total:.2f}")

    print("\n=== Cleaned descriptions ===")
    print(clean_descriptions(TRANSACTIONS))

    print("\n=== Sorted by description (A-Z) ===")
    for t in sort_by_description(TRANSACTIONS):
        print(f"{t['description'].strip()} - {t['amount']:.2f}")

    print("\n=== Ranking by amount ===")
    for rank, t in enumerate(sort_by_amount(TRANSACTIONS), start=1):
        print(f"{rank}. {t['description'].strip()} - {t['amount']:.2f}")

    print("\n=== Budget comparison ===")
    for category, budget, spent, status in compare_budgets(TRANSACTIONS):
        print(f"{category}: budget {budget:.2f}, spent {spent:.2f} -> {status}")

    print("\n=== Assertions ===")
    run_assertions()


if __name__ == "__main__":
    main()