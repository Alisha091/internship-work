"""Demo for the banking model."""

from models import Account, User


def attempt(label, action):
    """Run an action; print OK or the rejection message."""
    try:
        action()
        print(f"OK: {label}")
    except (ValueError, TypeError) as error:
        print(f"Rejected: {label} -> {error}")


def show_history(account):
    """Print an account's balance and transactions."""
    print(f"\n{account}")
    for record in account.get_transactions():
        print("  ", record)


def main():
    """Create two users and accounts and show valid and invalid operations."""
    ali = User("U1", "Ali", "ali@example.com")
    sara = User("U2", "Sara", "sara@example.com")
    ali_account = Account("PK00112233", ali)
    sara_account = Account("PK00445566", sara)

    print("=== Valid operations ===")
    attempt("Ali deposits 5000", lambda: ali_account.deposit(5000))
    attempt("Ali withdraws 1500", lambda: ali_account.withdraw(1500))
    attempt("Sara deposits 2000", lambda: sara_account.deposit(2000))
    attempt("Ali transfers 500 to Sara", lambda: ali_account.transfer_to(sara_account, 500))

    print("\n=== Invalid operations ===")
    attempt("Deposit 0", lambda: ali_account.deposit(0))
    attempt("Deposit -100", lambda: ali_account.deposit(-100))
    attempt("Withdraw 10000 (more than balance)", lambda: ali_account.withdraw(10000))
    attempt("Deposit 'abc'", lambda: ali_account.deposit("abc"))
    attempt("Create user with blank name", lambda: User("U3", "  ", "x@example.com"))

    print("\n=== Balances and history ===")
    show_history(ali_account)
    show_history(sara_account)

    print("\nDirect access to private history:", hasattr(ali_account, "__transactions"))


if __name__ == "__main__":
    main()