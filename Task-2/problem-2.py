n=int(input())
list1=list(map(int,(input().split())))
time0=len(set(list1))
if 0 in list1:
    time0-=1 
print(time0)