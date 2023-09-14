import os
import pandas as pd
class Bank():
    def __init__(self,Ac_Holder_Name,Account_Number,Join_balance = 1000):
        self .Ac_Holder_Name = Ac_Holder_Name
        self .Account_Number = Account_Number
        self .Join_balance = Join_balance
    def Account_creation(self):
        data = {'Ac_Holder_Name':[Ac_Holder_Name],'Account_Number':[Account_Number],'Join_balance':[Join_balance]}
        df = pd.DataFrame(data)
        df.to_csv('Bank.csv',mode='a',index=False,header=False)
        return ('Account Created {}'.format(self .Ac_Holder_Name))

Ac_Holder_Name = str(input("Ac_Holder_Name   "))
Account_Number = int(input("Account_Number"))
c1 = Bank(Ac_Holder_Name,Account_Number)
print(c1.Account_creation())


