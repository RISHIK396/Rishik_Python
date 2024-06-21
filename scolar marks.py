#EXAMPLE 7
def scholars(L):
    s=[]
    for i in L:
        if i>90:
            s.append(i)
    return s
L1=[67,98,45,92]
L2=[95,58,95,99,87]
slr1=scholars(L1)
slr2=scholars(L2)
print("L1:",L1)
print("sclr marks from L1:",slr1)
print("L2:",L2)
print("sclr marks from L2:",slr2)
