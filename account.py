class Account:

    def __init__ (self, name, accountNumber, balance = 0):

        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        else:
            self.balance = self.balance - amount
            return True

    def showBalance(self):
        return self.balance

    def __str__(self):
        return self.name + "has a current balance of" + str(self.balance)





