import sys

def binary_search(a, x, left, right):
    r = -1
    if left <= right:
        mid = int((left + right)/2)
        if x > a[mid]:
            left = mid + 1
            r = binary_search(a, x, left, right)
        elif x < a[mid]:
            right = mid - 1
            r = binary_search(a, x, left, right)
        else:
            r = mid
    return r

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split(" ")))
    m =int(input())
    search_num = list(map(int,input().split(" "))) 
    
    for x in search_num:
        left, right = 0, n-1
        print(binary_search(a, x, left, right), end = ' ')
