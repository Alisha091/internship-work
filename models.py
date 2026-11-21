"""Banking model: User, Transaction and Account classes."""

import itertools

_transaction_ids = itertools.count(1)


class User:
    """A bank customer with an ID, a name and an email."""

    def __init__(self, user_id, name, email):
        if not str(user_id).strip() or not name.strip() or not email.strip():
            raise ValueError("User ID, name and email cannot be empty.")
        self.user_id = str(user_id).strip()
        self.name = name.strip()
        self.email = email.strip()

    def __str__(self):
        return f"{self.name} (ID: {self.user_id})"

    def __repr__(self):
        return f"User(user_id={self.user_id!r}, name={self.name!r})"


class Transaction:
    """One deposit or withdrawal record."""

    VALID_TYPES = ("deposit", "withdrawal")

    def __init__(self, transaction_type, amount, description=""):
        if transaction_type not in self.VALID_TYPES:
            raise ValueError("Transaction type must be 'deposit' or 'withdrawal'.")
        if amount <= 0:
            raise ValueError("Transaction amount must be positive.")
        self.transaction_id = next(_transaction_ids)
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description

    def __str__(self):
        return (f"#{self.transaction_id} {self.transaction_type} "
                f"{self.amount:.2f} - {self.description}")

    def __repr__(self):
        return (f"Transaction(id={self.transaction_id}, "
                f"type={self.transaction_type!r}, amount={self.amount})")


class Account:
    """A bank account linked to one user.

    The balance is protected (_balance) and the history is private
    (__transactions), so they change only through the methods below.
    """

    def __init__(self, account_number, owner):
        if not str(account_number).strip():
            raise ValueError("Account number cannot be empty.")
        if not isinstance(owner, User):
            raise TypeError("Account owner must be a User.")
        self.account_number = str(account_number).strip()
        self.owner = owner
        self._balance = 0
        self.__transactions = []

    @staticmethod
    def _validate_amount(amount):
        """Raise ValueError unless amount is a positive number."""
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

    def _masked_number(self):
        """Return the account number with only the last 4 characters visible."""
        return "****" + self.account_number[-4:]

    def deposit(self, amount, description="Deposit"):
        """Add money to the account and record a Transaction."""
        self._validate_amount(amount)
        self._balance += amount
        record = Transaction("deposit", amount, description)
        self.__transactions.append(record)
        return record

    def withdraw(self, amount, description="Withdrawal"):
        """Remove money from the account and record a Transaction."""
        self._validate_amount(amount)
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        record = Transaction("withdrawal", amount, description)
        self.__transactions.append(record)
        return record

    def get_balance(self):
        """Return the current balance."""
        return self._balance

    def get_transactions(self):
        """Return a copy of the transaction history."""
        return list(self.__transactions)

    def transfer_to(self, other, amount):
        """Bonus: move money to another account safely."""
        if not isinstance(other, Account) or other is self:
            raise ValueError("Transfer needs a different, valid account.")
        self.withdraw(amount, f"Transfer to {other._masked_number()}")
        other.deposit(amount, f"Transfer from {self._masked_number()}")

    def __str__(self):
        return f"Account {self._masked_number()} ({self.owner.name}) - Balance: {self._balance:.2f}"

    def __repr__(self):
        return f"Account(number={self._masked_number()!r}, owner={self.owner.name!r})"