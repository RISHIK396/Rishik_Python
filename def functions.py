#EXAMPLE 6
def something(some_parameter):
    #some expression
    var1=(some_parameter)*5
    var2=(some_parameter)*3
    return var1,var2
p=input("enter some value ")
v1,v2=something(p)
print(v1)
print(v2)
v1,v2=something(50)
print(v1)
print(v2)
