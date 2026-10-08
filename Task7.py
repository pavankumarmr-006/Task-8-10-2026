'''7. Bank Account Program
• Create a BankAccount class with account holder and balance.
• Create deposit() and withdraw() methods.
• Do not allow withdrawal when the balance is insufficient.
• Display the final balance.'''

class BankAccount():
    def __init__(self, acc_holder, acc_balance):
        self.acc_holder = acc_holder
        self.acc_balance = acc_balance

    def deposit(self, amount):
        self.acc_balance = self.acc_balance + amount
        print("Deposited: ", amount)


    def withdraw(self, amount):
        if amount <= self.acc_balance:
            self.acc_balance = self.acc_balance - amount
            print("Amount withdrawed: ", amount)
        else:
            print("Insufficient balance!")    

    def final_balance(self):
        print("Holder Name: ", self.acc_holder)
        print("Available Balance: ", self.acc_balance)


# Create bank account
account = BankAccount("Pavan", 150000)


# Deposit money
account.deposit(20000)

# Withdraw money
account.withdraw(30000)

# Try to withdraw more than the balance
account.withdraw(50000)

# Display final balance
account.final_balance()


