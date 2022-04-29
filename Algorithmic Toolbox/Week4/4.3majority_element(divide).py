n = int(input())
seq = list(map(int,input().split()))


def divide_func(seq, left, right):
    if left+1==right:
        return seq[left]
    elif left+2==right:
        return seq[left]
    m = (left+right)//2
    left = divide_func(seq, left, m)
    right = divide_func(seq, m, right)

    c1, c2 = 0, 0
    for i in seq[left:right]:
        if i == left:
            c1+=1
        elif i == right:
            c2+=1
    if c1>(right-left)//2 and left != -1:
        return left
    elif c2>(right-left)//2 and right != -1:
        return right
    else: 
        return -1

print(int(divide_func(seq, 0, n) != -1))