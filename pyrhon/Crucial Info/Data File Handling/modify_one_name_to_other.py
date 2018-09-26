# TO MODIFY NAME "RAHUL" TO "RAJESH" IN THE FILE "Marks.det"
f=open("Marks.det","r+")
while True:
      pos=f.tell()
      recs=f.readline()
      if recs.find("Rahul")!=-1:
            recs=recs.replace("Rahul","Rajesh")
            f.seek(pos)
            f.write(recs)
            break
f.close()



