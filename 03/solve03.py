gearbox = []

with open("AdventOfCode_2023/03/miniinput.txt", 'r') as f:
        for line in f.readlines():
            line = list(line)
            gearbox.append(line[:-1])


#Part A 
non_symbol = ['.','1','2','3','4','5','6','7','8','9','0']
m,n = len(gearbox[0]),len(gearbox)

output_sum = 0
for i in range(m):
    for j in range(n):
        if gearbox[i][j].isdigit() == False and gearbox[i][j] is not '.':
            neigh1 = int(gearbox[i-1][j-1].isdigit())
            neigh2 = int(gearbox[i][j-1].isdigit())
            neigh3 = int(gearbox[i+1][j-1].isdigit())
            neigh4 = int(gearbox[i-1][j].isdigit())
            neigh5 = int(gearbox[i+1][j].isdigit())
            neigh6 = int(gearbox[i-1][j+1].isdigit())
            neigh7 = int(gearbox[i][j+1].isdigit())
            neigh8 = int(gearbox[i+1][j+1].isdigit())
            neigh_num = neigh1 + neigh2 + neigh3 + neigh4 + neigh5 + neigh6 + neigh7 + neigh8
            if(neigh_num > 0):
                output_sum += symbol_sum(i,j,neigh_num)
                
        

def symbol_sum(i,j,num):
    pass
