class Account:

    def __init__(self, owner, balance = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f'Dear {self.owner}, your balance is {self.balance}, you can not extract {amount}!')

    def __str__(self):
        return (f'Owner: {self.owner} \nBalance: {self.balance}')

acct1 = Account('Jose',100)

print(acct1.balance)
print(acct1.owner)
acct1.deposit(200)
print(acct1.balance)
acct1.withdraw(100)
print(acct1.balance)
acct1.withdraw(150)
print(acct1.balance)
acct1.withdraw(51)
print(acct1.balance)
print(acct1)
print(type(acct1.balance))
print(type(acct1.owner))
print(type(acct1))