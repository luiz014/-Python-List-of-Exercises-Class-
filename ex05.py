


class CheckingAccount:
    def __init__(self,number=0,name="unknown",balance=0):
        self.number=number
        self.name=name
        self.balance=balance
    
    def change_name(self,new_name):
        self.name=new_name
        return new_name
    
    def deposit(self,value):
        self.balance=self.balance+int(value)
        return self.balance        
        
        
    def withdraw(self,value):
        self.balance=self.balance-int(value)
        return self.balance
    
    def show_account(self):
        print(f'Account number: {self.number}\nName: {self.name}\nBalance: {self.balance}')
    
def main():
    
    account=CheckingAccount(789,'Biden',1000.0)
    change=str(input('Do you want to change your name ? [y/n] ')).lower()[0]
    if change == 'y':
        name=input('Which one? ')
        account.change_name(name)        
    account.show_account()
    print('-'*30)
    a=float(input('How much do you want to deposit? '))
    account.deposit(a)
    account.show_account()
    print('-'*30)
    b=float(input('How much do you want to withdraw? '))
    account.withdraw(b)
    account.show_account()
    print('-'*30)
    
main() 