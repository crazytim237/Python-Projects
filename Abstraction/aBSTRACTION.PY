from abc import ABC, abstractmethod
class car(ABC):
    def payslip(self, amount):
        print ("Your purchase amount: ", amount)

    @abstractmethod
    def payment (self, amount):
        pass
class DebitCardPayment (car):
#here we've defined how to implement the payment function from its parent payslip class.
    def payment(self, amount):
        print ('Your purchase amount of {} exceeded your $100 limit '.format (amount))
obj = DebitCardPayment ()
obj.payslip ("$400")
obj.payment ("$400")
