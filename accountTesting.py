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
print(mike.showBalance())


jim = account.Account("jim", 1359, 30)
if jim.withdraw(5):
    print("your new balance is", jim.showBalance())
else:
    print("insuficient funds")

jim.deposit(50)
print(jim.showBalance())

if jim.withdraw(100):
    print("your new balance is" , jim.showBalance())
else:
    print("insuficient funds")

jim.deposit(900)
print(jim.showBalance())


bob = account.Account("bob", 1234, 70)
if bob.withdraw(5):
    print("your new balance is", bob.showBalance())
else:
    print("insuficient funds")

bob.deposit(50)
print(bob.showBalance())

if bob.withdraw(100):
    print("your new balance is" , bob.showBalance())
else:
    print("insuficient funds")

bob.deposit(900)
print(bob.showBalance())




