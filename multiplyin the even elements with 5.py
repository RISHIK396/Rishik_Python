#to enter a list and multiply the the even elements with 5
list1=[1,2,3,56,78,4,8,10,11,15,16,17,19,18,22,25,27]
print("list1 is",list1)
for items in list1:
    if str(items).isnumeric() and items%2==0:
        print(items*5)
    
