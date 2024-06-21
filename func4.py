#EXAMPLE 30
def multi(**p):
    print(type(p))
    print(p)
    for k,v in p.items():
        print(k,"->",v)
multi(name="suraj",fee=3000,type="guest")
s={"ino":11,'item':'pen','qty':40}
multi(stock=s)
