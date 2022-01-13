class parkville:
    def __init__(self,account_name,account_balance):
        self.account_name=account_name
        self.account_balance=account_balance
    def calculate(self,years):
        for i in range(years):
            print("\nthe account name is : ",self.account_name)
            self.account_balance=self.account_balance*1.03
            print("the account balance of year {} is {} ".format(i+1,self.account_balance))
    '''def display(self):
        parkville.calculate()
      #  print("\nthe account name is : ", self.account_name)
     #   print("the account balance of year ", i + 1, "is ", self.account_balance)'''
bank_accname=input("enter the account name: ")
bank_accname=bank_accname.title()#capitilizes every first letter of the words
bank_accbalance=float(input("\nplease enter your account balance: "))
employee_1=parkville(bank_accname,bank_accbalance)
employee_1.calculate(4)
#employee_1.display()