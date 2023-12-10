import sys

def drawLine(MAP,MAP_value,position):
    value = 1
    while not MAP_value[position[0]][position[1]] == value:
        print(value)
        if MAP_value[position[0]][position[1]] == '.' or MAP_value[position[0]][position[1]] > value:
            MAP_value[position[0]][position[1]] = value
        
        match ( MAP[position[0]][position[1]] ) :
            case '|':
                if position[0] > 0:
                    if MAP_value[position[0]-1][position[1]] == '.' or MAP_value[position[0]-1][position[1]] > value:
                        Nposition = (position[0]-1,position[1])
                        value = value+1
                if position[0] < len(MAP)-1:
                    if MAP_value[position[0]+1][position[1]] == '.' or MAP_value[position[0]+1][position[1]] > value:
                        Nposition = (position[0]+1,position[1])
                        value = value+1
                position = Nposition
            case '-':
                if position[1] > 0:
                    if MAP_value[position[0]][position[1]-1] == '.' or MAP_value[position[0]][position[1]-1] > value:
                        Nposition = (position[0],position[1]-1)
                        value = value+1
                if position[1] < len(MAP)-1:
                    if MAP_value[position[0]][position[1]+1] == '.' or MAP_value[position[0]][position[1]+1] > value:
                        Nposition = (position[0],position[1]+1)
                        value = value+1
                position = Nposition
            case 'L':
                if position[0] > 0:
                    if MAP_value[position[0]-1][position[1]] == '.' or MAP_value[position[0]-1][position[1]] > value:
                        Nposition = (position[0]-1,position[1])
                        value = value+1
                if position[1] < len(MAP)-1:
                    if MAP_value[position[0]][position[1]+1] == '.' or MAP_value[position[0]][position[1]+1] > value:
                        Nposition = (position[0],position[1]+1)
                        value = value+1
                position = Nposition
            case 'J':
                if position[0] > 0:
                    if MAP_value[position[0]-1][position[1]] == '.' or MAP_value[position[0]-1][position[1]] > value:
                        Nposition = (position[0]-1,position[1])
                        value = value+1
                if position[1] > 0:
                    if MAP_value[position[0]][position[1]-1] == '.' or MAP_value[position[0]][position[1]-1] > value:
                        Nposition = (position[0],position[1]-1)
                        value = value+1
                position = Nposition
                
            case '7':
                if position[0] < len(MAP)-1:
                    if MAP_value[position[0]+1][position[1]] == '.' or MAP_value[position[0]+1][position[1]] > value:
                        Nposition = (position[0]+1,position[1])
                        value = value+1
                if position[1] > 0:
                    if MAP_value[position[0]][position[1]-1] == '.' or MAP_value[position[0]][position[1]-1] > value:
                        Nposition = (position[0],position[1]-1)
                        value = value+1
                position = Nposition
                
            case 'F':
                if position[0] < len(MAP)-1:
                    if MAP_value[position[0]+1][position[1]] == '.' or MAP_value[position[0]+1][position[1]] > value:
                        Nposition = (position[0]+1,position[1])
                        value = value+1
                if position[1] < len(MAP)-1:
                    if MAP_value[position[0]][position[1]+1] == '.' or MAP_value[position[0]][position[1]+1] > value:
                        Nposition = (position[0],position[1]+1)
                        value = value+1
                position = Nposition
                

    return MAP_value   

def findMax(MAP):
    MAX = 0
    for l in MAP:
        for p in l:
            if not p == '.' and p > MAX:
                MAX = p
    return MAX

def Orecur(MAP,x,y):
    if x >= 0 and x < len(MAP) and y >= 0 and y < len(MAP):
        MAP[x][y] = 'O'
        if x > 0 and MAP[x-1][y] == '.':
            MAP = Orecur(MAP,x-1,y)
        if x < len(MAP)-1 and MAP[x+1][y] == '.':
            MAP = Orecur(MAP,x+1,y)
        if y > 0 and MAP[x][y-1] == '.':
            MAP = Orecur(MAP,x,y-1)
        if y < len(MAP)-1 and MAP[x][y+1] == '.':
            MAP = Orecur(MAP,x,y+1)
    return MAP
    

