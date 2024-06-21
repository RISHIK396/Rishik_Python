n=int(input("Enter number of vertices: "))
check = True
print("Enter 1 if there is edge between vertex else enter 0\n")
ver=[]
represent=[]
for i in range(1,n+1):
    temp1=[]
    temp=[]
    for j in range(1,n+1):
        print(f"Enter edge for vertex {i} to {j}:",end=" ")
        e=int(input())
        if(i == j and e == 1):
            check = False
        if(e==1):
            temp1.append(tuple((i,j)))
        temp.append(e)
    ver.append(temp)
    represent.append(temp1)

for i in ver:
    if(sum(i) != n-1):
        check = False 
        break
if(check):
    print(f"\nThe given graph is complete k{n} graph\n")
else:
    print(f"\nThe given graph is not a complete graph\n")

print("Representing the graph using List Representation\n")
print("Vertex\t\t","List of Edges")
for i in range(1,n+1):
        print(i,end="\t\t")
        print(represent[i-1])
