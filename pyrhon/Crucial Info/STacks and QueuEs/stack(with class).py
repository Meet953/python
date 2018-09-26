# STACK IMPLEMENTATION USING CLASSES..
print"\t\t\t !!STACK OPERATIONS!!"
class stack:
      s=[]              # initially stack is empty.
      def push(self):
            a=input("Enter any number:")
            stack.s.append(a)
      def display(self):
            L=len(stack.s)
            for i in range(L-1,-1,-1):
                  print stack.s[i]
a=stack()
c="y"
while c=="y":
      print"1.PUSH"
      print"2.POP"
      print"3.Display"
      ch=input("Enter number of your choice{1 or 2 or 3}:")
      if ch==1:
            a.push()
      elif ch==2:
            if a.s==[]:
                  print"Stack Empty"
            else:
                  print"Deleted element is:",a.s.pop()
      elif ch==3:
            a.display()
      else:
            print "WRONG INPUT"
      c=raw_input("Do you want to continue or not?")
      print















