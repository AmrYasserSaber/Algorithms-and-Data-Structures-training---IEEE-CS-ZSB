# Uses python3
def get_change(m):
    x=(m//10)
    y=((m%10)//5)
    z=((m%10)%5)


    r=x+y+z
    return r

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
