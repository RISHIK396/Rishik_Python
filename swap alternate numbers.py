#EXAMPLE 14
def swapalternate(l):
    n=len(l)
    for i in range(0,n-1,2):
        l[i],l[i+1]=l[i+1],l[i]
a=[10,20,30,40,50,60,70]
print(a)
swapalternate(a)
print(a)
a=[12,34,56,65,43,23]
print(a)
swapalternate(a)
print(a)
