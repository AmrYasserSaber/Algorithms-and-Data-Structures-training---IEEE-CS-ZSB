def max_dot_product(a, b):
    a.sort()
    b.sort()
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    n,a,b =[int(input()),list(map(int,input().split())),list(map(int,input().split()))]

    print(max_dot_product(a, b))
    
