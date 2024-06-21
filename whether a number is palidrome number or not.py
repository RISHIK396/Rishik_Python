# to find that a string is a palidrome or not
str1=input("enter any string to be checked: ")
if(str1==str1[::-1]):
    print("the string is palidrome")
else:
    print("the string is not a palidrome")
