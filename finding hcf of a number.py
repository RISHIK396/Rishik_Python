'''objective: tofind the hcf of a number
input:num1:integer,num2:integer
output:print the hcf of the numbers'''
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if num1>num2:
    while True:
        if num1%num2==0:
            print("The HCF is",num2)
            break
        else:
            for i in range(num2-1,0,-1):
                if num1%i==0 and num2%i==0:
                    print(i,"is the HCF of num1 and num2")
                    break
else:
    while True:
        if num2%num1==0:
            print("The HCF is",num1)
            break
        else:
            for i in range(num1-1,0,-1):
                if num2%i==0 and num1%i==0:
                    print("The HCF of num1 and num2 is",i)
                    break
print("THANK YOU FOR USING IT")
