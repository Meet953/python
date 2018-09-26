# Declare a class to represent fixed-deposit account of 4 to 5 customers and also display that
#    whether the money can be withdrawn when the half time of the initially given time has passed... 
class fixed_deposit:
    print"\t \t \t WELCOME TO THE 4SHARED BANK \t\n "
    s=10                    # Initally given Time
    def __init__(self,nd=" ",ac=0,t=0,amt=0):
        self.nd=nd              # nd--> Name of Depositor
        self.ac=ac              # ac--> Account Number
        self.t=t                 # t --> Time Period
        self.amt=amt           # amt --> Amount Deposited
    def half_time(self):
        if fixed_deposit.s/2>=self.t:
            print"ACCOUNT HOLDER:",self.ac," NAME:",self.nd,
            print"----THE MONEY CAN BE WITHDRAWN----"
        else:
            print"ACCOUNT HOLDER:",self.ac," NAME:",self.nd,
            print"----THE MONEY CAN'T BE WITHDRAWN----"
    def __str__(self):
        return"Name of Depositor:"+str(self.nd)+" || "+"Account Number:"+str(self.ac)+" || "+"Time Period:"+str(self.t)+" || "+"Amount Deposited:"+str(self.amt)
# ----main----
m1=fixed_deposit("Samarth Arora",1234340145,5,300000)
m2=fixed_deposit("Humpty Sharma",25365445,2,400000)
m3=fixed_deposit("Vikram Rathor",34500989065,5,30000)
m4=fixed_deposit("Sakshi Ahuja",67535475,4,500000)
m5=fixed_deposit("Ansh Kapoor",4449900007,6,700000)
m1.half_time()
m2.half_time()
m3.half_time()
m4.half_time()
m5.half_time()
print"\n THE DATA BASE OF THE BANK MEMBERS IS AS FOLLOWS ---> \n"
print m1
print m2
print m3
print m4
print m5



