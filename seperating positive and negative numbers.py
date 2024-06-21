#to create two new list one with positive numbers and other with negative numbers
list1=[1,2,3,4,5,6,7,8,-1,-2,-3,-4,-5,-6,-7]
list2=[]
list3=[]
for items in list1:
    if(list1[items]>0):
        list2.append(list1[items])
    else:
        list3.append(list1[items])
print("the original list is",list1)
print("the positive number list is",list2)
print("the negative number list is",list3)
