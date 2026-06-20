#program for reading a Word and
# decide whether It is Palidrome or not 
# using simple if statement
#IfElseStmtEx1.py
value=input("Enter Any Value:") # PYTHON
if(value==value[::-1]):
    print("\t{} is Palindrome".format(value))
else:
    print("\t{} is Not Palindrome".format(value))
print("Program Execution Completed Successfully")
