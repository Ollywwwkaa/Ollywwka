from abc import ABC, abstractmethod
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
class CreditCardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата картой на сумму {amount} руб.")
    def refund(self, amount):
        print(f"Возврат на карту на сумму {amount} руб.")
class PayPalPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата через PayPal на сумму {amount} руб.")
    def refund(self, amount):
        print(f"Возврат через PayPal на сумму {amount} руб.")
if __name__ == "__main__":
    print(" Демонстрация системы платежей \n")
    print("1. Оплата кредитной картой:")
    card_payment = CreditCardPayment()
    card_payment.pay(1000)
    card_payment.refund(500)
    print("\n2. Оплата через PayPal:")
    paypal_payment = PayPalPayment()
    paypal_payment.pay(2000)
    paypal_payment.refund(300)
    print("\n3. Попытка создания экземпляра абстрактного класса PaymentSystem:")
    try:
        payment_system = PaymentSystem()
        print("Экземпляр создан успешно (этого не должно было произойти)")
    except TypeError as e:
        print(f"Ошибка: {e}")
        print("Доказательство: нельзя создать экземпляр абстрактного класса!")
    print("\n4. Полиморфизм - работа через общий интерфейс:")
    payment_methods = [
        CreditCardPayment(),
        PayPalPayment(),
        CreditCardPayment()]
    amounts = [1500, 2500, 800]
    for i, payment_method in enumerate(payment_methods):
        print(f"\n  Платеж {i+1}:")
        payment_method.pay(amounts[i])
    print("\n Демонстрация завершена ")