def convert(num):
    number_names = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    result=""
    for ch in num:
        key=int(ch)
        value=number_names[key]
        result=result+ value
    return result
num=input("enter the number:")
result=convert(num)
print("the number is:",num)
print("the number_names is:",result)
