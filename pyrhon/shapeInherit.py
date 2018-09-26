class shape:
    def calc_Area(self):
        print("Default Area")

    def calc_Peri(self):
        print("Default Perimeter")

class square(shape):
    def calc_Area(self,s):
        print("Sqaure Area : ",s*s)

    def calc_Peri(self,s):
        print("Sqaure Perimeter : ",4*s)

class rectangle(shape):
    def calc_Area(self,ln,br):
        print("Rectangle Area : ",ln*br)

    def calc_Peri(self,ln,br):
        print("Rectangle Perimeter : ",2*(ln+br))

class circle(shape):
    def calc_Area(self,r):
        print("Circle Area : ",3.14*r*r)

    def calc_Peri(self,r):
        print("Circle Perimeter : ",2*3.14*r)

c = circle()
c.calc_Area(3)
c.calc_Peri(3)

r = rectangle()
r.calc_Area(3,5)
r.calc_Peri(3,5)

s = square()
s.calc_Area(2)
s.calc_Peri(2)
