str=input("enter any sentence")
d=0
u=0
l=0
w=0
for ch in str:
    if ch.islower():
        l+=1
    if ch.isupper():
        u+=1
    if ch.isdigit():
        d+=1
    if ch=='':
        w+=1
print("\nTotal Upper case alphabets are:",u)
print("\nTotal Lower case alphabets are:",l)
print("\nTotal Digits are:",d)
print("\Total Words are:",w+1)
