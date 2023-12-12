import sys

def tabDistance(MAP,position,val):
    if position[0] >=0 and position[0] < len(MAP) and position[1] >=0 and position[1] < len(MAP[position[0]]):
        if MAP[position[0]][position[1]] == '.' or MAP[position[0]][position[1]] > val:
            MAP[position[0]][position[1]] = val
            MAP = tabDistance(MAP,(position[0]-1,position[1]),val+1)
            MAP = tabDistance(MAP,(position[0]+1,position[1]),val+1)
            MAP = tabDistance(MAP,(position[0],position[1]-1),val+1)
            MAP = tabDistance(MAP,(position[0],position[1]+1),val+1)
        return MAP
    else:
        return MAP
    

def findGalaxy(MAP):
    position = []
    for i in range(len(MAP)):
        for j in range(len(MAP[i])):
            if not MAP[i][j]=='.':
                position.append((i,j))
    sum = 0
    for p in range(len(position)):
        print(p)
        EMPTY_MAP = []
        for i in range(len(MAP)):
            EMPTY_LINE = []
            for j in range(len(MAP[i])):
                EMPTY_LINE.append('.')
            EMPTY_MAP.append(EMPTY_LINE)
        TAB = tabDistance(EMPTY_MAP,position[p],0)
        for q in range(p+1,len(position)):
            sum = sum + TAB[position[q][0]][position[q][1]]
    print(sum)
    
sys.setrecursionlimit(1000000)
input = open("input.txt").readlines()
listLig = []
i = 0
listCol = []
j = 0
for L in input:
    if(i == 0):
        listCol = list(range(len(L.strip("\n"))))
    if not '#' in L:
        listLig.append(i)
    i = i + 1
    for l in range(len(L.strip("\n"))):
        if L[l] == '#' and l in listCol:
            listCol.pop(listCol.index(l))

print(listLig)
print(listCol)

univ_extend = []
i=0
val = 0
for L in input:
    s = []
    j = 0
    for l in L.strip("\n"):
        if l == '#':
            val = val+1
            s.append(val)
        else:
            s.append('.')
            if j in listCol:
                s.append('.')
        j = j+1
    univ_extend.append(s)
    if i in listLig:
        univ_extend.append(s)
    i= i+1
findGalaxy(univ_extend)
