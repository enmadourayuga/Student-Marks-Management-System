#task 3
from datetime import datetime

class Account:
    
    def __init__(self,accno,name,fund,total_deposit=0,total_withdrawal=0,history=[]):
        self.accno=accno
        self.name=name
        self.fund=fund
        self.total_deposit=total_deposit
        self.total_withdrawal=total_withdrawal
        self.history=history
        print(f"Welcome to ABC Bank\nAccount Created Successfully\nCurrent Balance: ${self.fund}")

    def deposit(self):
        d=int(input("Enter Deposit Number:"))
        if d<0:
            print("Invalid Amount")
        else:
            self.fund+=d
            self.total_deposit+=d
            print(f"Successfully Deposited ${d}")
            self.history.append(f"Deposit ${d}")
            

    def withdraw(self):
        now = datetime.now()
        ct = now.strftime("%H")
        limit = 0
        if ct == 0:
            limit=0

        if limit <= 25000:
            w=int(input("Enter Withdrawal Number:"))
            if w>self.fund:
                print("Insufficient Balance")
            else:
                self.fund-=w
                self.total_withdrawal+=w
                print(f"Successfully Withdrawn ${w}")
                self.history.append(f"Withdraw ${w}")
        else:
            print("Daily Withdrawal Limit Exceeded")

    def balance(self):
        print(f"Current Balance:${self.fund}")

    def mini_statement(self):
        print(f"Total Deposited:${self.total_deposit} \nTotal Withdrawn:${self.total_withdrawal} \nCurrent Balance:${self.fund}")

    def his(self):
        sl=1
        for i in self.history:
            print(f"{sl}.{i}")
            sl+=1

acno=["A1001B","A1002B","A1003B","A1004B","A1005B"]
option=input("Add Account?(Y/N)")
if option=="Y":
    n=input("Name:")
    f=int(input("Funds:"))


c1=Account('Tom',1000)

o=0
print("1.Deposit Money \n2.WithdraW Money \n3.Check Balance \n4.Mini Statement \n5.Transaction History \n6.Exit")
while o!=6:
    o=int(input("Option:"))

    if o==1:
        c1.deposit()

    if o==2:
        c1.withdraw()

    if o==3:
        c1.balance()

    if o==4:
        c1.mini_statement()

    if o==5:
        c1.his()
    