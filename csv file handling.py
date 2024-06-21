import csv
with open("stationary.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["itemno","itemname","price"])
    writer.writerow(["A01","pencil",25])
    writer.writerow(["A02","Pen",75])
    writer.writerow(["A03","Eraser",15])
print("Data written to stationary.csv")
