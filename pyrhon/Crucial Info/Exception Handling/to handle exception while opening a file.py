# TO HANDLE EXCEPTION WHILE OPENING A FILE..
print"FOR Ist FILE"
try:
      my_file=open("myfile.txt","r")
      print my_file.read()
except:
      print"ERROR opening file!!"

print
print"FOR IInd FILE"

try:
      my_file=open("read_file.txt","r")
      print my_file.read()
except:
      print"ERROR this file can't be opened or it does not exist."




