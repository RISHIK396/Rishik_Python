# to create a binary file
def make():
    '''store roll no., name  and marks of 5 students in a file, s details.txt'''
    with open('sdetails.txt','w'):
        for i in range(5):
            rn=int(input("enter tyour roll number:"))
            name=input("enter your name:")
            marks=int(input("enter your marks:"))
            row=(str(rn)+name+str(marks)+'\n')
            file.writelines(row)
makefile()
