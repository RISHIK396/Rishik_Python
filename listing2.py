# Q.3
#read the list of integers
ineg=[]
ipos=[]
n=int(input("enter the numbers of elements:"))
for i in range(1,1+n):
    el=int(input("enter the element no.%u:"%i))
    if el>0:
        ipos.append(el)
    elif el<0:
        ineg.append(el)
    else:
        pass #zero is not included in any of the list
print("lists of the positive numbers are:",ipos)
print("lists of the negative numbers are:",ineg)

            
