def optimal_weight(C,v, n):
    v.insert(0,0)
    t=[[0 for i in range(C + 1)] for j in range(n + 1)]
    for i in range(0,n+1):
        if i == 0 :
            continue
        for j in range (0,C+1):
            if j==0:
                continue
            if v[i]>j:
                t[i][j]=t[i-1][j]
            else:
                t[i][j]=max(t[i-1][j],t[i-1][j-v[i]]+v[i])
    if  t[n][C]<C:
        return 0
    i=n 
    j=C
    l=[]
    for i in range(n,0,-1):
        if t[i][j]>t[i-1][j]:
            l.append(v[i])
            j-=v[i]
    return l
if __name__ == '__main__':
    sum0=0
    b=int(input())
    w=[int(x) for x in input().split()]
    for i in range (0,len(w)):
        sum0+=w[i]
        if sum0%3==0:
            W=sum0//3
        else:
            print(0)
            exit()
    for i in range (0,3):
        temp=optimal_weight(W,w,len(w))
        if (temp)==0:
            print(0)
            exit()
        else:
            for i in range (0,len(temp)):
                w.remove(temp[i])
    print(1)

