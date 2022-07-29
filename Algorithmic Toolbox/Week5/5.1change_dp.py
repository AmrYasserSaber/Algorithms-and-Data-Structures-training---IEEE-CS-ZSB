def get_change(m):
    if m%4==0:
        return m//4
    else:
        return(m//4+1)
m=int(input(""))
print(get_change(m))