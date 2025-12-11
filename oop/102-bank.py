# Bank Account class** (deposit, withdraw, check balance).
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
    def check_balance(self):
        return self.balance
    
    def __str__(self):
        return f"BankAccount with balance {self.balance}"
    
bank = BankAccount(1000)
print(bank)
bank.deposit(500)
print(bank)
bank.withdraw(200)
print(bank)
print(bank.check_balance())