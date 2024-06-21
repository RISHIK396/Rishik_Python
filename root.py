#PROGRAMS THAT COMPUTE THE REAL ROOTS OF A QUADRATIC EQUATION.
import math
print()
a=int(input("enter the coefficient of a :"))
b=int(input("enter the coefficient of b:"))
c=int(input("enter the coefficient of c:"))
discroot= math.sqrt(b*b-4*a*c)
root1=(-b + discroot)/(2*a)
root2=(-b-discroot)/(2*a)
print()
print("the two roots are:",(root1,root2))
