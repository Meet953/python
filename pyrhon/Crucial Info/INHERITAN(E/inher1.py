# TO CREATE A CLASS EMPLOYEE AND ANOTHER CLASS CAR AND SHOW THE METHOD
# OF """SINGLE INHERITANCE"""..
class emp(object):                          # ...BASE CLASS...
    cmp_nm="\t\t\t\t YAKIMONO HOLLU AND CO. \t"
    def __init__(self,en,enm,dn):
        self.en=en                  # en --> Employee Number
        self.enm=enm              # enm --> Employee Name
        self.dn=dn                 # dn --> Department
    def __str__(self):
        return "Employee Name ::"+str(self.enm)+" with employee number :"+str(self.en)+" works in the "+str(self.dn)+" department of the Company. "
class car(emp):                             # ...DERIVED CLASS...
    def __init__(self,clr,cnm,enm,en,dn):
        self.clr=clr                     #  Car Colour
        self.cnm=cnm                     # Car Name
        emp.__init__(self,enm,en,dn)  # statement for invoking the __init__()method of the base class.
    def __str__(self):
        return str(self.enm)+" has "+str(self.cnm)+" of "+str(self.clr)+" colour."
# ---main---
print emp.cmp_nm
e1=emp(1123,"Sumit Singh","Manufacturing")
e1_1=car("Red","Wagonar",1123,"Sumit Singh","Manufacturing")
e2=emp(1134,"Ridhi Arora","Finance")
e2_2=car("Black","BMW 09C$",1134,"Ridhi Arora","Finance")
e3=emp(3423,"Rahul Wahi","Sales")
e3_3=car("White","Merc CDI",3423,"Rahul Wahi","Sales")
print e1
print e1_1
print e2
print e2_2
print e3
print e3_3






