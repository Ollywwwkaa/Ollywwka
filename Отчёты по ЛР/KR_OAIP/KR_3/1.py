def audit_log(func):
    def wrapper(self, amount):
        print(f'Выполнена операция "{func.__name__}". Сумма: {amount}')
        return func(self, amount)
    return wrapper
class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance
    @audit_log
    def deposit(self, amount):
        if amount <= 0:
            print("Сумма для пополнения должна быть положительной")
            return False
        self.__balance += amount
        return True
    @audit_log
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма для снятия должна быть положительной")
            return False
        if amount > self.__balance:
            print("Недостаточно средств на счете")
            return False
        self.__balance -= amount
        return True
    def balance(self):
        return self.__balance
if __name__ == "__main__":
    account = BankAccount(1000)
    print(f"Начальный баланс: {account.balance()}\n")
    account.deposit(500)
    print(f"Баланс после пополнения: {account.balance()}\n")
    account.withdraw(300)
    account.withdraw(1500)
    print(f"Баланс после попытки снятия: {account.balance()}\n")
    account.deposit(-100)
    account.withdraw(0)
    print(f"Итоговый баланс: {account.balance()}")