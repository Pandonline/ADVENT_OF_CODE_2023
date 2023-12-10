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

print(findMax(MAP_value))