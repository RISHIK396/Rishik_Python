import math
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
discroot=math.sqrt(b**2-4*a*c)
root1=(-b+discroot)/(2*a)
root2=(-+discroot)/(2*a)
print()
print("the two roots are:%0.2f,%0.2f"%(root1,root2))
