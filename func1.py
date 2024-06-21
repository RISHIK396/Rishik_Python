#EXAMPLE 27
def tensum(*n):
    s=0
    for i in n:
        if type(i) is int or type(i) is float:
            if i%10==0:
                s+=i
        else:
            print('unsupported type')
    return s
print(tensum(20,34,19))
print(tensum(5,'a',30))
print(tensum("big",24,50,20))
