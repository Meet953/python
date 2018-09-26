while True:
    print '1. Volume of sphere'
    print '2. Volume of cone'
    print '3. Area of triangle'
    print '4. Area of rhombus'
    print '5. Exit'
    ch=input("Enter your choise(between 1-5):")
    if ch==1:
        r=input('Enter radius of sphere:')
        vol= 1.33*3.14*(r**3)
        print "Volume of sphere is -->",vol
    elif ch==2:
        r=input('Radius of cone:')
        h=input('Height of cone:')
        vol=0.33*3.14*(r**2)*h
        print "Volume of cone is -->",vol
    elif ch==3:
        b=input('Base of the triangle:')
        a=input('Altitude/height of the triangle')
        area=(b*a)/2
        print area
    elif ch==4:
        
        d1=input('Length of diagonal 1:')
        d2=input('Length of diagonal 2:')
        area=(d1*d2)/2
        print area
    elif ch==5:
        print "-----------------\t\tPROGRAM OVER\t\t--------------------------"
        break
    else:
        print "Please enter a valid choise (between 1-5)"
    print
    print'\t\t!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    print











