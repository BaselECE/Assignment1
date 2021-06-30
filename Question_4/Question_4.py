#Here is the bank class
class bank():
    account_num=0
    def __init__(self,fname,lname,profit,amount,phone_n):
        self.fname  =  fname
        self.lname  =  lname
        self.profit  =  profit
        self.amount = amount
        self.phone_n  =  phone_n
        bank.account_num+=1
        print("creating new account")
    def getfullname(self):
        return self.fname + " " +self.lname
    def info (self):
        return ('name : '+self.fname + '  '+self.lname+' amount '+str(self.amount)+' profit :'+str(self.profit)+' phone number '+str(self.phone_n))
    def setprofit(self,profit):
        self.profit=profit
    def get_account_num(cls):
        return 'the number of accounts'+cls.account_num

#Here is the s_bank class    
class s_bank(bank):
    syr_account_num=0
    def __init__(self,fname,lname,profit,amount,phone_n,syrian_id):
        super().__init__(fname,lname,profit,amount,phone_n)
        self.syrian_id=syrian_id
        s_bank.syr_account_num+=1
        print("creating a new account")
    def info (self):
        return('name : '+self.fname + '  '+self.lname+' amount '+str(self.amount)+' profit :'+str(self.profit)+ \
               ' phone number '+str(self.phone_n)+' syrian ID : '+str(self.syrian_id))
    def get_account_num(cls):
        return 'the number of s_accounts'+cls.syr_account_num
def main():
    user1=bank('Ali','Hasan',30,300,925412563225)
    print(user1.info())
    user2=s_bank('Basel','Abras',97,'150',936251425878,20)
    print(user2.info())
if __name__=='__main__':
    main()

