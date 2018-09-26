# TO WRITE INSTANCES OF CLASS STUDENT ONTO A FILE NAMELY ""student.log""
import pickle
class student:
      def __init__(self,rno=0,name=" "):
            self.rollno=rno
            self.name=name
            self.marks1,self.marks2,self.marks3=0.0,0.0,0.0
      def readmarks(self):
            print"Enter marks of 3 Subjects"
            self.marks1=float(raw_input("Subject 1:"))
            self.marks2=float(raw_input("Subject 2:"))
            self.marks3=float(raw_input("Subject 3:"))
      def display(self):
            print"Student details are:"
            print"Roll Number:",self.rollno
            print"Name:",self.name
            print"Marks in 3 subjects:",self.marks1,self.marks2,self.marks3
stud1=student(12,"Pranay")
stud2=student(15,"Trisha")
stud1.readmarks()
stud2.readmarks()
f1=open("student.log","wb")
pickle.dump(stud1,f1)
pickle.dump(stud2,f1)
f1.close()







