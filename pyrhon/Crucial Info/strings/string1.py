#1. TO CHECK WHETHER A STRING IS PANINDROME OR NOT..
string=raw_input("Enter the STRING:")
l=len(string)
i=0
j=l-1
z=1
while i<=j:
    if string[i] == string[j]:
        i=i+1
        j=j-1
    else:
        z=0
        break
if z==1:
    print"\n\t THE GIVEN STRING IS PALINDROME"
else:
    print"\n\t THE GIVEN STRING IS NOT PALINDROME"




















































