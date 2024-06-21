def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)
  
a = int(input("enter the number1:"))
b = int(input("enter the numeber2:"))
  
# prints 12
print("The gcd of ",a," and",b," is : ", end="")
print(hcf(a, b))
