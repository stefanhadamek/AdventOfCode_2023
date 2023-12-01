
f = open("AdventOfCode_2023/01/input.txt","r")
lines = f.readlines()
summe = 0
for l in lines:
    # twone, threeight,oneight,fiveight, sevenine, eightwo, eighthree, nineight
    #print("String before: ", l)
    #Blub9 => 9bluB
    #
    l = l.replace("one","o1e")
    l = l.replace("two","t2o")
    l = l.replace("three","t3e")
    l = l.replace("four","f4r")
    l = l.replace("five","f5e")
    l = l.replace("six","s6x")
    l = l.replace("seven","s7n")
    l = l.replace("eight","e8t")
    l = l.replace("nine","n9e")
    print("String after hehe: ",l)
    
    arr = ''.join(c for c in l if c.isdigit())
    #print(arr)
    first = int(arr[0])
    last = int(arr[-1])
    summe += first*10+last
    print("Just Iteration Sum: ",first*10+last)
    print("Summe: ",summe)
print(summe)

