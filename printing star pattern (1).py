n=int(input("enter the no. of rows in pyramid:"))
m=20
c=''
for i in range(1,n+1):
    print(c*m,end='')
    print('*'*(2*i-1))
    m=m-1
print()
