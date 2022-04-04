def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return (a // gcd(a, b) * b)


a, b = input().split()
a, b = int(a), int(b)
print(lcm(a, b))