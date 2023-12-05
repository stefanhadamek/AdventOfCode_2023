import numpy as np
import pandas as pd 

gearbox = []
def has_neigh(i,j,n,m):
    check =['*','+','=','%','-','#','@','/','&','$'] 
    #symbol index 
    
    if i>0 and j>0 and gearbox[i-1][j-1] in check:
        return True, (i-1,j-1)
    if i>0 and gearbox[i-1][j] in check:
        return True, (i-1,j)
    if i>0 and j<m-1 and gearbox[i-1][j+1] in check:
        return True, (i-1,j+1)
    if j>0 and gearbox[i][j-1] in check:
        return True, (i,j-1)
    #print(i,j,n,m, gearbox[i][j])
    #print(len(gearbox[138]))
    if j<m-1 and gearbox[i][j+1] in check:
        return True, (i,j+1)
    if i<n-1 and j>0 and gearbox[i+1][j-1] in check:
        return True, (i+1,j-1)
    if i<n-1 and gearbox[i+1][j] in check:
        return True, (i+1,j)
    if i<n-1 and j<m-1 and gearbox[i+1][j+1] in check:
        return True, (i+1,j+1)
    return False,(-1,-1)

with open("AdventOfCode_2023/03/input.txt", 'r') as f:
        for line in f.readlines():
            line = list(line)
            gearbox.append(line[:-1])

#A 
m,n = len(gearbox[0]),len(gearbox)

output_sum = 0
output_tracker = []
for i in range(m):
    current_status = False
    current_number = ''
    current_posx,current_posy =-1,-1
    for j in range(n):
        if gearbox[i][j].isdigit():
            current_number = current_number + gearbox[i][j]
            status,(pos_x,pos_y) = has_neigh(i,j,n,m)
            if status:
                current_status = True
                current_posx = pos_x
                current_posy = pos_y
                continue
        if gearbox[i][j] in ['.','*','+','=','%','-','#','@','/','&','$'] and current_number != '' and current_status == True:
            output_tracker.append((current_number,(current_posx,current_posy)))
            current_status = False
            current_posx,current_posy = -1,-1
            current_number = ''
        if gearbox[i][j] == '.' or gearbox[i][j] in ['*','+','=','%','-','#','@','/','&','$']:
            current_status = False
            current_posx,current_posy = -1,-1
            current_number = ''
        if j == m-1 and gearbox[i][j].isdigit() and current_number != '' and current_status == True:
            output_tracker.append((current_number,(current_posx,current_posy)))
            current_status = False
            current_posx,current_posy = -1,-1
            current_number = ''
for i in range(len(output_tracker)):
    output_sum += int(output_tracker[i][0])
#print(output_tracker)
print(output_sum)
df = pd.DataFrame(list(output_tracker))
df.columns = ['numbers', 'Index']
dff = df.groupby('Index')['numbers'].apply(list)
print(dff[0])
gear_sum_output = 0
for i in range(len(dff)):
    if(len(dff[i])==1):
        continue
    gear_sum_output+=int(dff[i][0])*int(dff[i][1])

print(gear_sum_output)