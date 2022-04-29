
import math

def minimum_distance(n, arr):
    c={}
    for i in range (0,n) :
        if arr[i] in c:
            c[arr[i]]=(c.get(arr[i]))+1
            if c[arr[i]]>n/2:
                return(1)
        else:
            c[arr[i]]=1
    return(0)
        



n = int(input())

arr =list(map(int,input().split(" "))) 

print(minimum_distance(n, arr))
