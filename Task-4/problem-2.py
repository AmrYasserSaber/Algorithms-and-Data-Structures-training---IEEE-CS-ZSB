def lexNext(s, n):
    for i in range(n - 1, -1, -1):
        if s[i] != 'z':
            k = ord(s[i])
            s[i] = chr(k + 1)
            return ''.join(s)
        s[i] = 'a'


if __name__ == "__main__":
    S = input()
    T = input()
    n = len(S)
 
    S = list(S)
    res = lexNext(S, n)
    if res != T:
        print(res)
    else:
        print("No such string")