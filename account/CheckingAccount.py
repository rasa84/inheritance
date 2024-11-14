from account.BankAccount import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, balance=0.0, withdrawal_fee=2.00):
        super().__init__(balance)
        self.withdrawal_fee = withdrawal_fee

    def withdraw(self, amount):
        amount += self.withdrawal_fee
        super().withdraw(amount)