input = open("input.txt")
MAP = []
MAP_value = []
position_init = (0,0)
i = 0
for L in input.readlines():
    line = []
    line_value = []
    j = 0
    for l in L.strip("\n"):
        if l == 'S':
            position_init = (i,j)
        line_value.append('.')
        line.append(l)
        j = j+1
    MAP.append(line)
    MAP_value.append(line_value)
    i = i+1

MAP_value[position_init[0]][position_init[1]] = 0

if position_init[0] > 0 and MAP[position_init[0]-1][position_init[1]] in ['|','7','F']:
    MAP_value = drawLine(MAP,MAP_value,(position_init[0]-1,position_init[1]))
if position_init[0] < len(MAP)-1 and MAP[position_init[0]+1][position_init[1]] in ['|','J','L']:
    MAP_value = drawLine(MAP,MAP_value,(position_init[0]+1,position_init[1]))
if position_init[1] > 0 and MAP[position_init[0]][position_init[1]-1] in ['-','L','F']:
    MAP_value = drawLine(MAP,MAP_value,(position_init[0],position_init[1]-1))
if position_init[1] < len(MAP)-1 and MAP[position_init[0]][position_init[1]+1] in ['-','7','J']:
    MAP_value = drawLine(MAP,MAP_value,(position_init[0],position_init[1]+1))


output = open("MAP_simplifier.txt",'w')
for i in range(len(MAP)):
    line = ""
    for j in range(len(MAP[i])):
        if MAP_value[i][j] == '.':
            line = line + '.'
        else:
            line = line+MAP[i][j]
    output.write(line+"\n")
output.close()
    
Big_output = open("MAP_Exploser.txt",'w')
for L in open("MAP_simplifier.txt").readlines():
    line1 = ""
    line2 = ""
    line3 = ""
    for l in L.strip("\n"):
        match(l):
            case '.':
                line1 = line1 + "..."
                line2 = line2 + "..."
                line3 = line3 + "..."
            case '-':
                line1 = line1 + "..."
                line2 = line2 + "---"
                line3 = line3 + "..."
            case '|':
                line1 = line1 + ".|."
                line2 = line2 + ".|."
                line3 = line3 + ".|."
            case 'L':
                line1 = line1 + ".|."
                line2 = line2 + ".L-"
                line3 = line3 + "..."
            case 'J':
                line1 = line1 + ".|."
                line2 = line2 + "-J."
                line3 = line3 + "..."
            case '7':
                line1 = line1 + "..."
                line2 = line2 + "-7."
                line3 = line3 + ".|."
            case 'F':
                line1 = line1 + "..."
                line2 = line2 + ".F-"
                line3 = line3 + ".|."
            case 'S':
                line1 = line1 + ".|."
                line2 = line2 + "-S-"
                line3 = line3 + ".|."
    Big_output.write(line1+"\n")
    Big_output.write(line2+"\n")
    Big_output.write(line3+"\n")
Big_output.close()

newMap = open("MAP_exploser.txt")
MAP_EXP = []
for L in newMap.readlines():
    line = []
    for l in L.strip("\n"):
         line.append(l)
    MAP_EXP.append(line)

sys.setrecursionlimit(1000000)
MAP_EXP = Orecur(MAP_EXP,0,0)

for i in range(len(MAP_EXP)):
    for j in range(len(MAP_EXP[i])):
        if MAP_EXP[i][j] == '.':
            MAP_EXP[i][j] = 'I'

output = open("MAP_exploser_withair.txt",'w')
for i in range(len(MAP_EXP)):
    line = ""
    for j in range(len(MAP_EXP[i])):
        line = line+MAP_EXP[i][j]
    output.write(line+"\n")
output.close()

output = open("MAP_simplifier_withair.txt",'w')
for i in range(len(MAP)):
    line = ""
    for j in range(len(MAP[i])):
        line = line+MAP_EXP[3*i+1][3*j+1]
    output.write(line+"\n")
output.close()