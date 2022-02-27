n=int(input())
row=[]
chess=[]
if n!=0:
    if n%2==0:
        maximum_number_of_Coders=(n**2)//2
    else:
        maximum_number_of_Coders=(n*((n//2)+1))-(n//2)
    for c in range(0,n):
        row=[]
        for r in range(0,n):
            if (c+r)%2==0:
                row.append("C")
            else:
                row.append(".")
        chess.append(row)
    print(maximum_number_of_Coders)
    for i in chess:
        print("".join(i))
else:
    (print(0))
