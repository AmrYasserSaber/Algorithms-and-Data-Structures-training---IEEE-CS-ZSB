n=int(input())
stones=list(input())
taken0=0
for i in range(1,len(stones)):
    if stones[i]==stones[i-1]:
        taken0+=1
print(taken0)