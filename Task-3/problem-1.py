n=int(input())
space=False
r=[]
for g in range(0,n):
        r.append(input().split("|"))

for i in range(0,n):
    for j in range (0,len(r[i])):
        if r[i][j]=="OO":
            r[i][j]="++"
            space=True
            break
    if r[i][j]=="++":
            break
if space==True:
    print("YES")
    for i in r:
        print("|".join(i))
else:
    print("NO")