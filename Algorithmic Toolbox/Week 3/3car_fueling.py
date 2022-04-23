d,m,n,li=[int(input()),int(input()),int(input()),list(map(int,input().split()))]
li.append(d)
li=list(set(li))
li.sort()
if d<m:
    print(0)
    quit()
if li[0]>m:
    print(-1)
    quit()

now=0
c=0
for i in range (0,len(li)):
    if i ==0:continue
    if li[i]-li[i-1]<=m:
        if li[i]-now>m:
            now=li[i-1]
            c+=1
            if now>=d:
                print(c)
                quit()
    else:
        print(-1)
        quit()
print(c)



