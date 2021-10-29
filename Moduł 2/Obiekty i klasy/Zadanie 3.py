class BankAccount:

    def __init__(self, number):
        self.number = number
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

a = BankAccount(1)
a.deposit_cash(100.0)
a.print_info()
print(a.withdraw_cash(20.0))
a.print_info()

    
