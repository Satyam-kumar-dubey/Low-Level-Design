
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    
    @abstractmethod
    def Payment(self, amount:int):
        pass
    
    
class UPI(PaymentMethod):
    def Payment(self, amount:int):
         print(f"Payment is done via UPI of rs. {amount}")
         
class NetBanking(PaymentMethod):
    def Payment(self, amount:int):
         print(f"Payment is done via NetBanking of rs. {amount}")
         
class Creditcard(PaymentMethod):
    def Payment(self, amount:int):
         print(f"Payment is done via Creditcard of rs. {amount}")
         
         
class PaymentProcessor:
    
    def process_payment(self, pay:PaymentMethod, amount:int):
        pay.Payment(amount)
        
        
Upi = UPI()
Credit = Creditcard()

pay = PaymentProcessor()
pay.process_payment(Credit,900)