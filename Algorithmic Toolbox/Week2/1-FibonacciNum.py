# not the best solution
def fibonacci(n):
    list1 = [0, 1]
    for index in range(n):
        list1.append(list1[index] + list1[index + 1])
        index += 1
    return list1[n]

# a good solution
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

n = int(input())

print(fibonacci1(n))