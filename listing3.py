# program 3
#a
l=[]
n=int(input("enter the number of elements you want to input:"))
for i in range(1,n+1):
    el=int(input("enter the elements:"))
    l.append(el)
print("the modified list is:")

#b
largest=l[0]
smallest=l[0]
for x in l:
    if x>largest:
        largest=x
    elif x<smallest:
        smallest=x

print("largest number:",largest)
print("smallest number:",smallest)
print()
#c
fir=largest
sec=l[0]
thir=[0]

for y in l:
    if y>sec:
        if y<largest:
            sec=y
for z in l:
    if z>thir:
        if z<sec:
            thir=z
            print("the largest element is thir:",thir)
            print()

#d
L=[]
print("enter new five elements for new list:")
for i in range(1,6):
    el=int(input("enter the elements:"%i))
    L.append(el)
    print("the new list is:",L)
    
