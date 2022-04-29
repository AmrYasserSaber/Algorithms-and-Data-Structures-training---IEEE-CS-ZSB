numbreOfElements=int(input())
listOfInts=list(map(int,(input().split())))
insertedNum=listOfInts[numbreOfElements-1]

for i in range(numbreOfElements-1,-1,-1):
        if insertedNum<=listOfInts[i]:
            if listOfInts[i-1] >insertedNum:
                listOfInts[i]=listOfInts[i-1]
                if i!=0:
                    print(" ".join(map(str,listOfInts)))
                else:
                    listOfInts[0]=insertedNum
                    print(" ".join(map(str,listOfInts)))
                    break
        else:
            listOfInts[i+1]=insertedNum
            print(" ".join(map(str,listOfInts)))
            break