# DELETION OF ELEMENT FROM THE ARRAY...
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
    else:
          return False
# ----main----
l=list(input("Enter desired list:"))
print"The list in sorted order is"
print l
v=input("Enter a suitable value from the list ::")
position=bsearch(l,v)
if position:
      del l[position]
      print "The list after deleting",v,"is"
      print l
else:
      print "S0RRY!! no such element in the list"




