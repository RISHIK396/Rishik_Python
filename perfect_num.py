#perfect number
'''list1=[]
num=int(input("enter the number to check whether the number is a perefect number or not:"))
for i in range(1,num//2+1):
    if num%i==0:
        list1.append(i)
    else:
    	pass
if sum(list1)==num:
    print("the number is a perfect number")
else:
    print("the number entered is not a perfect number")
'''
#LCM OF A NUMBER
'''num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
i=1
while True:
   if i%num1==0 and i%num2==0:
       break
   else:
       i+=1
print("the lcm of",num1,"and",num2,"is",i)
'''
#HCF of a number
'''num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
if (num1>num2):
    a=num2
else:
    a=num1
i=a
for i in range(i,0,-1):
    if num1%i==0 and num2%i==0:
        break
    else:
        pass
print("the hcf of",num1,"and",num2,"is",i)
''' 

#finding the sum of the digits
'''num=int(input("enter the number whose sum of digits is to be found:"))
sum1=0
for i in range(0,num+1):
    sum1+=i
print("the sum of the numbers is:",sum1)
'''
#finding whether a number is an armstrong number or not
'''num=input("enter the number which is to be checked:")
list1=list(num)
print(list1)
list2=[]
for i in list1:
    list2.append(int(i)**3)
print(list2)
if sum(list2)==int(num):
    print("the number entered is an armstrong number")
else:
    print("the number is not an armstrong number")
 '''
#printing table of 5 and 6
'''i=1
while i<=10:
    print(5,'x',i,'=',5*i,'\t',6,'x',i,'=',6*i)
    i+=1'''
