class BankAccount:
    
    def __init__(self, account_balance):
        self.account_balance = 0.00

    def deposit(self, amount):
        if amount > 0.00:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount < self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
