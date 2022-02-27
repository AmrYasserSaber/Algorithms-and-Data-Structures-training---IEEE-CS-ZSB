num_of_pairs=int(input())
bag=list(map(int,(input().split())))
table=[]
max0=0
seen=[]
for sock in bag:
    if sock not in table:
        table.append(sock)
        if len(table)>max0:
            max0=len(table)
    else:
        table.remove(sock)
    if sock not in seen:
        seen.append(sock)
    if len(seen)==num_of_pairs:
        break
    
print(max0)