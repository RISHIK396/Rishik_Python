# to do various functions in a list
list1=[1,2,4,6,8,9,12,45,0,-1,23,54,-67]
print("the original list is:",list1)
largest_number=max(list1)
smallest_number=min(list1)
print("the largest number is",largest_number)
print("the smallest number is",smallest_number)
third_largest=list1.sort()
print("the third largest number is:",list1[-3])
list2=[15,16,17,18,19,20]
print("the list of five numbers is:",list2)
list1.extend(list2)
print("the extended list is",list1)
