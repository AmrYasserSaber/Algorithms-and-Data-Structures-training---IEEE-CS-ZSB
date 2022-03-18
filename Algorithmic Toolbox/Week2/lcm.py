# Uses python3
""""def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b"""
def lcm_naive(a, b):
    s=0
    for i in range(1,min(a,b)):
        if a%i==0 and b%i==0:
            if i>s:
                s=i
    return(a*b//s)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm_naive(a, b))

