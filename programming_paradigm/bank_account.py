# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the amount to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw amount if funds are sufficient.
        Return True if successful, otherwise False.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.account_balance}")
