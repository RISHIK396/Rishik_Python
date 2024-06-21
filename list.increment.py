#program to increment the elements of a list passed as an argumentto a function
def increment(list2):
    for i in range(0,len(list2)):
        #5 is added to individual elements in the list
        list2[i]+=5
    print('reference of list inside function',id(list2))
#end of function
list1=[10,20,30,40,50]
print("reference of list before the function call")
print(list1)
increment(list1)   #list1 is passed as  parameter to function
print("the list after the function call")
print(list1)











