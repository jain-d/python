class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.__balance = balance
        self.__ac_number = account_number

    @property
    def balance(self):
        return self.__balance

account1 = BankAccount("John", "54321", 3000)
print(account1.balance)
