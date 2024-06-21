#to input students name and their roll_numbers and marks in different subjects
num=int(input("enter the number of person whose record is to be stored:"))
count=1
person=dict()
while count<=num:
    name=input("enter your name: ")
    roll_no=int(input("enter your roll_no. "))
    maths=int(input("enter the marks in maths"))
    english=int(input("enter the marks in english"))
    physics=int(input("enter the marks in physics"))
    chemistry=int(input("enter the marks in chemistry"))
    computer_science=int(input("enter the marks in computer_science"))
    person[name]=roll_no
    count+=1
print("\n\nPERSON_NAME\troll_no.")
for k in person:
    print(k,'\t\t',person[k])
