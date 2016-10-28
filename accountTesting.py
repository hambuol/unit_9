# written by oliver hamburger
# program testes account class

# imports account class
import account

# creates acount with name and given ammount
mike = account.Account("mike", 2468, 10)
# withdraws given ammount only if ammount is smaller than account
if mike.withdraw(5):
    print("your new balance is", mike.showbalance())
else:
    print("insuficient funds")
# deposits given ammount into balance
mike.deposit(50)
print(mike.showbalance())
# withdraws given ammount only if ammount is smaller than account
if mike.withdraw(100):
    print("your new balance is", mike.showbalance())
else:
    print("insuficient funds")
# deposits given ammount into balance
mike.deposit(900)
print(mike.showbalance())

# creates acount with name and given ammount
jim = account.Account("jim", 1359, 30)
# withdraws given ammount only if ammount is smaller than account
if jim.withdraw(5):
    print("your new balance is", jim.showbalance())
else:
    print("insuficient funds")
# deposits given ammount into balance
jim.deposit(50)
print(jim.showbalance())
# withdraws given ammount only if ammount is smaller than account
if jim.withdraw(100):
    print("your new balance is", jim.showbalance())
else:
    print("insuficient funds")
# deposits given ammount into balance
jim.deposit(900)
print(jim.showbalance())

# creates acount with name and given ammount
bob = account.Account("bob", 1234, 70)
# withdraws given ammount only if ammount is smaller than account
if bob.withdraw(5):
    print("your new balance is", bob.showbalance())
else:
    print("insuficient funds")
# deposits given ammount into balance
bob.deposit(50)
print(bob.showbalance())
# withdraws given ammount only if ammount is smaller than account
if bob.withdraw(100):
    print("your new balance is", bob.showbalance())
else:
    print("insuficient funds")
# deposits given ammount into balance
bob.deposit(900)
print(bob.showbalance())
