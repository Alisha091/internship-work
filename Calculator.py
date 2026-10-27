def get_number(prompt):
    while True:
        text = input(prompt)
        try:
            return float(text)
        except ValueError:
            print("Invalid number. Please enter a numeric value.")


while True:
    print("\n===== Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor division (//)")
    print("6. Remainder (%)")
    print("7. Exponent (**)")
    print("8. Exit")

    choice = input("Choose an option (1-8): ").strip()

    if choice == "8":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice. Please select a number from 1 to 8.")
        continue

    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")

    if choice == "1":
        print(f"Result: {a} + {b} = {a + b}")
    elif choice == "2":
        print(f"Result: {a} - {b} = {a - b}")
    elif choice == "3":
        print(f"Result: {a} * {b} = {a * b}")
    elif choice in ["4", "5", "6"] and b == 0:
        print("Error: Cannot divide by zero.")
    elif choice == "4":
        print(f"Result: {a} / {b} = {a / b}")
    elif choice == "5":
        print(f"Result: {a} // {b} = {a // b}")
    elif choice == "6":
        print(f"Result: {a} % {b} = {a % b}")
    elif choice == "7":
        print(f"Result: {a} ** {b} = {a ** b}")