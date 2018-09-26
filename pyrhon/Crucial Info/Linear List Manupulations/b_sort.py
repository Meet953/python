# BUBBLE SORT..
def swap_elements(alist):
    i=0
    while(i<len(alist)-1):
        if(alist[i]>alist[i+1]):
            t=alist[i]
            alist[i]=alist[i+1]
            alist[i+1]=t
        i=i+1
        print"List after pass",(i),":",alist
def bubble_sort(alist):
    for d in range(len(alist)-1):
        print"------Iteration",d,"------"
        swap_elements(alist)

# ----main----
L1=[15,6,33,78,59,223,2]
print"Original list is ::",L1
bubble_sort(L1)
print"List after sorting ::",L1
        









