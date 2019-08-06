# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.balance = balance
        self.int_rate = int_rate
    
    def make_deposit(self, amount):
        self.balance += amount
        return self

    def widthdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient Funds! Balance is only at {self.balance}. Your widthdrawal request of {amount} can't be completed.")
        else:
            self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f"The Balance is {self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.int_rate)
        print(f"With your interest rate of {self.int_rate}, your new balance is now {self.balance}")
        return self

sam_account = BankAccount(0.25, 50000)
johhn_account = BankAccount(0.025, 1000000)

sam_account.make_deposit(2500).make_deposit(2500).make_deposit(2500).widthdraw(15000).yield_interest().display_account_info()
johhn_account.make_deposit(10000).make_deposit(25000).widthdraw(50000).widthdraw(10000).widthdraw(5000).widthdraw(2500).yield_interest().display_account_info()