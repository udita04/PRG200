class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited NPR", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn NPR", amount)
        else:
            print("Insufficient funds")

    def get_balance(self):
        print(self.name, "-", self.account_number)
        print("Balance: NPR", self.balance)
        print()


accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000)
]

bank_accounts = []

for name, account_number, balance in accounts:
    account = BankAccount(name, account_number, balance)
    bank_accounts.append(account)

bank_accounts[1].deposit(3000)

bank_accounts[2].withdraw(15000)

bank_accounts[0].withdraw(2000)

print("\nFinal Balances")
print("")

for account in bank_accounts:
    account.get_balance()