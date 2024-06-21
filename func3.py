#EXAMPLE 29
def getpoints(p,**e):
    print('e=',e)
    if(type(e.get("level1"))==int and e["level"]%5==0):
        p=p+10
        print("awarded:",p,"pointds")
    if e["bonus"]=="yes":
        p+=p
        print("awarded:",p,"points")
    return p
p=0
p=getpoints(p,level=2,bonus="yes")
p=getpoints(p,level=5,bonus='no')
p=getpoints(p,level=10,bonus='yes')
p=getpoints(p,bonus='yes')
