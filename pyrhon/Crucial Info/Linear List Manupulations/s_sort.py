# SELECTION SORT..
def selection_sort(L):
    k=L[0]
    u=len(L)
    for i in range (0,u):
        k=L[i]
        pos=i
        for j in range(i+1,u):
            if L[j]<k:
                k=L[j]
                pos=j
            t=L[i]
            L[i]=L[pos]
            L[pos]=t
    return L
# ----main----
L=list(input("Enter a random list -->"))
h=selection_sort(L)
print "The Random List In Ascending Order Now Is ::",h



























