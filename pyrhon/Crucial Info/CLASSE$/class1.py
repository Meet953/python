# Define a class to represent a book in a library and to display the book information..
class library:
    print"\t \t \t \t WELC()ME TO THE LIBRARY...\n"
    def __init__(self,bn=0,bnm=" ",au=" ",pub=" ",p=0,noc=0,noci=0):
        self.bn = bn                    #  bn   -->Book Number
        self.bnm= bnm                 #   bnm -->Book Name                
        self.au = au                    #   au   --> Author             
        self.pub = pub                  #  pub  --> Publisher   
        self.p = p                      #   p    --> Price
        self.noc = noc                  #  noc   --> No.of copies
        self.noci = noci                #   noci  --> No.of copies issued
    def book(self):
        if self.bn >=100 and self.bn <= 2000:
            print "THE BOOK NAMED -->",self.bnm,"\t //// IS AVAILABLE.////"
        else:
            print"THE BOOK NAMED -->",self.bnm,"\t //// IS NOT AVAILABLE.////"
    def __str__(self):
        return "Book Number:"+str(self.bn)+"||"+"Book Name:"+str(self.bnm)+"||"+"Author:"+str(self.au)+"||"+"Publisher:"+str(self.pub)+"||"+"Price:"+str(self.p)+"||"+"No.of copies:"+str(self.noc)+"||"+"No.of copies issued:"+str(self.noci)
# ----main----
b1=library(1020,"2 States","Chetan Bhagat","Lincorp Pvt Ltd",500,3000,12)
b2=library(9000,"Five Point Someone","Chetan Bhagat","Lincorp Pvt Ltd",700,300,300) 
b3=library(1190,"The Time Machine","HG Wells","Paet Pvt Ltd",250,30,5)
b4=library(120,"The Invisible Man","HG Wells","Paet Pvt Ltd",150,15,3)
b5=library(6074,"Three Mistakes Of My Life","Chetan Bhagat","Lincorp Pvt Ltd",450,24,24)
b1.book()
b2.book()
b3.book()
b4.book()
b5.book()
print"\t\t\n THE DATA BASE OF THE BOOKS IS AS FOLLOWS--->"
print b1
print b2
print b3
print b4
print b5







