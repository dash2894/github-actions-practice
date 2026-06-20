#IfElseStmtEx3.py
n=int(input("Enter Any Numerical Integer Value:"))
if(n<0):
    print("\t{} is Invalid Input".format(n))
else:
    if(n%3==0) and (n%5==0):
        print("\t{} is Multiple of both 3 and 5".format(n))
    else:
        if(n%3==0):
            print("\t{} is Multiple of 3".format(n))
        else:
            print("\t{} is Multiple of 5".format(n))