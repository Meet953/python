#3. TO READ A STRING AND CONVERT UPPER CASE TO LOWER CASE AND VICE-VERSA..
a=raw_input("Enter the value:")
a1=''
for i in range(0,len(a),1):
    if a[i].isupper()==True:
        a1+=a[i].lower()
    elif a[i].islower()==True:
            a1+=a[i].upper()
print "\t So the string now becomes --->\n ",a1




































































