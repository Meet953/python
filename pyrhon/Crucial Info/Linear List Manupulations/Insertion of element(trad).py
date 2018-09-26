# INSERTING AN ELEMENT IN THE SORTED ARRAY(traditionally)..
def POS(L,val):
    size=len(L)
    if val<L[0]:
        return 0
    else:
        pos=-1
        for i in range(0,size):
              if L[i]<=val and val<=L[i+1]:
                    pos=i+1
                    break
        if pos ==-1:
              pos=size
        return pos      
def SHIFT(L,pos):
      L.append(None)
      size=len(L)
      i=size-1
      while i>=pos:
            L[i]=L[i-1]
            i=i-1
# ----main----
L=[10,20,30,40,50,60,70]
print "List in sorted order is"
print L
val=int(raw_input("Enter the new element to be inserted:"))
position=POS(L,val)
SHIFT(L,position)
L[position]=val
print "The list after inserting",val,"is"
print L




