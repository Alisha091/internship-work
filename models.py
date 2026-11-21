"""Banking model refactored with data classes, type hints and composition."""

from dataclasses import dataclass, field
from itertools import count
from typing import List

_transaction_ids = count(1)
VALID_TYPES = ("deposit", "withdrawal")


def validate_amount(amount: float) -> None:
    """Raise ValueError unless amount is a positive number."""
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number.")
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")


@dataclass
class User:
    """A bank customer (data class: __init__ and __repr__ are generated)."""

    user_id: str
    name: str
    email: str = field(repr=False)

    def __post_init__(self) -> None:
        self.user_id = str(self.user_id).strip()
        self.name = self.name.strip()
        self.email = self.email.strip()
        if not (self.user_id and self.name and self.email):
            raise ValueError("User ID, name and email cannot be empty.")


@dataclass(frozen=True)
class Transaction:
    """One deposit or withdrawal record (immutable data class)."""

    transaction_type: str
    amount: float
    description: str = ""
    transaction_id: int = field(default_factory=lambda: next(_transaction_ids))

    def __post_init__(self) -> None:
        if self.transaction_type not in VALID_TYPES:
            raise ValueError("Transaction type must be 'deposit' or 'withdrawal'.")
        validate_amount(self.amount)

    def __str__(self) -> str:
        return (f"#{self.transaction_id} {self.transaction_type} "
                f"{self.amount:.2f} - {self.description}")


@dataclass
class Account:
    """An account that HAS-A owner and HAS-MANY transactions (composition)."""

    account_number: str = field(repr=False)
    owner: User
    transactions: List[Transaction] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.account_number = str(self.account_number).strip()
        if not self.account_number:
            raise ValueError("Account number cannot be empty.")
        if not isinstance(self.owner, User):
            raise TypeError("Account owner must be a User.")

    def masked_number(self) -> str:
        """Return the account number with only the last 4 characters visible."""
        return "****" + self.account_number[-4:]

    def calculate_balance(self) -> float:
        """Return the balance calculated from all transactions."""
        return sum(t.amount if t.transaction_type == "deposit" else -t.amount
                for t in self.transactions)

    def add_transaction(self, transaction: Transaction) -> Transaction:
        """Store a valid transaction; reject withdrawals above the balance."""
        if (transaction.transaction_type == "withdrawal"
                and transaction.amount > self.calculate_balance()):
            raise ValueError("Insufficient funds.")
        self.transactions.append(transaction)
        return transaction

    def deposit(self, amount: float, description: str = "Deposit") -> Transaction:
        """Create and store a deposit."""
        return self.add_transaction(Transaction("deposit", amount, description))

    def withdraw(self, amount: float, description: str = "Withdrawal") -> Transaction:
        """Create and store a withdrawal."""
        return self.add_transaction(Transaction("withdrawal", amount, description))

    def get_transactions(self) -> List[Transaction]:
        """Return a copy of the transaction history."""
        return list(self.transactions)

    def __str__(self) -> str:
        return (f"Account {self.masked_number()} ({self.owner.name}) - "
                f"Balance: {self.calculate_balance():.2f}")


@dataclass
class SavingsAccount(Account):
    """A SavingsAccount IS-A Account that also earns interest.

    Inheritance is justified: it needs everything an Account does
    (deposit, withdraw, history) plus an interest rate and extra behavior.
    """

    interest_rate: float = 0.02

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

    def apply_interest(self) -> Transaction:
        """Deposit interest based on the current balance."""
        interest = round(self.calculate_balance() * self.interest_rate, 2)
        return self.deposit(interest, f"Interest at {self.interest_rate:.1%}")

    def __str__(self) -> str:
        return super().__str__() + f" [Savings, rate {self.interest_rate:.1%}]"