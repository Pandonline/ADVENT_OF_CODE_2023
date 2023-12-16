
def defColN(Map,c):
    l = []
    for i in range(len(Map)):
        l.append(Map[i][c])
    return l

def UndefColN(Map,c,l):
    for i in range(len(Map)):
        Map[i][c] = l[i]
    return Map

def defColS(Map,c):
    l = []
    for i in range(len(Map)):
        l.append(Map[len(Map)-1-i][c])
    return l

def UndefColS(Map,c,l):
    for i in range(len(Map)):
        Map[len(Map)-1-i][c] = l[i]
    return Map

def defLineW(Map,l):
    c = []
    for i in range(len(Map[l])):
        c.append(Map[l][i])
    return c

def UndefLineW(Map,l,c):
    for i in range(len(Map[l])):
        Map[l][i] = c[i]
    return Map

def defLineE(Map,l):
    c = []
    for i in range(len(Map[l])):
        c.append(Map[l][len(Map[l])-1-i])
    return c

def UndefLineE(Map,l,c):
    for i in range(len(Map[l])):
        Map[l][len(Map[l])-1-i] = c[i]
    return Map

CACHE = {}

def moveLine(l):
    for i in range(len(l)):
        if l[i] == 'O':
            j = i-1
            while j >= 0 and l[j] =='.':
                l[j] = 'O'
                l[j+1] = '.'
                j -= 1
    return l

def lineValue(MAP,l,v):
    sum = 0
    for i in MAP[l]:
        if i == 'O':
            sum += v
    return sum

in_loop = False
input = open("input.txt")
MAP = []
for L in input.readlines():
    line = []
    for l in L.strip("\n"):
        line.append(l)
    MAP.append(line)

list = []
subList = []
for k in range(1000):
        in_loop = False

        for c in range(len(MAP)):
            MAP = UndefColN(MAP,c,moveLine(defColN(MAP,c)))

        for l in range(len(MAP[0])):
            MAP = UndefLineW(MAP,l,moveLine(defLineW(MAP,l)))
            
        for c in range(len(MAP)):
            MAP = UndefColS(MAP,c,moveLine(defColS(MAP,c)))
            
        for l in range(len(MAP[0])):
            MAP = UndefLineE(MAP,l,moveLine(defLineE(MAP,l)))
    
            sum = 0
        for i in range(len(MAP)):
            sum += lineValue(MAP,len(MAP)-1-i,i+1)
            
        if len(subList) > 2:
            if subList[0] == sum:
                break
        if sum in list:
            subList.append(sum)
        else:
            subList = []
        list.append(sum)
print(subList)
print(list)
newS = 1000000000-len(list)
print(subList[ newS-(newS//len(subList))*len(subList) -1 ])