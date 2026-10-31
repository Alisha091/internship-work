CATEGORIES = ("Food", "Transport", "Bills", "Others")
expenses = []

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Summary")
    print("4. Show used categories")
    print("5. Exit")

    choice = input("Choose an option (1-5): ").strip()

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please select a number from 1 to 5.")
        continue
    if choice == "1":
        description = input("Description: ").strip()
        if description == "":
            print("Description cannot be empty.")
            continue

        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Amount must be a number.")
            continue
        if amount <= 0:
            print("Amount must be positive.")
            continue

        print("Categories:", ", ".join(CATEGORIES))
        category = input("Category: ").strip().title()
        if category not in CATEGORIES:
            print("Invalid category.")
            continue

        expense = {"description": description, "amount": amount, "category": category}
        expenses.append(expense)
        print("Expense added!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet.")
            continue
        for number, expense in enumerate(expenses, start=1):
            print(f"{number}. {expense['description']} - {expense['amount']:.2f} ({expense['category']})")

    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses yet.")
            continue
        total = 0
        category_totals = {}
        for expense in expenses:
            total += expense["amount"]
            name = expense["category"]
            category_totals[name] = category_totals.get(name, 0) + expense["amount"]
        print(f"Total: {total:.2f}")
        for name, amount_sum in category_totals.items():
            print(f"  {name}: {amount_sum:.2f}")

    elif choice == "4":
        used_categories = set()
        for expense in expenses:
            used_categories.add(expense["category"])
        print("Used categories:", sorted(used_categories))
        