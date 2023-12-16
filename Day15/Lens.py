def getHASH(str):
    s = 0
    for i in str:
        s = ((s+ord(i))*17)%256
    return int(s)

def treatStr(box,str):
    if '-' in str:
        label = str.removesuffix("-")
        rmBox(box,label)
    else:
        label,value = str.split("=")
        addBox(box,(label,int(value)))
    return box

def addBox(box,tup):
    hash = getHASH(tup[0])
    for i in range(len(box[hash])):
        if box[hash][i][0] == tup[0]:
            box[hash].pop(i)
            box[hash].insert(i,tup)
            return box
    box[hash].append(tup)
    return box

def rmBox(box,label):
    hash = getHASH(label)
    for b in box[hash]:
        if b[0] == label:
            box[hash].remove(b)
    return box
    
input = open("input.txt")
list = []
for L in input.readlines():
    for l in L.strip("\n").split(","):
        list.append(l)

box = [[] for i in range(256)]
for i in list:
    box = treatStr(box,i)
    
sum = 0
for i in range(len(box)):
    for j in range(len(box[i])):
        sum += (1+i)*(j+1)*box[i][j][1]
print(sum)