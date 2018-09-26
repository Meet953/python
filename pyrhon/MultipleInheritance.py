class personal:
    id=1
    name="a"
    dob="7/09/1800"

    def show_pers(self):
        id = input("Enter ID")
        name = input("Enter Name")
        dob = input("Enter DOB")
        print("Personal Details | ID :",id," Name :",name," DOB:",dob)
    
    
class professional:
    dept="a"
    post="b"

    def show_prof(self):
        dept = input("Enter Department")
        post = input("Enter Designation")
        print("Professional Details | Department :",dept," Designation :",post)
        
class academics:
    degree="BSc"
    exp=2

    def show_acad(self):
        degree = input("Enter Degree")
        exp = input("Enter Experience")
        print("Academic Details | Degree :",degree," Experience :",exp)
        
class employee(personal,professional,academics):
    def show_over(self):
        super(employee,self).show_pers()
        super(employee,self).show_prof()
        super(employee,self).show_acad()
        #print("Personal Details | ID :",self.id," Name :",self.name," DOB:",self.dob)
        #print("Professional Details | Department :",self.dept," Designation :",self.post)
        #print("Academic Details | Degree :",self.degree," Experience :",self.exp)

emp = employee()
emp.show_over()
