# DICTIONARY FUCTIONS AND METHODS

print"\t\t\t DICTIONARY FUNCTIONS AND METHODS\t\t\t"
print "1. The len() method :returns length of dictionary"
print 'syntax: len(<dictionary>)'
d1={'name':'Dhruv','salary':315000,'age':25}
print d1
length=len(d1)
print 'Length of the dictionary is ',length
print

print"2. The clear() method : removes all itms from the dictionary"
print' syntax: <dictionary>.clear()'
d2={'name':'Sameer','salary':152000,'age':22}
print d2
d2.clear()
print d2,"---Empty dictionary"
print

print'3. The get() method : display the value with the given key'
print 'syntax: <dictionary.get(key,[default])>'
d3={'name':'Rahul','salary':85600,'age':21}
print d3
print d3.get('salary'),"---salary"
print

print'4. The has_key() method : checks the presence of given key'
print'syntax: <dictionary>.has_key(key)'
d4={'name':'Mridual','salary':80000,'age':20}
print d4
print d4.has_key('age'),'when checking for age'
print d4.has_key('gender'),'when checking for gender'
print

print'5. The items() method : returns list of all keys with their value'
print'syntax : <dictionary>.items()'
d5={'name':'Parv','salary':95000,'age':25}
print d5
print d5.items(),'---items'
print

print'6.  The keys() method : returns a list of keys'
print'syntax : <dictionary>.keys()'
d6={'name':'Nisha','salary':220000,'age':27}
print d6
print d6.keys(),'---keys'
print

print'7. The values() method :  returns list of values'
print'syntax : <dictionary>.values()'
d7={'name':'Krishan','salary':350000,'age':29}
print d7
print d7.values(),'---values'
print

print'8. The update method : merges key-value pairs from new dictionary to orignal dictionary'
print'syntax : <dictionary>.update(<new dictionary>)'
D81={'name':'Harry','salary':35000,'age':25}
D82={'name':'Humpty','salary':60000,'age':28 ,'gender':'male' }
print D81
print D82
print 'After uptating',D81,'by D82'
D81.update(D82)
print'Dictionary 1(updated):',D81
print'Dictionary 2:',D82
print

print '9. The cmp() method : compares two dictionary and gives ----> '
print '\t 1(dict1>dict2); -1(dict2>dict1); 0(dict1=dict2) \t'
print 'syntax : cmp(dict1,dict2)'
d9a={'name':'Sakshi','salary':210000,'age':26}
d9b={'name':'Parth','salary':5000000,'age':27}
d9c={'name':'Sakshi','salary':210000,'age':26}
d9d={'name':'Vicky','salary':9500000,'age':25}
print 'dictionary 1 :',d9a
print 'dictionary 2 :',d9b
print 'dictionary 3 :',d9c
print 'dictionary 4 :',d9d
print 'on comparing dictonary 1 and dictionary 2 gives :', cmp(d9a,d9b)
print 'on comparing dictonary 1 and dictionary 3 gives :', cmp(d9a,d9c)
print 'on comparing dictonary 1 and dictionary 4 gives :', cmp(d9a,d9d)
print 'on comparing dictonary 2 and dictionary 3 gives :', cmp(d9b,d9c)
print 'on comparing dictonary 2 and dictionary 4 gives :', cmp(d9b,d9d)
print 'on comparing dictonary 3 and dictionary 4 gives :', cmp(d9c,d9d)
print
print'------------------------>\tPROGRAM OVER\t<-------------------------------------'
print
































