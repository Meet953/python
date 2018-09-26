#INSERTING AN ELEMENT IN THE SORTED ARRAY(using bisect module)..
import bisect
L=list(input("Enter a list:"))
print"The list in sorted order is"
print L
val=int(raw_input("Enter the value to be inserted:"))
ind=bisect.bisect(L,val)
bisect.insort(L,val)
print val,"inserted at index",ind
print "The list after inserting new element is"
print L





