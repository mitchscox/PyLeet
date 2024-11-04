class BankAccount:
    # Constructor to initialize the account
    def __init__(self, account_number, initial_balance=0.0):
        self.__account_number = account_number  # Private attribute for account number (double underscores)
        self.__balance = initial_balance        # Private attribute for balance

    # Public method to get the balance
    def get_balance(self):
        return self.__balance

    # Method to deposit money with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Deposit amount must be positive")

    # Method to withdraw money with validation
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
        else:
            print("Invalid withdraw amount")

    # Public method to get the account number
    def get_account_number(self):
        return self.__account_number



"""
Explanation:

    Private Attributes: The attributes __balance and __account_number are marked with double underscores (__), making them private. This restricts direct access to these attributes from outside the class.

    Public Methods for Controlled Access: The methods get_balance(), deposit(), and withdraw() provide controlled access to the private attributes.

    Encapsulation of Business Logic: The deposit() and withdraw() methods perform validation, ensuring that only valid operations are allowed, protecting the integrity of the balance.
"""