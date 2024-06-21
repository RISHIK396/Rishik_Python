# program to read list of n numbers and replace odd position element
#with even position elements.
l=[]
n=int(input("enter the number of elements:"))
while n%2!=0:
    print("please enter even number of terms")
    n=int(input("enter the number of elements:"))
for i in range(1,n+1):
    el=input("enter the elements no.%u:"%i)
    l.append(el)
print("original list",l)

for x in range(0,n,2):
    if(x+1)%2==0:
        l[x],l[x+1]=l[x+1],l[x]
    else:
        continue
print("modified list:",l)
