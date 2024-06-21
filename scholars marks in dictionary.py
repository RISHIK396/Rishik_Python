#EXAMPLE 8
def scholars(ST):
    s={}
    for k,v in ST.items():
        if v>=90:
            s[k]=v
    return s
s1={"Anu":67,"Raj":98,"Ken":45,"Ram":92}
sr1=scholars(s1)
print(s1)
print(sr1)
