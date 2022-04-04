def fibonacci(n):
    n1, n2 = 0, 1
    total = 1
    if n==0:
        return(0)
    else:
        for index in range(n - 1):
            sum = (n1 + n2) % 10
            n1 = n2
            n2 = sum
            total += sum
        total = str(total)
        return int(total[-1])


n = int(input())
print(fibonacci(n))