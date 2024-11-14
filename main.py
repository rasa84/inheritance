from account.CheckingAccount import CheckingAccount
from account.SavingsAccount import SavingsAccount
from company.Designer import Designer
from company.Developer import Developer
from figure.Circle import Circle
from figure.Rectangle import Rectangle

rectangle = Rectangle(5, 6)
print(f"Stačiakampio plotas: {rectangle.area()}")

circle = Circle(5)
print(f"Skritulio plotas: {circle.area()}")

# ----------------------------------------------------------------------------------------------------------------------

developer = Developer("Petras", 1200, "Java")
designer = Designer("Antanas", 1000, "Photoshop")
print(developer.get_details())
print(designer.get_details())

# ----------------------------------------------------------------------------------------------------------------------

s_account = SavingsAccount(100)
s_account.deposit(200)
print(s_account)
s_account.withdraw(50)
print(s_account)
print(f"Palūkanos: {s_account.calculate_interest()}")

c_account = CheckingAccount(100)
c_account.deposit(200)
print(c_account)
c_account.withdraw(50)
print(c_account)
