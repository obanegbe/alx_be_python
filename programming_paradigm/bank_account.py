class BankAccount:
    
    def __init__(self, account_balance):
        self.account_balance = 0.0

    def deposit(self, amount):
        if amount > 0.0:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
