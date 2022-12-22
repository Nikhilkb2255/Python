class bank_account:
    def __init__(self,a,n,t):
        self.acc_no = a
        self.name = n
        self.balance = 0
    def deposit(self):
        amt = float(input("Enter the amount to deposit :"))
        self.balance = self.balance + amt
        print("Amount deposited")
    def withdraw(self):
        amt = float(input("Enter the amount to withdraw :"))
        if amt > self.balance:
            print("Balance not sufficient")
        else:
            self.balance = self.balance - amt
    def bal_check(self):
        print("Account balance = ",self.balance)

n = input("Enter account name : ")
a = input("Enter account number : ")
t = input("Enter account type : ")

acc1 = bank_account(a,n,t)

while(1):
    print("*O P T I O N S*")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check balance")
    c = int(input("Enter choice : "))

    if c == 1:
        acc1.deposit()
    elif c == 2:
        acc1.withdraw()
    elif c == 3:
        acc1.bal_check()
    else:
        print("Wrong choice")
