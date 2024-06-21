#EXAMPLE 28
def disp(**detail):
    print("detail1=",detail)
    for k,v in detail.items():
        print(k,"->",v)
q={'name':10,'scorw':[12,34]}
disp(q=q)
disp(q1='priya',q2=45,q3=[23,56],q4=34.5)
