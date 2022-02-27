n=int(input())
points=list(map(int,(input().split())))
result0=0
min0=points[0]
max0=points[0]
for i in range(0,len(points)):
    if i !=0:
        if points[i]<min0:
            min0=points[i]
            result0+=1
        if points[i]>max0:
            max0=points[i]
            result0+=1
print(result0)
