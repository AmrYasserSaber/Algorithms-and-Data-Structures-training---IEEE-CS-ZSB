#Uses python3
def lcs2(a, b):
    index0=0
    c=0
    for i in range (0,len(b)):
        if b[i] in a[index0:]:   
            index0=a.index(b[i])
            c+=1
        
    return c

if __name__ == '__main__':
    x=int(input())
    data0 = list(map(int, input().split()))
    k=int(input())
    data1=list(map(int, input().split()))
if k==max(x,k):
    print(lcs2(data1, data0))
else:
    print(lcs2(data0, data1))
    
