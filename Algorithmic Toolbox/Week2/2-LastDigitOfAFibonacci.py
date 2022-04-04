def fibonacci2(n):
    n1 = 0
    n2 = 1
    for index in range(num - 1):
        sum = (n1 + n2) % 10
        n1 = n2
        n2 = sum
    sum = str(sum)
    return int(sum[-1])

num = int(input())
print(fibonacci2(num))