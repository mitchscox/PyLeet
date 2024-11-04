# test_bank_account.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from BankAccounts import BankAccount

def test_initial_balance():
    account = BankAccount("123456789", 1000.0)
    assert account.get_balance() == 1000.0, "Initial balance should be 1000.0"

def test_deposit_positive_amount():
    account = BankAccount("123456789", 1000.0)
    account.deposit(500)
    assert account.get_balance() == 1500.0, "Balance should be 1500.0 after deposit of 500"

def test_deposit_negative_amount():
    account = BankAccount("123456789", 1000.0)
    account.deposit(-100)
    assert account.get_balance() == 1000.0, "Balance should remain 1000.0 after attempting to deposit negative amount"

def test_withdraw_valid_amount():
    account = BankAccount("123456789", 1000.0)
    account.withdraw(200)
    assert account.get_balance() == 800.0, "Balance should be 800.0 after withdrawing 200"

def test_withdraw_insufficient_funds():
    account = BankAccount("123456789", 100.0)
    account.withdraw(200)
    assert account.get_balance() == 100.0, "Balance should remain 100.0 after attempting to withdraw more than available"

def test_get_account_number():
    account = BankAccount("123456789", 1000.0)
    assert account.get_account_number() == "123456789", "Account number should match the initialized value"
