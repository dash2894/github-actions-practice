#program for reading a Numerical value
# decide whether It is +ve or -ve or zero by using simple if statement
#IfElseStmtEx2.py
value=float(input("Enter Any Numerical Value:"))#n=0
if(value>0):
    print("\t{} is +VE".format(value))
else:
    if(value<0):
        print("\t{} is -VE".format(value))
    else:
        print("\t{} is ZERO".format(value))
    print("I am from Inner-if..else Statement")
print("I am from outer-if..else Statement")