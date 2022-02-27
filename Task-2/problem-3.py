n=int(input())
list0=list(map(int,(input().split())))
Sereja=0
Dima=0
list1=[]
left0=0
right0=0
for i in range (0,n):
    if list0[0+right0]>list0[n-left0-1]:
        list1.append(list0[right0])
        right0+=1
    else:
        list1.append(list0[len(list0)-left0-1])
        left0+=1
for i in range(0,len(list1)):
    if i%2==0:
        Sereja+=list1[i]
    else:
        Dima+=list1[i]
print(str(Sereja)+" "+str(Dima))