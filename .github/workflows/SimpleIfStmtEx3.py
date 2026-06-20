#Program for Generating Pay Slip of an employee
#SimpleIfStmtEx3.py
import sys
empno=int(input("Enter Employee Number:"))
empname=input("Enter Employee Name:")
basicsal=float(input("Enter Employee Basic Sal:"))
if(basicsal<=0):
    print("\tInvalid Salary-try again")
    sys.exit()
if(basicsal>=10000):
    da = (20/100)*basicsal
    ta = (10/100)*basicsal
    hra = (8/100)*basicsal
    ma = (1/100)* basicsal
    cca = (0.5/100)* basicsal
if(0<basicsal<10000):
    da = (10/100)*basicsal
    ta = (5/100)*basicsal
    hra = (4/100)*basicsal
    ma = (0.5/100)* basicsal
    cca = (0.5/100)* basicsal
netsal = basicsal + da + ta + hra + ma + cca
print("-" * 50)
print("EMPLOYEE PAY SLIP")
print("-" * 50)
print("\tEmployee Number:{}".format(empno))
print("\tEmployee Name:{}".format(empname))
print("\tEmployee Basic Salary:{}".format(basicsal))
print("\tDA:{}".format(da))
print("\tTA:{}".format(ta))
print("\tHRA:{}".format(hra))
print("\tMA:{}".format(ma))
print("\tCCA:{}".format(cca))
print("\tNET SALARY:{}".format(netsal))
print("-" * 50)