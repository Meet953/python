# TO GENERATE FIBONACCI VALUES..
def fibonacci(max):
      a,b=0,1
      while a<max:
            yield a
            a,b=b,a+b
# ---main---
n=int(raw_input("Fibonacci Values upto number:"))
for i in fibonacci(n):
      print i,



      
