class Account:
    def __init__(self, account_no , balance):
        self.acc_no = account_no
        self.balance = balance

    def debit_amount(self,deb_amount):
        self.balance-=deb_amount
        return self.balance,deb_amount
    
    def credit_amount(self , credit_amount ):
        self.balance+=credit_amount
        return self.balance,credit_amount 
    
    def print_balance(self):
        return self.balance
    
account = Account(123456 , 3087345)  

# Account details
print("Balance Details for Account having Number", account.acc_no,"is:", account.balance) 

# After debiting amount
updated_balance,deb_amount = account.debit_amount(2)
print("Your balance after debiting amount",deb_amount,"is",updated_balance)

# After credeting amount
updated_balance,credit_amount = account.credit_amount(3)
print("Your balance after crediting amount",credit_amount,"is",updated_balance)

# current balance after updation
current_balance = account.print_balance()
print("Your updated balance is",current_balance)



  


            




        

