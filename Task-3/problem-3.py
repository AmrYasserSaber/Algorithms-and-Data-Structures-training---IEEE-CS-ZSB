n=int(input())
l=list(input())
if l.count("A")>l.count("D"):
    print("Anton")
elif l.count("A")<l.count("D") :
    print("Danik")
else:
    print("Friendship")