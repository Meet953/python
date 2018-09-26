# LINEAR SEARCH..
def lsearch(ar,item):
    p=0                 # initial position be zero.
    for i in ar:
        if i==item:
            return p+1
        p=p+1
    return -1
# ----main----
l=list(input("Enter desired linear list size (max 10) -->"))
v=input("Enter a suitable value from the list ::")
k=lsearch(l,v)
if k!= -1:
    print "Value",v,"is found at the position",k
else:
    print"Such value is not contained in the given list."
    












