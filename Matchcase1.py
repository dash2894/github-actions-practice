#program for implementing all arithimetic operation by using match case.
#MatchCaseEx1
import sys
print("*"*50)
print("\tArithimetic Operationd")
print("*"*50)
print("\t\t1.Addition")
print("\t\t2.Substraction")
print("\t\t3.Multiplication")
print("\t\t4.Division")
print("\t\t5.Floor Division")
print("\t\t6.Modulo Division")
print("\t\t7.Exponentiation")
print("\t\t8.Exit")
print("*"*50)
ch=int(input("Enter ur Choice: "))
match(ch):
    case 1:
        print("Enter two values for Addition: ")
        a,b = float(input()),float(input())
        print("\t\tsum({},{})={}".format(a,b,a+b))
    case 2:
        print("Enter two values for Substraction: ")
        a,b = float(input()),float(input())
        print("\t\tsub({},{})={}".format(a,b,a-b))
    case 3:
        print("Enter two values for Multiplication: ")
        a,b = float(input()),float(input())
        print("\t\tmul({},{})={}".format(a,b,a*b))
    case 4:
        print("Enter two values for Division: ")
        a,b = float(input()), float(input())
        print("\t\tDiv({},{})={}".format(a,b,a/b))
    case 5:
        print("Enter two values for Floor Division: ")
        a,b = float(input()), float(input())
        print("\t\tFloorDiv({},{})={}".format(a,b,a//b))
    case 6:
        print("Enter two values for Modulo Division: ")
        a,b = float(input()), float(input())
        print("\t\tMod({},{})={}".format(a,b,a%b))
    case 7:
        print("Enter two values for Exponentian: ")
        a,b = float(input()), float(input())
        print("\t\ttpow({},{})={}".format(a,b,a**b))
    case 8:
        print("Thanx for using Python")
        sys.exit()
    case _: #default case block
        print("Your selection of operation wrong-try again")
print("Program completed")