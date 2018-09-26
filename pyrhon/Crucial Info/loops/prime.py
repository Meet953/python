#TO CHECK WHWETHER A NUMBER IS PRIME OR NOT..

i=2
r=input("Enter the number:")            # say r = 15
while i<r:
    if r % i==0:
        break
    i=i+1
if r==i:
    print"\t\t\n The Number iS Prime \t\t\n"
else:
    print"\t\t\n The Number iS n0T priMe \t\t\n"





