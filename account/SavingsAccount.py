from account.BankAccount import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, balance=0.0, interest_rate=0.05):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate
