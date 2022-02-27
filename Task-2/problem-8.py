skill=list(map(int,(input().split())))[1]
problems=list(map(int,(input().split())))
right0=0
left0=len(problems)-1
counter1=0
while right0 - left0!=1 :
    if problems[right0]<=skill :
        right0+=1
        counter1+=1
    elif problems[left0]<=skill :
        left0-=1
        counter1+=1
    else:
        break
print(counter1)