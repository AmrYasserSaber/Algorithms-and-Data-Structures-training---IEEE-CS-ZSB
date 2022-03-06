n=list(map(int,(input().split())))
last_page=n[0]
range0=n[2]
currant_page=n[1]
result0=["({})".format(currant_page)]
for i in range(1,range0+1):
    if currant_page-i>=1:
        result0.insert(0,currant_page-i)
    if currant_page+i<=last_page:
        result0.append(currant_page+i)
result0.append(">>")
result0.insert(0,"<<")
if 1 in result0 or currant_page==1:
    result0.remove("<<")
if last_page in result0 or last_page==currant_page:
    result0.remove(">>")
print(" ".join(map(str,result0)))