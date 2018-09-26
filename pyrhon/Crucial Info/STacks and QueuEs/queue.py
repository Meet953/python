# QUEUE IMPLEMENTATION...
print"\t\t !!QUEUE IMPLEMENTATION!!"
a=[]              # initially queue is empty.
c="y"
while c=="y":
      print"1.INSERT"
      print"2.DELETE"
      print"3.Display"
      ch=input("Enter your choice{1 or 2 or 3}:")
      if ch==1:
            b=input("Enter a number:")
            a.append(b)
      elif ch==2:
            if a==[]:
                  print"Queue Empty"
            else:
                  print"Deleted element is",a[0]
                  del a[0]
      elif ch==3:
            L=len(a)
            for i in range(0,L):
                  print a[i]
      else:
            print"WRONG INPUT"
      c=raw_input("Do you want to continue or not?")
      print



