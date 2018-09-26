# TUPLE FUNCTIONS AND METHODS..

print '1. The len() method ; returns the length of  the tuple'
print 'syntax : len(<tuple>)'
t1=('Jaggu',65780,27,'sales')
print "tuple-1 :",t1
print "the length of the tuple-1 :",len(t1)
print

print '2. The max() method ; returns the element from the tuple having maximum value.'
print 'syntax : max(<tuple>)'
t2=(100,120,140,200,220,240,240,300,320,360)
print 'tuple-2 :',t2
print 'maximum value of tuple :',max(t2)
print

print '3. The min() method ; returns the element from the tuple having minimum value'
print'syntax : min(<tuple>)'
t3=(102, 122, 142, 202, 223, 244, 305, 326, 334)
print 'tuple-3:',t3
print 'minimum value of tuple :',min(t3)
print

print '4. The cmp() method ; compares two tuples and returns --->'
print'\t 1(tuple1>tuple2); -1(tuple2>tuple1); 0(tuplet1=tuple2) \t'
print 'syntax : cmp(tuple1,tuple2)'
t3a=(20,40,60,80)
t3b=('20','40','60','80')
t3c=([20], [30], [40], [50])
t3d=(20, 40, 60, 80)
print 'tuple 3-a',t3a
print 'tuple 3-b',t3b
print 'tuple 3-c',t3c
print 'tuple 3-d',t3d
print 'comparing tuple3-a and tuple3-b', cmp(t3a, t3b)
print 'comparing tuple3-b and tuple3-c', cmp(t3b, t3c)
print 'comparing tuple3-a and tuple3-d', cmp(t3a, t3d)
print

print '5. The tuple() method ; create tuples from given sequence'
print 'syntax : tuple(<sequence>)'
print 'empty tuple',tuple()
print 'tuple from a string(say "abc")',tuple('abc')
print 'tuple from a list(say [1,2,3])',tuple([1,2,3])
print 'tuple from keys of dictionary(say {1:"1", 2:"2"})',tuple({1:"1", 2:"2"})
print



















