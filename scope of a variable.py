#EXAMPLE 17
G=10
def test1():
    G=20
    print("test1 G:",G)
def test2():
    G=30
    print("test2 G:",G)
print("main G:",G)
G+=5
test1()
print("main G:",G)
G+=10
test2()
print("main G:",G)
