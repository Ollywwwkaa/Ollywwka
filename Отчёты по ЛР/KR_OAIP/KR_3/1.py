def audit_log(operation_name):
    def decorator(fun):
        def wrapper(self, summ):
            print(f'Операция "{operation_name}" на сумму: {summ}')
            return fun(self, summ)
        return wrapper
    return decorator
class BankAccount:
    balance = 0
    @audit_log("пополнение")
    def deposit(self, summ):
        self.balance += summ
    @audit_log("снятие")
    def withdraw(self, summ):
        if summ <= self.balance:
            self.balance -= summ
        else:
            print("Недостаточно денег")
account = BankAccount()
print(f"Баланс: {account.balance}")
account.deposit(100000)
print(f"Баланс: {account.balance}")
account.withdraw(300)
print(f"Баланс: {account.balance}")
account.withdraw(800000)
print(f"Баланс: {account.balance}")
account.withdraw(800)
print(f"Баланс: {account.balance}")