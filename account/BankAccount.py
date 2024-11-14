class BankAccount:
    def __init__(self, balance=0.0):
        self.balance = balance

    def __str__(self):
        return f"Balansas: {self.balance} eur"

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Per mažas pinigų likutis")
