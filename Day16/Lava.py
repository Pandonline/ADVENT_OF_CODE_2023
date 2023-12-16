import sys

FLOOR = []
MAP = []
VALEUR = []

CACHE = {}

def addRay(i,j,d_i,d_j):
    position = '.'
    if d_i == 1:
        position = 'v'
    elif d_i == -1:
        position = '^'
    elif d_j == 1:
        position = '>'
    elif d_j == -1:
        position = '<'
    loop = (position in FLOOR[i][j])
    FLOOR[i][j] += position
    return loop



def recurBeam(i,j,d_i,d_j):
    if i >= 0 and i < len(MAP) and j >= 0 and j < len(MAP[0]):
        loop = addRay(i,j,d_i,d_j)
        if loop:
            return 0
        val = 0
        if len(FLOOR[i][j]) == 2:
            val = 1
            VALEUR[i][j] += 1
        match(MAP[i][j]):
            case '.':
                return recurBeam(i+d_i,j+d_j,d_i,d_j) + val
            case '/':
                d_i,d_j = -d_j,-d_i
                return recurBeam(i+d_i,j+d_j,d_i,d_j) + val
            case '\\':
                d_i,d_j = d_j,d_i
                return recurBeam(i+d_i,j+d_j,d_i,d_j) + val
            case '-':
                if d_i == 0:
                    return recurBeam(i+d_i,j+d_j,d_i,d_j) + val
                elif d_j == 0:
                    d_i = 0
                    return recurBeam(i+d_i,j+1,d_i,1) + recurBeam(i+d_i,j-1,d_i,-1) + val
            case '|':
                if d_j == 0:
                    return  recurBeam(i+d_i,j+d_j,d_i,d_j) + val
                elif d_i == 0:
                    d_j = 0
                    return recurBeam(i+1,j+d_j,1,d_j) + recurBeam(i-1,j+d_j,-1,d_j) + val
    return 0

def resetFloor():
    for k in range(len(MAP)):
        for p in range(len(MAP[0])):
            FLOOR[k][p] = "."
            VALEUR[k][p] = 0

input = open("input.txt")
for L in input.readlines():
    line = []
    lineFloor = []
    lineValeur = []
    for l in L.strip("\n"):
        line.append(l)
        lineFloor.append('.')
        lineValeur.append(0)
    MAP.append(line)
    FLOOR.append(lineFloor)
    VALEUR.append(lineValeur)
    
sys.setrecursionlimit(1000000)
find_max = 0
for i in range(len(MAP)):
    resetFloor()
    find_max = max(find_max,recurBeam(i,0,0,1))
    resetFloor()
    find_max = max(find_max,recurBeam(i,len(MAP[0])-1,0,-1))
    
for j in range(len(MAP[0])):
    resetFloor()
    find_max = max(find_max,recurBeam(0,j,1,0))
    resetFloor()
    find_max = max(find_max,recurBeam(len(MAP)-1,j,-1,0))
print(find_max)