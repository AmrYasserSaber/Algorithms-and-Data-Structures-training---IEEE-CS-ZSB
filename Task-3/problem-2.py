n=int(input())
list0=input().split("W")
list1=[]
r=0
for i in list0:
    if len(i)!=0:
        list1.append(len(i))
if 0 in list1:
    list1.remove(0)
print(len(list1))
if len(list1)!=0:
    print(" ".join(map(str,list1)))