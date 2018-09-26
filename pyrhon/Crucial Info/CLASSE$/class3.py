# Define a class Applicant which store details of 5 to 7 students of class XI-D and display their aggregate marks and "GRADE"...
class applicant:
    class_name="XI-D"
    num_stud=7
    def __init__(self,ano=0,n=" ",agg=0.0,g=" "):
        self.ano=ano        #Admission Number
        self.n=n             # Name
        self.agg=agg        # Aggregate Marks
        self.g=g            # Grade
    def grademe(self):
        if self.agg>=80:
            self.g='A'
        elif self.agg>=65:
            self.g='B'
        elif self.agg>=50:
            self.g='C'
        else:
            self.g='D'
a1=applicant(12924,"Manvi Khanna",74)
a2=applicant(12923,"Namit Kapoor",45)
a3=applicant(12925,"Ashok Kumar",75)
a4=applicant(12926,"Naresh Kumar",59)
a5=applicant(12920,"Rahul Ahuja",89)
a6=applicant(12922,"Nikita Arora",97)
a7=applicant(12927,"Naresh Ahuja",70)
print "--THE MARKS RECORD OF CLASS ",applicant.class_name," ARE AS FOLLOWS--"
print"NUMBER OF APPLICANT'S IN THE CLASS ARE : ",applicant.num_stud
a1.grademe()
print"The Aggregate Marks Of ",a1.n,"Are",a1.agg," and Grade is " ,a1.g
a2.grademe()
print"The Aggregate Marks Of ",a2.n,"Are",a2.agg," and Grade is " ,a2.g
a3.grademe()
print"The Aggregate Marks Of ",a3.n,"Are",a3.agg," and Grade is " ,a3.g
a4.grademe()
print"The Aggregate Marks Of ",a4.n,"Are",a4.agg," and Grade is " ,a4.g
a5.grademe()
print"The Aggregate Marks Of ",a5.n,"Are",a5.agg," and Grade is " ,a5.g
a6.grademe()
print"The Aggregate Marks Of ",a6.n,"Are",a6.agg," and Grade is " ,a6.g
a7.grademe()
print"The Aggregate Marks Of ",a7.n,"Are",a7.agg," and Grade is " ,a7.g


            
