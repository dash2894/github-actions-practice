# Taking user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a == b:
    print("First and second numbers are equal.")
if b == c:
    print("Second and third numbers are equal.")
if a == c:
    print("First and third numbers are equal.")
if a == b and b == c:
    print("All three numbers are equal.")
if a < b and a < c:
    print("The smallest number is:", a)
if b < a and b < c:
    print("The smallest number is:", b)
if c < a and c < b:
    print("The smallest number is:", c)
