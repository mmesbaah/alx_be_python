class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance (default is 0)."""
        self.account_balance = initial balance

    def deposit(self, amount):
        """deposit the specified amount into the account."""
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    def withdraw(self, amount):
        """withdraw the specified amount if sufficient funds exist. Returns True if successful, False otherwise."""
        if 0 < amount <= self.acount_balance:
            self.acount_balance -= amount 
            return True
        return False
    def display_balance(self):
        """prints the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")


import sys
from bank_account import BankAccount

def main():
    """Handles command-line arguments for banking operations."""
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        if account.deposit(amount):
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid amount.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()


