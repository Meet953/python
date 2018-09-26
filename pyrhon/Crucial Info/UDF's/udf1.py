# Fibonacci Series..
def fibonaci(n):
    f=0                     # f --> First Number
    s=1                     # s --> Second Number
    print f,s,
    for i in range(3,n+1):
        t=f+s
        print t,            # t --> Third Number
        f=s
        s=t
        i=i+1
    return ' '
n=input("Enter the number :")        # Number Whose Fibonacci Series You Want To Know.
print"The Series Is --> ",fibonaci(n)








