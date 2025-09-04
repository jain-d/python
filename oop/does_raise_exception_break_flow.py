class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount < 1:
            raise Exception("cannot deposit nothing.")
        self.__balance += amount
        print(f"still executing {self.__balance}")

john_account = BankAccount("John's Account Number", 500)

try:
    john_account.deposit(0)
except:
    print("it failed, as conspired")
    print(f"here is john's balance {john_account.balance}")
