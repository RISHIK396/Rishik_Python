#EXAMPLE 13
def halfswap(l):
    n=len(l)
    for i in range(n//2):
        l[i],l[n//2+i]=l[n//2+i],l[i]
a=[10,20,30,40,50,60,70]
print(a)
halfswap(a)
print(a)
a=[12,34,56,65,43,23]
print(a)
halfswap(a)
print(a)
