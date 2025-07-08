###Static variable:
#1.Class level variable.
#2.one copy is created.
#3.Accessed using class name.

###Non-static variable:
#1.object level variable.
#2.copies will be depends on how many object are created.
#3.Accessed using object name.

class Account:
    bank_name="SBI"

    def __init__(self,holder_name,account_number,balance):
        self.holder_name=holder_name
        self.account_number=account_number
        self.balance=balance

    def showData(self):
        print("Bank name:",Account.bank_name)
        print("Holder name:",self.holder_name)
        print("Account number:",self.account_number)
        print("balance:",self.balance)
        print("#################################")

Account.bank_name="State Bank Of India"
ac1=Account("ganesh kasture",101,10000)
ac1.showData()
ac2=Account("omkar kasture",102,15000)
ac2.showData()

