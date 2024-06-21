#EXAMPLE 12
def calc(a):
    a=list(a)
    a[0]=a[0]*2
    a[1]=a[1]+1
    print("calc:",a)
p=(100,200)
print(p)
calc(p)
print(p)
