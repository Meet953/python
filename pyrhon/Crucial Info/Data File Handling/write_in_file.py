# WAP TO ENTER ROLL NO , MARKS AND NAME OF STUDENTS OF
# A CLASS IN A FILE CALLED "Marks.det"...
c=int(raw_input("How many students are there in the class ?"))
fileout=open("Marks.det","w")
for i in range(c):
      print"Enter details for student",(i+1),"below:"
      rollno=int(raw_input("Roll No:"))
      name=raw_input("Name:")
      marks=float(raw_input("Marks:"))
      rec=str(rollno)+","+name+","+str(marks)+"\n"
      fileout.write(rec)
fileout.close()


