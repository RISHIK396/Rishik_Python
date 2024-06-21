#program 4
def reverse(L):
    L_new=[]
    i=0
    c=-1
    length=len(L)
    while i<length:
        L_new+=[L[c]]
        i+=1
        c-=1
    return L_new
L=[]
n=int(input("enter the number of the elements in the list:"))
for x in range(1,n+1):
    el=input("enter the element no.%u:"%x)
    L.append(el)
    print("ORIGINAL LIST:",L)
    rev=reverse(L)
    print("REVERSED LIST:",rev)
