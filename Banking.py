class Account():
    def __init__(self,acc_holder,balance):
        self.acc_holder=acc_holder
        self.balance=balance


    def deposit(self,deposit_amount):
        self.balance=self.balance+deposit_amount

    def withdrawl(self,withdrawl_amount):
        if self.balance>withdrawl_amount:
            self.balance = self.balance - withdrawl_amount
        else:
            print("Insufficient funds!")

    def __str__(self):
        return f'acc_holder:{self.acc_holder}\nBalance:{self.balance}'

acc=Account("Prajakta",500)
print(acc)
acc.deposit(500)
print(acc)
acc.withdrawl(1200)