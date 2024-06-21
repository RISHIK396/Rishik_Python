import csv
filename=input("enter the name of the file")
with open(filename,'r')as file:
    data=csv.reader(file)
    for row in data:
        print(row)
