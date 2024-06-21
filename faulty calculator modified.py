#faulty calculator
operator=input("enter the operator you want to use: ")
num1=int(input("enter the number 1: "))
num2=int(input("enter the number 2: " ))
if num1==1 and num2==4 and oprator=='/':
    print('0.12345')
elif num1==100 and num2==23 and operator=='+':
    print('193')
elif operator=='+':
    print(num1+num2)
elif operator=='-':
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)
elif operator=='/':
    num=input("whether you want num1/num2: ")
    if num=="yes":
        print(num1/num2)
    else:
        print(num2/num1)
elif operator =="//":
    num5=input("whether you want num1//num2")
    if num5=="yes":
        print(num1//num2)
    else:
        print(num2//num1)
elif operator=='%':
    num6=input("whether you want num1%num2")
    if num6=="yes":
        print(num1%num2)
    else:
        print(num2%num1)
elif operator=='*':
    print(num1*num2)
elif operator=='**':
    num7=input("whether you want num1**num2")
    if num7=="yes":
        print(num1**num2)
    else:
        print(num2**num1)
