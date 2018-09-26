# 5. TO READ THE E-MAIL ID OF A PERSON IN THE FORM OF A STRING AND
#                                  ENSURE THAT IT BELONGS TO DOMAIN @gmail.com ..

email=raw_input("Enter the email id:")
domain='@gmail.com'
l=len(domain)
m=len(email)
s=email[m-l :]
if s == domain :
    if l!=m:
        print"It is valid email id."
    else:
        print"This is an invalid email id."
else:
    print"This email id is either not valid or belong to some other domain."























