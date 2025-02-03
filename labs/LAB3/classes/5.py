class Bank():
    def __init__(self, owner, balance): # owner and balance are attributes
        self.owner = owner
        self.balance = balance

    def Deposit(self, amount):
        if amount > 0:
            self.balance += amount  
            print(f"Your current balance: {self.balance}")
        else:
            print("Error")

    def Withdrawals(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Your current balance: {self.balance}")
        else:
            print("Error: Insufficient funds.")

bank = Bank("Bakhyt", 1000)

print(f"Account owner: {bank.owner}")
print(f"Initial balance: {bank.balance}")


bank.Deposit(1000)


bank.Withdraw(3000)
bank.Withdraw(2000)