n = input()
s = set()
i = 0
for x in input().split():
    s ^= {x}
    i = max(i, len(s))
print(i)
