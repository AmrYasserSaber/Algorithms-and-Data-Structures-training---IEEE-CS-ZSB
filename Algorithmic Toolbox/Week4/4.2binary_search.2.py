def first(arr, low, high, x, n) :
    if(high >= low) :
        mid = low + (high - low) // 2
        if( ( mid == 0 or x > arr[mid - 1]) and arr[mid] == x) :
            return mid
        elif(x > arr[mid]) :
            return first(arr, (mid + 1), high, x, n)
        else :
            return first(arr, low, (mid - 1), x, n)
     
    return -1
         
         
n = int(input())
arr = list(map(int,input().split(" ")))
j= int(input())
search_num=list(map(int,input().split(" ")))
for x in search_num:
    left, right = 0, n-1
    print(first(arr, 0, n - 1,x, n), end = ' ')