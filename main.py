"""Command-line menu for the expense tracker."""

import tracker


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


def main():
    """Run the menu loop until the user chooses Exit."""
    expenses = []
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break
        elif choice == "1":
            expenses = add_expense_flow(expenses)
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