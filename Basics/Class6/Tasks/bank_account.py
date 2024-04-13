# Create a class called "BankAccount" with attributes for account number and balance.
# Add methods to the BankAccount class for depositing and withdrawing money.
# Create a subclass of BankAccount called "SavingsAccount" with an additional attribute for interest rate.
# Override the BankAccount class's withdraw method in the SavingsAccount subclass to include a fee for each withdrawal.

class BankAccount:
    def __init__(self, account_nr, balance):
        self.account_nr = account_nr
        self.balance = balance

    def depositing(self, amount):
        self.balance += amount
        print(f"Deposited {amount}€. New balance is {self.balance}€.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}€. New balance is {self.balance}€.")
        else:
            print("Not enough")


class SavingsAccount(BankAccount):
    def __init__(self,account_nr, balance, interest_rate):
        super().__init__(account_nr, balance)
        self.interest_rate = interest_rate
        self.withdrawal_fee = 1.50

    def withdraw(self, amount):
        total_withdrawal = self.withdrawal_fee + amount
        if total_withdrawal <= self.balance:
            self.balance -= total_withdrawal
            print(f"Withdrew {amount}€ with fee of {self.withdrawal_fee}. New balance is {self.balance}€")
        else:
            print("Not enough")


bank_acc = BankAccount("123368901237", 100000)
bank_acc.depositing(2500)
bank_acc.withdraw(9000)
savings_acc = SavingsAccount("2746732549", 100000, 0.05)
savings_acc.depositing(70)
savings_acc.withdraw(4689)
