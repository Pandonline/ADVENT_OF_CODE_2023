def verifSymetrieLine(MAP,l1,l2,start,smudge):
    if  l1 < 0 or  l2 >= len(MAP):
        if not smudge == 0:
            return 0
        return start
    for j in range(len(MAP[0])):
        if not MAP[l1][j] == MAP[l2][j]:
            if smudge > 0:
                smudge -= 1
            else:
                return 0
    return verifSymetrieLine(MAP,l1-1,l2+1,start,smudge)

def verifSymetrieCol(MAP,c1,c2,start,smudge):
    if  c1 < 0 or  c2 >= len(MAP[0]):
        if not smudge == 0:
            return 0
        return start
    for i in range(len(MAP)):
        if not MAP[i][c1] == MAP[i][c2]:
            if smudge > 0:
                smudge -= 1
            else:
                return 0
    return verifSymetrieCol(MAP,c1-1,c2+1,start,smudge)
                

def findSymetrie(MAP):
    nbLine = 0
    nbColonne = 0
    for i in range(len(MAP)-1):
        nbLine += verifSymetrieLine(MAP,i,i+1,i+1,1)
    for j in range(len(MAP[0])-1):
        nbColonne += verifSymetrieCol(MAP,j,j+1,j+1,1)
    return 100*nbLine+nbColonne


input = open("input.txt")
map = []
sum = 0
for L in input.readlines():
    if len(L) > 2:
        line = []
        for l in L.strip("\n"):
            line.append(l)
        map.append(line)
    if len(L) < 2 or L.find('\n') == -1:
        sum += findSymetrie(map)
        map = []
print(sum)
    