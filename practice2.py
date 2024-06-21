#to print numbers from a given list greater than 6
list1=["hello","friends",int,float,1,2,34,5,4,7,89,45,11,6,-1,-22]
for items in list1:
    if str(items).isnumeric() and items>6:
        print(items)
        
