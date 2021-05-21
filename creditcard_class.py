class creditcard:
    """Customer Credit Card"""
    def __init__(self,customer,bank,account,limit):
        """ Initial balance=0"""
        self._customer=customer
        self._bank=bank
        self._account=account
        self._limit=limit
        self._balance=0
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_limit(self):
        return self._limit
    def get_account(self):
        return self._account
    def get_balance(self):
        return self._balance
    def charge(self,price):
        if(price+self._balance)>self._limit:
            return False
        else:
            self._balance+=price
            return True
    def make_payment(self,amount):
        self._balance-=amount
list=[]
def options():
        name=input("Enter Your name")
        bank=input("Enter your bank name")
        account=int(input("Enter bank account number:"))
        limit=float(input("Enter max credit limit"))
        list.append(creditcard(name.capitalize(),bank.capitalize(),account,limit))
        print(list[0].get_customer)
if __name__ == '__main__':
    for i in range(3):
        options()
