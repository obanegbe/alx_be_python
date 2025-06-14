class BankAccount:
    
    def __init__(self, account_balance):
        self.account_balance = 0.00

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

    def deposit(self, amount):
        if amount > 0.00:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount < self.__account_balance:
            self.__account_balance -= amount
            return True
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.__account_balance:
            return False
        else:
            return False
