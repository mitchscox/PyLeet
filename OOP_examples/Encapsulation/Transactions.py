# main.py
import BankAccounts

# Example usage
if __name__ == "__main__":
    # Creating a BankAccount object
    account = BankAccounts.BankAccount("123456789", 1000.0)

    # Accessing the balance through the public method
    print("Balance:", account.get_balance())

    # Depositing and withdrawing money
    account.deposit(500)
    account.withdraw(200)
    print("Balance after transactions:", account.get_balance())

    # Accessing account number through the public method
    print("Account Number:", account.get_account_number())

