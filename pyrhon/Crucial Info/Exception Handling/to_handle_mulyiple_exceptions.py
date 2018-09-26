# TO HANDLE MULTIPLE EXCEPTIONS..
try:
      f=open("myfile.txt")
      line=f.readline()
      Int=int(s.strip())
      calculated_value=101/Int
except IOError:
      print"I/O error occured"
except ValueError:
      print"Could not convert data to integer"
except ZeroDivisionError:
      print"Zero Division Error"
except:
      print"Unexpected Error"
else:
      print"YEH!! No Exceptions"




