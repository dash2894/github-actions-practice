#program for reading a Numerical value decide
# whether It is +ve or -ve or zero by using simple if statement
#IfElifElseStmtEx1.py
value=float(input("Enter Any Numerical Value:"))#n=10
if(value>0):
    print("{} is +VE Value".format(value))
elif(value<0):
    print("{} is -VE Value".format(value))
elif(value==0):
    print("{} is ZERO".format(value))
print("Program execution Completed")