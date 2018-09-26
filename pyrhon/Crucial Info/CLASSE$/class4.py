# DEFINE A CLASS EMPLOYEE TO STORE ALL THE DETAILS OF THE EMPLOYEES OF 
# VARIOUS DEPARTMENTS IN THE HEAD OFFICE AND TO INCREASE THEIR SALARY BY 5000 IF
# THE DEPARTMENT IS FINANCE OR OTHERWISE INCREASE THE SALARY BY 2000 AND
# DISPLAY THE DATABASE...
class employee:
    no_of_emp=0
    c_name="ACCENTURE"
    c_city="MUMBAI"
    def __init__(self,ei=" ",en=" ",d=" " ,s=0):
        self.ei=ei          # employee ID
        self.en=en          # Employee Name
        self.d=d            # Department
        self.s=s            # Salary
        employee.no_of_emp+=1
    def check(self):
        if self.d=="Finance":
            self.s+=5000
        else:
            self.s+=2000
    def __str__(self):
        return "Name of employee:"+str(self.en)+"||"+"Employee ID:"+str(self.ei)+"||"+"Department:"+str(self.d)+"||"+"Salary:"+str(self.s)
# ---main---
s1=employee("FC113","Mishthi Gupta","Finance",800000)
s2=employee("IC356","Deepali Mittal","IT",600000)
s3=employee("SA007","Arshita Kharwal","Sales",700000)
s4=employee("FC673","Aditya Dhingra","finance",400000)
s5=employee("AC0005","Anupam Ahuja","Accounts",300000)
s1.check()
s2.check()
s3.check()
s4.check()
s5.check()
print"\t\t\nTHE DATABASE OF--",employee.c_name,"Pvt Ltd  ","HEAD OFFICE IN--",
print employee.c_city,"ARE AS FOLLOWS ---->"
print"\t\tTHE NUMBER OF EMPLOYEES IN THE COMPANY ARE :::",employee.no_of_emp
print s1
print s2
print s3
print s4
print s5



