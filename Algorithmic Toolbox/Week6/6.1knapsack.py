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
    return t[n][C]
if __name__ == '__main__':
    [W,n]=[int(x) for x in input().split()]
    w=[int(x) for x in input().split()]
    print(optimal_weight(W, w, n))
