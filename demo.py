"""Demo for the refactored banking model."""

from typing import Callable

from models import Account, SavingsAccount, User


def attempt(label: str, action: Callable[[], object]) -> None:
    """Run an action; print OK or the rejection message."""
    try:
        action()
        print(f"OK: {label}")
    except (ValueError, TypeError) as error:
        print(f"Rejected: {label} -> {error}")


def show_account(account: Account) -> None:
    """Print an account summary and its transactions."""
    print(f"\n{account}")
    for record in account.get_transactions():
        print("  ", record)


def main() -> None:
    """Create a user with two accounts and show valid and invalid cases."""
    ali = User("U1", "Ali", "ali@example.com")
    current = Account("PK00112233", ali)
    savings = SavingsAccount("PK00445566", ali, interest_rate=0.05)

    print("=== Valid operations ===")
    attempt("Deposit 5000 into current", lambda: current.deposit(5000))
    attempt("Withdraw 1500 from current", lambda: current.withdraw(1500))
    attempt("Deposit 10000 into savings", lambda: savings.deposit(10000))
    attempt("Apply interest to savings", savings.apply_interest)

    print("\n=== Invalid operations ===")
    attempt("Deposit -100", lambda: current.deposit(-100))
    attempt("Withdraw 99999", lambda: current.withdraw(99999))
    attempt("User with blank name", lambda: User("U2", " ", "x@example.com"))
    attempt("Negative interest rate", lambda: SavingsAccount("PK99990000", ali, interest_rate=-0.1))

    print("\n=== Summary ===")
    show_account(current)
    show_account(savings)

    other = Account("PK00778899", ali)
    print("\nSeparate transaction lists (safe default factory):",
        other.transactions is not current.transactions)
    print("User repr (email hidden):", repr(ali))


if __name__ == "__main__":
    main()