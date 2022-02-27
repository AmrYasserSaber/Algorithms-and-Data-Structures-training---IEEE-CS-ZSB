stones=list(input())
instructions=list(input())
stone=0
for i in instructions:
    if stones[stone]==i:
        stone+=1
print(stone+1)