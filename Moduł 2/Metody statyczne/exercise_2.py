class BankAccount:

    next_acc_number = 1

    def __init__(self):
        self.number = self.next_acc_number
        BankAccount.next_acc_number += 1
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0.0:
            self.cash += amount
            
    def withdraw_cash(self, amount):
        if amount > 0.0:
            if amount <= self.cash:
                self.cash -= amount
                return amount
            else:
                amount = self.cash
                self.cash = 0.0
                return amount

    def print_info(self):
        print(self.number)
        print(self.cash)

a = BankAccount()
b = BankAccount()
c = BankAccount()

print(a.number)
print(b.number)
print(c.number)
