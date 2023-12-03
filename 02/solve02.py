
f = open("AdventOfCode_2023/02/input.txt","r")
lines = f.readlines()
summe = 0
RED_LIM, GREEN_LIM, BLUE_LIM = 12,13,14

for l in lines:
    
    
    ids,cubes_org = l.split(":")
    iden = int(ids[5:])
    
    sets = cubes_org.split(";")
    
    impossible_game = False
    for sete in sets:
        print(sete)
        red,green,blue = 0,0,0
        cubes = sete.split(" ")
        for i in range(len(cubes)):
            if cubes[i].startswith("blue"):
                blue = int(cubes[i-1])
            elif cubes[i].startswith("red"):
                red = int(cubes[i-1])
            elif cubes[i].startswith("green"):
                green = int(cubes[i-1])
        if red > RED_LIM or green > GREEN_LIM or blue > BLUE_LIM:
            impossible_game = True
        #print(red,green,blue)
        #assert False
    if impossible_game == False:
        summe += iden
print(summe)