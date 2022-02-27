pixels=list(map(int,(input().split())))
rows=pixels[0]
columns=pixels[1]
matrix0=[]
color0=False
for i in range(0,rows):
    matrix0.append(list((input().split())))
for i in matrix0:
    if "C" in i or 'M' in i or 'Y' in i:
        color0=True
        break
if color0==True:
    print("#Color")
else:
    print("#Black&White")
