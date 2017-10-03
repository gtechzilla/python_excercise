#A basic calculator in python

#LOOP TO ENSURE THE PROGRAM IS RUNNING
while True:
    print ("Enter 'add' to perform addition")
    print ("Enter 'sub' to raise to subtract")
    print ("Enter 'multi' to perform multiplication")
    print ("Enter 'div' to perform division")
    print("Type 'quit' to terminate the calculator")
    value=input(">>>")

    #CHANGES THE CASING IN THE INPUT VALUE TO LOWERCASE
    value=value.lower()
    if value=="quit":
        break
    elif value=="add":
        num1=float(input("Enter your 1st number >>>"))
        num2=float(input("Enter your 2nd number >>>"))
        result = str(num1+num2)
        print("The answer is " + result)
        print("\n")
    elif value=="sub":
        num1=float(input("Enter your 1st number >>>"))
        num2=float(input("Enter your 2nd number >>>"))
        result = str(num1-num2)
        print("The answer is " + result)
        print("\n")
    elif value=="multi":
        num1=float(input("Enter your 1st number >>>"))
        num2=float(input("Enter your 2nd number >>>"))
        result = str(num1*num2)
        print("The answer is " + result)
        print("\n")
    elif value=="div":
        num1=float(input("Enter your 1st number >>>"))
        num2=float(input("Enter your 2nd number >>>"))
        result = str(num1/num2)
        print("The answer is " + result)
        print("\n")
    else:
        print("Check your input")
