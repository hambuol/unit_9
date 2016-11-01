# written by oliver hamburger
# program is a class for a simple account
# last modified 11/1/16

class Account:
    """basic funtionality for a simple account. users can make deposits, withdraws and check their balance"""

    def __init__(self, name, accountnumber, balance=0):

        self.name = name
        self.accountNumber = accountnumber
        self.balance = balance

    def deposit(self, amount):
        """
        adds deposited amount to balance
        :param:amount:
        :return:None
        """
        self.balance = self.balance + amount

    def withdraw(self, amount):
        """
        withdraws from account if the withdraw ammount is less than the original ammount
        :param:withdraw
        :return:True or False
        """
        if amount > self.balance:
            return False
        else:
            self.balance -= amount
            return True

    def showbalance(self):
        """
        returns balance
        :param:None
        :return:balance
        """

        return self.balance

    def __str__(self):
        """
        returns users name and current balance
        :param:None
        :return:name and their balance
        """
        return self.name + "has a current balance of" + str(self.balance)
