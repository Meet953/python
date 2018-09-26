a=['pam','sds',232,13.3]
print("list a = ",a)

#list indices starts at 0
#print(a[0])
#print(a[3])

#print(a[-2])
#print(a[-3])
#print(a[-1])

#list can be sliced, concatenated and so on
#print(a[1:-1])
#print(a[:2] + ['bac',2*2])
#print(3*a[:3] + ['Boe!'])


#possible to change some items
#a[0:3] = [1,12]
#print(a)

#remove some
#a[0:2] = []
#print(a)

#nest list
q=[2,3]
p=[1,q,4]
print(p)
print(len(p))
print(p[1])
print(p[1][0])
p[1].append('xtra')
print(p)

a=[66.6,333,333,1,1234.5]
print(a.count(333),a.count(66.6),a.count('x'))
a.insert(2,-1)
print(a)

a.insert(2,-1)
print(a)

print(a.index(333))

a.remove(333)
print(a)

a.reverse()
print(a)

a.sort()
print(a)


