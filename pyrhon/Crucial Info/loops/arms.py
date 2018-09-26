# TO CHECK WHETHER A NUMBER IS ARMSTRONG NUMBER OR NOT..

sum=0
n=input("Enter the value of n:")        # say n = 15
h=n
while n>0:
    d=n%10
    sum=sum+d**3
    n=n/10
if sum==h:
    print"ARMSTRONG NUMBER"
else:
    print"NOT ARMSTRONG NUMBER"










