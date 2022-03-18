import random
def slowway(l):
    r=1
    for i in range(0,len(l)):
        for j in range(0,len(l)):
            if (l[i])*(l[j])> r and i!=j:
                r=l[i]*l[j]
    return(r)
def  fastway(l):
    m1=max(l)
    l.remove(m1)
    m2=max(l)
    return m1*m2
while True:
    list0=[]
    length0=random.randint(2,50)
    for i in range(0,length0):
        list0.append(random.randint(1,100))
    slow0=slowway(list0)
    fast0=fastway(list0)
    if fast0==slow0:
        print("YES")
        print(list0)
        print("slow {}".format(slow0))
        print("fast {}".format(fast0))
    else:
        print("NO")
        print(list0)
        print("slow {}".format(slow0))
        print("fast {}".format(fast0))
        break
        