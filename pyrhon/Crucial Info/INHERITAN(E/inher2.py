# TO CREATE A CLASS SPECIAL ENGINE AND ANOTHER CLASS BIKE AND ONE MORE
#  CLASS RACING BIKES TO SHOW THE METHOD OF  """MULTIPLE INHERITANCE"""..
class specialengine(object):                        # Base Class
    def __init__(self,p):
        self.power=p
    def IGNTION(self):
        print"Its Engine Started"
class bike(object):                                 # Derived Class 1
    def __init__(self,clr):
        self.colour=clr
    def changeGears(self,gr):
        print "Gear was changed to ",gr
    def turn(self,direction):
        print "it turned in the ",direction," direction..."
class racingBikes(specialengine,bike):              # Derived Class 2
    def __init__(self,clr,p,tr,spd):
        specialengine.__init__(self,p)
        bike.__init__(self,clr)
        self.turnRadius=tr
        self.speed=spd
    def start(self):
        print "I saw a ",self.colour," coloured HARLEY DAVIDSON "
        print"The Bike was ready to vrooom!!"
        self.IGNTION()
        self.changeGears(2)
        print "At the speed of",self.speed,"Km/hr"
        print "With Horse Power :::",self.power
        print"With turn radius --->",self.turnRadius
# ---main---
rbike=racingBikes("Green",750,"6''",200)
rbike.start()
rbike.turn("left")
print 


