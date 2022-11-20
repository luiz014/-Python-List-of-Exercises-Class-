import random

class CheckingAccount:
    def __init__(self,number=0,name="unknown",balance=0.0):
        self.number=number
        self.name=name
        self.balance=balance
    
    def change_name(self,new_name):
        self.name=new_name
        return new_name
    
    def deposit(self,value):
        self.balance=self.balance+float(value)
        return self.balance        
        
    def withdraw(self,value):
        self.balance=self.balance-float(value)
        return self.balance
    
    def show_account(self):
        print(f'Account number: {self.number}\nName: {self.name}\nBalance: {self.balance}')
    
def main():
    while True:
        option=int(input('Choose a option: \n1-Create account\n2-Change name \n3-Deposit\n4-Withdraw\n5-Bank Statement\n6-Leave \n'))
        if option ==1:  
            name=str(input('What is your name ? '))
            a=random.randint(1000,9999)
            account=CheckingAccount(a,name,0)
            account.show_account()
        if option ==2:
            change=str(input(f'You name is {account.name} which one do you want to change? '))
            account.change_name(change)        
            account.show_account()
        if option ==3:
            a=float(input('How much do you want to deposit? '))
            account.deposit(a)
            account.show_account()
        if option ==4:
            b=float(input('How much do you want to withdraw? '))
            account.withdraw(b)
            account.show_account()
        if option ==5:
            account.show_account()
        if option ==6:
            break

main() 
