# A USER DEFINED FUNCTION REGARDING RECTANGLE OPERATIONS...
import math
def operations():
    while True:
        print"  Rectangle Menu \t "
        print"\t 1.Area"
        print"\t 2.Perimeter"
        print"\t 3.Diagonal"
        print"\t 4.Exit"
        ch=input("Enter your Choice(between 1-4):")
        if ch==1:
            x=input("Enter the LENGTH of the rectange(in cm) :")
            y=input("Enter the BREADTH of the rectangle (in cm) :")
            a = x * y
            print " Area of the ractange is --> ",a ,"sq.cm "
        elif ch==2:
            x=input("Enter the LENGTH of the rectange(in cm) :")
            y=input("Enter the BREADTH of the rectangle (in cm) :")
            p = 2*(x + y)
            print " Perimeter of the rectangle is --> ",p ,"cm "
        elif ch==3:
            x=input("Enter the LENGTH of the rectange(in cm) :")
            y=input("Enter the BREADTH of the rectangle (in cm) :")
            d = math.sqrt (x*x + y*y)
            print " The diagonal of the rectangle is --> ",d,"cm "
        elif ch==4:
            print " --------------- /////  PROGRAM OVER  ///// -----------------"
            break
        else:
            print" \t\t\t\t\t  //Enter a valid choice//  \t\t\t\t\t  "
        print
    return "  "
o = operations()    





   
