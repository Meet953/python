# TO INPUT A LIST AND CALCULATE THE SUM OF ALL THE EVEN NUMBERS FROM IT..
L1=list(input("Enter the list of numbers:"))
l=len(L1)
s=0
for i in range(0,l):
    if L1[i]%2==0:
        s=s+L1[i]
print "THE TOTAL SUM IS =",s








