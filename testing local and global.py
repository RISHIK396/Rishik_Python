#EXAMPLE 14
G=10
def test():
    l=G+20 #LOCAL VARIABLE
    print("local:" ,l)
print("main:",G)
G+=30
test()
print("main:",G)
