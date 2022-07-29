def perfect(n,l=[]):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if (n%3==0 and n%2 ==0) :
            x=min(len(perfect(n//3)),len(perfect(n//2)))
            if x == len(perfect(n//3)):
                n = n//3
            else:
                n=n//2
        elif (((n-1)%3==0) and n%2==0):
            r=min(len(perfect(((n-1)))),len(perfect(n//2)))
            if r==len(perfect((n-1))):
                n=(n-1)
            else:
                n=n//2
        elif n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    sequence=reversed(sequence)
    return(list(sequence))
input0 = int(input(" "))
sequence = list(perfect(input0))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
