# TO CHECK WHETHER A NUMBER PALINDROME OR NOT..

n=input("Enter the value of n:")        # say n = 121
digit=0
rev=0
d=n
while n>0:
    digit=n%10
    n=n/10
    rev=rev*10+digit
print "THE REVERSE IS:",rev
if d==rev:
    print"PALINDROME!!!"
else:
    print"NOT PALINDROME!!!"



    
