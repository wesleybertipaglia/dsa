# encapsulation: private attributes and methods
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance    

# create an object
account = BankAccount("Alice", 1000)
get_balance = account.get_balance() # access private attribute
set_balance = account.set_balance(2000) # change private attribute
