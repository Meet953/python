def dictionary(n):
    compwinners={}
    for a in range (n):
        key=raw_input("Enter the name of student:")
        value=int(raw_input("Number of competitions won:"))
        compwinners[key] = value
        print"Dictionary now is :"
        print compwinners
    return ' '
n=int(raw_input("How many students? --->"))
dictionary(n)
