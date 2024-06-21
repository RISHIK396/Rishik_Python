#to find whether a number is a prime number or not

N=int(input("enter the number to be checked: "))
c=2
while c<N:
    if N%c==0:
        print("number is not a prime number")
        break
    c=c+1
else:
    print("number is a prime numebr")
