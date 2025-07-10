#BSCIT-05-0836/2022
class BankAccount:
    def __init__(self, account_number, customer_name, date_of_opening, balance=0.0):
#instance variables
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: ${amount:.2f}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance."
        else:
            self.balance -= amount
            return f"Withdrew: ${amount:.2f}"

    def check_balance(self):
        return f"Current Balance: ${self.balance:.2f}"

    def customer_details(self):
        details = (
            f"Customer Name: {self.customer_name}\n"
            f"Account Number: {self.account_number}\n"
            f"Date of Opening: {self.date_of_opening}\n"
            f"Balance: ${self.balance:.2f}"
        )
        return details

account_number = input("Enter account number: ")
customer_name = input("Enter customer name: ")
date_of_opening = input("Enter date of opening (YYYY-MM-DD): ")

account = BankAccount(account_number, customer_name, date_of_opening)

deposit_amount = float(input("Enter amount to deposit: "))
print(account.deposit(deposit_amount))

withdraw_amount = float(input("Enter amount to withdraw: "))
print(account.withdraw(withdraw_amount))

print("\nAccount Information:")
print(account.customer_details())
print(account.check_balance())
