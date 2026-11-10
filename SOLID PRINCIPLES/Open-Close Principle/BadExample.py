
class PaymentProcessor:
    
    def Payment(self, payMethod: str, amount:int):
        if(payMethod == "UPI"):
            print(f"The Payment is done via UPI of the rs. {amount}")
        if(payMethod == "credit"):
            print(f"The Payment is done via credit of the rs. {amount}")
        if(payMethod == "debitCard"):
            print(f"The Payment is done via debit card of the rs. {amount}")
        if(payMethod == "NetBanking"):
            print(f"The Payment is done via NetBanking of the rs. {amount}")
            

pay = PaymentProcessor()
pay.Payment("NetBanking", 1000)

    