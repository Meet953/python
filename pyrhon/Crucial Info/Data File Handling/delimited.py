#WAP TO READ FROM A COMMA-DELIMITED FILE
# AND DISPLAYING INDIVIDUAL ITEMS..
fileinp=open("Marks.det","r")
filecon=fileinp.readlines()
i=1
for rec in filecon:
      onerec=rec.split(",")
      rollno=int(onerec[0])
      name=onerec[1]
      marks=float(onerec[2])
      print"Record",i,"contains:",rollno,name,marks
      i=i+1
fileinp.close()

