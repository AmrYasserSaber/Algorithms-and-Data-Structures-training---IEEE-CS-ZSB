n=input().split("/")
for i in range(0,n.count('')):
    n.remove('')
print("/"+"/".join(n))