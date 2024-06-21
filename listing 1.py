#write a python program to do various programs
l=[]
n=int(input("enter how many elements you want to add in the list ?"))
for i in range (1,1+n):
    add=input("enter the elemet you want to add:")
    l.append(add)

    print("list is :",l)

#b
pos=int(input("enter the position of the element to be deleted:"))
length=len(l)
if pos>length:
    print("invalid index number,max allowed is:",(length,n-1))
else:
    el=l.pop(pos)
    print("element",el,"was deleted")
print("modified list is",l)


#c
new_el=int(input("enter the element that you want to add in the list:"))
new_pos=int(input("enter the position where you want element to be inserted:"))
if new_pos>length:
    print("invalid index number,max allowed is:",(length,n-1))
else:
    l.insert(new_pos,new_el)
print("the modified list is:",l)
