num_of_wires=int(input())
num_of_birds=list(map(int,(input().split())))
num_of_shots=int(input())
def shots(num_of_birds,coordinates):
    if num_of_wires==1:
        num_of_birds[coordinates[0]-1]=0
        return
    if coordinates[0]-1>0 and coordinates[0]<num_of_wires:
        num_of_birds[coordinates[0]]+=num_of_birds[coordinates[0]-1]-coordinates[1]
        num_of_birds[coordinates[0]-2]+=coordinates[1]-1
        num_of_birds[coordinates[0]-1]=0
    elif coordinates[0]==1:
        num_of_birds[coordinates[0]]+=num_of_birds[coordinates[0]-1]-coordinates[1]
        num_of_birds[coordinates[0]-1]=0
    else:
        num_of_birds[coordinates[0]-2]+=coordinates[1]-1
        num_of_birds[coordinates[0]-1]=0
for i in range(0,num_of_shots):
    coordinates=list(map(int,(input().split())))
    shots(num_of_birds,coordinates)
for i in num_of_birds:
    print(i)