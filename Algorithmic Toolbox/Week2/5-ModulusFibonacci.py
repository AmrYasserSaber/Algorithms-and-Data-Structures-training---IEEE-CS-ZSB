def pisano(n):
    previous, current = 0, 1

    for index in range(n * n):
        previous, current \
        = current, (previous + current) % n
        if previous == 0 and current == 1:
            return index + 1

def fibonacci1(n):
    if n == 1:
        return 1
    n1 = 0
    n2 = 1
    sum = 0
    for index in range(n - 1):
        sum = n1 + n2
        n1 = n2
        n2 = sum
    return sum

def result(n, m):
    pisano1 = pisano(m)
    reminder = n % pisano1
    result1 = fibonacci1(reminder) % m
    return result1

n, m = input().split()
n = int(n)
m = int(m)
print(result(n, m))