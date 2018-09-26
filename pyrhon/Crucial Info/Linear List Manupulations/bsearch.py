# BINARY SEARCH...
def bsearch(ar,val):
    beg=0           # initially let the begining be zero
    end=len(ar)-1
    while beg<=end:
        mid=(beg+end)/2
        if ar[mid]==val:
            return mid
        elif ar[mid]>val:
            end=mid-1
        else:
            beg=mid+1
    return -1
# ----main----
l=list(input("Enter desired binary list size (max 10) -->"))
v=input("Enter a suitable value from the list ::")
k=bsearch(l,v)
print "Value is found at the position",k











