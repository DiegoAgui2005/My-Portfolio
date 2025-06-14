class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance
        self.__transactions = []

    def _update_balance(self, amount):
        self._balance += amount

    def __log_transaction(self, transaction_type, amount):
        self.__transactions.append({"type": transaction_type, "amount": amount})
        print(f"{transaction_type} of ${amount} on account {self.account_number}")

    def deposit(self, amount):
        self._update_balance(amount)
        self.__log_transaction("Deposit", amount)

    def display_balance(self):
        return self._balance

    def display_transactions(self):
        return self.__transactions


account = BankAccount("123456", 1000)
account.deposit(500)
print(account.display_balance())
print(account.display_transactions())