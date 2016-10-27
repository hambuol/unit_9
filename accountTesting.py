import account

mike = account.Account("mike", 2468, 10)

if mike.withdraw(5):
    print("your new balance is", mike.showBalance())
else:
    print("insuficient funds")

mike.deposit(50)
print(mike.showBalance())

if mike.withdraw(100):
    print("your new balance is" , mike.showBalance())
else:
    print("insuficient funds")

mike.deposit(900)




jim = account.Account("jim", 1359, 30)
bob = account.Account("bob", 1234, 70)


