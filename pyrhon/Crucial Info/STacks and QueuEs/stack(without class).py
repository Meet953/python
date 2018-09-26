# STACK IMPLEMENTATION WITHOUT USING CLASSES...
print "\t\t ...STACK OPERATIONS..."
s=[]           # initially stack is empty.
c="y"
while c=="y":
      print"1.PUSH"
      print"2.POP"
      print"3.DISPLAY"
      ch=input("Enter your choice:")
      if ch==1:
            a=input("Enter a number:")
            s.append(a)
      elif ch==2:
            if s==[]:
                  print"..STACK EMPTY.."
            else:
                  print"Deleted element is:",s.pop()
      elif ch==3:
            L=len(s)
            for i in range(L-1,-1,-1):
                  print s[i]
      else:
            print"WRONG INPUT"
      c=raw_input("Do you want to continue or not {y or n}:")
      print






