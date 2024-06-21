def makefile():
    '''store rollno, Name and Marks in a Text file sdetails.txt'''
    file=open("sdetails.txt",'w')
    for i in range (5):
        rn=int(input("Enter your roll number:"))
        name=input("Entr your name:")
        marks=int(input("Enter marks:"))
        row=str(rn)+','+ name +','+str(marks)
        file.write(row+'\n')
    file.close()
makefile()
               
