#program for implementing all area of different Figures
#MatchcaseEx2
import sys
s="""******************************************************
        AREA OF DIFFERENT fIGURES
******************************************************
        C. Circle
        S. Square
        R. Rectangle
        T. Triangle
        E. Exit
*******************************************************"""
print(s)
ch=input("Enter your Choice: ")
match(ch):
    case "C"|'c':
        r=float(input("Enter Radius: "))
        ac=3.14*r**2
        print("\tArea of Circle=",ac)
    case "R"|'r':
        l=float(input("Enter the Length value: "))
        b=float(input("Enter the Breadth value: "))
        ra=l*b
        print("\tArea of Rectangle:",ra)
    case "S"|'s':
        s=float(input("Enter side of square: "))
        sa= s**2
        print("\tArea of Square: ",sa)
    case "T"|'t':
        print("Enter the values of three sides of triangle: ")
        a,b,c=float(input()),float(input()),float(input())
        s=(a+b+c)/2
        ta=(s*(s-a)*(s-b)*(s-c))**0.5
        print("\tArea of Square: ",ta)
        print("-------------OR---------------")
        b=float(input("Enter Base of triangle: "))
        h=float(input("Enter Height of triangle: "))
        ta=(1/2)*b*h
        print("\tArea of Triangle: ",ta)
    case "E"|'e':
        print("Thanks for using program")
        sys.exit()
    case _:
        print("Your selection is invalid. Try Again")
print("Program execution completed")
