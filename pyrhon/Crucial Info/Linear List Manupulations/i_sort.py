# INSERTION SORT..
def insertion_sort(ar):
      for i in range(1,len(ar)):
            v=ar[i]
            j=i
            while ar[j-1]>v and j>=1:
                  ar[j]=ar[j-1]
                  j=j-1
            ar[j]=v
# ----main----
ar=input("Enter a desired list:")
print "0riginal list is:",ar
insertion_sort(ar)
print"List after sorting",ar











