#EXAMPLE 26
def multi(*p):
    print(type(p))
    for i in p:
        print(i)
multi(23)
multi(30,4,2,"amar")
