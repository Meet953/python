while True:
    try:
        x=int(input("Enter a Number"))
        print('you entered',x)
        break
    except ValueError:
        print("OOps!That was no valid no. Try Again")

