import numpy 
c=int(input())
l=[]
l.append(c/numpy.log(c))
l.append(1.25506*c/numpy.log(c))
new_list=[]
for i in l:
    new_list.append(round(i, 1))

new_list=map(str,new_list)
print(" ".join(new_list))