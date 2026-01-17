from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amont):
        pass

class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")

if __name__=="__main__":
    p = CreditCardPayment()
    p.pay(1000)

    p = UPIPayment()
    p.pay(500)
