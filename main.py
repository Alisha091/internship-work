"""Command-line menu for the expense tracker with JSON persistence."""

import storage
import tracker

DATA_FILE = "expenses.json"


def show_menu():
    """Print the main menu."""
    print("\n===== Expense Tracker =====")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Summary")
    print("4. Show used categories")
    print("5. Exit")


def add_expense_flow(expenses):
    """Ask the user for an expense and return the updated list."""
    description = input("Description: ")
    if not tracker.is_valid_description(description):
        print("Description cannot be empty.")
        return expenses

    amount = tracker.parse_amount(input("Amount: "))
    if amount is None:
        print("Amount must be a positive number.")
        return expenses

    print("Categories:", ", ".join(tracker.CATEGORIES))
    category = tracker.normalize_category(input("Category: "))
    if category is None:
        print("Invalid category.")
        return expenses

    expense = tracker.create_expense(description, amount, category)
    print("Expense added!")
    return tracker.add_expense(expenses, expense)


def list_expenses(expenses):
    """Print all expenses as a numbered list."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    for number, expense in enumerate(expenses, start=1):
        print(f"{number}. {expense['description']} - {expense['amount']:.2f} ({expense['category']})")


def show_summary(expenses):
    """Print the overall total and the total per category."""
    if len(expenses) == 0:
        print("No expenses yet.")
        return
    print(f"Total: {tracker.calculate_total(expenses):.2f}")
    for name, amount in tracker.calculate_category_totals(expenses).items():
        print(f"  {name}: {amount:.2f}")


def save_and_report(expenses):
    """Save expenses to the data file and print a message if it fails."""
    error = storage.save_expenses(DATA_FILE, expenses)
    if error:
        print("Warning:", error)
    else:
        print(f"Saved to {DATA_FILE}.")


def main():
    """Load saved expenses, then run the menu loop until Exit."""
    expenses, error = storage.load_expenses(DATA_FILE)
    if error:
        print("Warning:", error)
    else:
        print(f"Loaded {len(expenses)} expense(s) from {DATA_FILE}.")

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice == "1":
            updated = add_expense_flow(expenses)
            if len(updated) != len(expenses):
                expenses = updated
                save_and_report(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            show_summary(expenses)
        elif choice == "4":
            print("Used categories:", tracker.get_used_categories(expenses))
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()