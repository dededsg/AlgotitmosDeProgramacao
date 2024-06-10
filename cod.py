x = [48,0,1,23,0,-2,-5,4,4564,0]

for i in range(10):
    if x[i] == None or x[i] <= 0 :
        x[i] = 1  
        print(f'X[{i}] = {x[i]}')
    else:
        print(f'X[{i}] = {x[i]}')