#EXAMPLE 16
G=100
def function1():
    global G
    G+=20
    print(G)
print(G)
G+=10
print(G)
function1()
print(G)
