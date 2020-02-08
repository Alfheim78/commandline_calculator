#script to do basic calculations
#As I constantly forget to bring my calculator to
#the library when doing physics calculation I
#decided to create this script, anyone who finds
#finds this useful may use it as declared by me

#Author: Alfheim78
#Student email: 23842911@sun.ac.za
#Normal email: DefiniteIntegral7@gmail.com

import sys
import math

#create factorial function
def factorial(num):
    if(num <= 1):
        return 1
    return num*factorial(num - 1)

#convert from degrees to radians
def toRadians(degrees):
    return degrees*(math.pi/180)

def usingDegrees():
    if input("using degrees ?(y/n): ") == "y":
        return True
    else:
        return False

def usage():
    print("usage(1): calculator [num1] [num2] -option")
    print("options:\nx(--multiply) --> multiply 2 values")
    print("/(--divide) --> divide 2 values")
    print("+(--add) --> sum of 2 values")
    print("-(--subtract) --> difference of 2 values\n")

    print("usage(2): calculator [num1] -option")
    print("options:\n[-s(--sin)] --> sine function")
    print("[-c(--cos)] --> cosine function")
    print("[-t(--tan)] --> tangent function")
    print("!(--factorial) --> factorial of a value ")

if len(sys.argv) < 2:
   usage() 

if len(sys.argv) == 4:
    num1 = 0
    num2 = 0
    fnum = 0
    operator = ""  
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print(str(num1) + " or " + str(num2) + " is not a valid real value.")
    option = sys.argv[3]
    if option == "x" or option == "--multiply":
        fnum = num1*num2
        operator = "x"
    elif option == "/" or option == "--divide":
        fnum = num1/num2
        operator = "/"
    elif option == "+" or option == "--add":
        fnum = num1 + num2
        operator = "+"
    elif option == "-" or option == "--subtract":
        fnum = num1 - num2
        operator = "-"
    else:
        print("no valid option provided")
        usage()
    print(str(num1) + " " + operator + " " + str(num2) + " = " + str(fnum))

if len(sys.argv) == 3:
    num = 0
    fnum = 0
    operator = ""
    try:
        num = float(sys.argv[1])
    except ValueError:
        print(str(num) + " is not a valid real value.")
    option = sys.argv[2]
    if option == "-s" or option == "--sin":
        if usingDegrees():
            num = toRadians(num)
        fnum = math.sin(num)
        operator = "sin"
    elif option == "-c" or option == "--cos":
        if usingDegrees():
            num = toRadians(num)
        fnum = math.cos(num)
        operator = "cos"
    elif option == "-t" or option == "--tan":
        if usingDegrees():
            num = toRadians(num)
        fnum = math.tan(num)
        operator = "tan"
    elif option == "!" or option == "--factorial":
        fnum = factorial(num)
        operator = "factorial"
    else:
        print("no valid option provided\n")
        usage()
    print(operator + "(" + "{:0.2f}".format(num) + ") = " + "{:0.2f}".format(fnum))  

