input0=input().split("=")
right0=(input0[0].split("+"))
right1=list(right0[0])
right2=list(right0[1])
left0=list(input0[1])
right0_count=len(right1)+len(right2)
if abs(right0_count-len(left0))!=0 and abs(right0_count-len(left0)) != 2:
    print("Impossible")
else:
    if right0_count>len(left0):
        left0.append("|")
        if len(right1)>1:
            right1.remove("|")
        else:
            right2.remove("|")
    elif right0_count<len(left0):
        left0.remove("|")
        right1.append("|")
    print("".join(right1)+"+"+"".join(right2)+"="+"".join(left0))