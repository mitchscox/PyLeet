# BankAccountLibrary.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from BankAccounts import BankAccount

class BankAccountLibrary:
    def create_bank_account(self, account_number, initial_balance=0.0):
        """Creates a bank account with a given account number and initial balance."""
        self.account = BankAccount(account_number, initial_balance)

    def get_balance(self):
        """Returns the current balance of the account."""
        return self.account.get_balance()

    def deposit_amount(self, amount):
        """Deposits a given amount into the account."""
        self.account.deposit(amount)

    def withdraw_amount(self, amount):
        """Withdraws a given amount from the account."""
        self.account.withdraw(amount)

    def get_account_number(self):
        """Returns the account number of the account."""
        return self.account.get_account_number()
