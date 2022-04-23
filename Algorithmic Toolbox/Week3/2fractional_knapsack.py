n, capacity = [int(i) for i in input().split()]
lst = []

if capacity == 0:
    print(0)
    quit()

for j in range(n):
    v, w =  [int(i) for i in input().split()]
    if v == 0:
        continue
    lst.append((v, w))

lst.sort(key = lambda x: x[0]/x[1], reverse = True)

total_value = 0

for v,w in lst:
    if capacity==0:
        print(total_value)
        quit()
    loot = min(w, capacity)
    total_value += loot*v/w
    capacity -= loot

print(total_value)
