#3. TO PRINT THE GIVEN CODE..
n=input("Enter any number of your choice (1-15):")
for i in range(1,n):
    space=n-i
    if i==1:
        print" "*space+"*"
    else:
        print" "*space+"*"+" "*(i+(i-3))+"*"
for j in range(n,0,-1):
    space=n-j
    if j==1:
        print" "*space+"*"
    else:
        print" "*space+"*"+" "*(j+(j-3))+"*"




































