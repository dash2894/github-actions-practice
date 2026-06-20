#programming for base converting using match case statement
#MatchcaseEx3.py
s="""******************************************************
        AREA OF DIFFERENT fIGURES
******************************************************
        I.  Dec to Binary
            Dec to Octal
            Dec to Hexa
        II. Binary to Dec
            Binary to Oct
            Binary to Hexa
        III.Octal to Dec
            Octal to Binary
            Octal to Hexa
        IV. Hexa to Dec
            Hexa to Binary
            Hexa to Octal
        V: Exit
*******************************************************"""
print(s)
ch=input("Enter the choice for base conversion: ")
match(ch):
    case "I":
        dv=int(input("Enter the Decimal Number system Value: "))
        print("bin({})={}".format(dv,bin(dv)))
        print("oct({})={}".format(dv,oct(dv)))
        print("Hex({})={}".format(dv,hex(dv)))
    case "II":
        bv=input("Enter the Binary Number system value preceded 0b or 0B: ")
        dv=int(bv,2)
        print("Dec({})={}".format(bv,dv))
        print("oct({})={}".format(bv, oct(dv)))
        print("hex({})={}".format(bv,hex(dv)))
    case "III":
        ov=input("Enter the Octal Number system value preceded 0O or 0o: ")
        dv=int(ov,8)
        print("Dec({})={}".format(ov, dv))
        print("Bin({})={}".format(ov, bin(dv)))
        print("Hex({})={}".format(ov, hex(dv)))
    case "IV":
        hv=input("Enter the hexa decimal Number system value preceded 0x or 0X: ")
        dv=int(hv,16)
        print("Dec({})={}".format(hv, dv))
        print("Bin({})={}".format(hv, bin(dv)))
        print("oct({})={}".format(hv, oct(dv)))
    case "V": PASS
    case _:
        print("Your choice is invalid, TRY AGAIN")
print("Program execution completed, Thanks")