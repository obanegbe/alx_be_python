class BankAccount:
    
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(self.account_balance)
        else:
            print("Deposite amount must be greater than zero")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("You do not have up to that in your account balance")
            return False
        elif amount <= 0:
            print("Withdraw amount must be greater than zero")
            return False
        else:
            self.account_balance -= amount
            print(self.account_balance)

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
