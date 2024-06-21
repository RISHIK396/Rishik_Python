#design a calculator which will correctly solve all the problems except the following ones:
#45*3=555,56+9=77,56/6=4
#your program should take operaator and the two numbers as_input_from the user and then return the result
operator=input("enter the operator to be used:")
num1=int(input("enter the numeber1 to be used:"))
num2=int(input("enter the number2 to be used:"))
if num1==45 and num2==3 and operator=='*':
    print("555")
elif num1==56 and num2==9 and operator=='+':
    print("77")
elif num1==56 and num2==6 and operator=='/':
    print("4")
elif operator=='+':
    print(num1+num2)
elif operator=='-':
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)
elif operator=='/':
    print(num1/num2)
elif operator=='%':
    print(num1%num2)
elif operator=='**':
    print(num1**num2)
elif operator=='//':
    print(num1//num2)
else("plz check your input")
