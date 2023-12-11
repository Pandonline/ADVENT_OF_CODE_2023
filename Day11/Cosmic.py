def truePosition(position,empty_line,empty_col) :
    l = 0
    for i in empty_line:
        if i < position[0]:
            l = l+1
    c = 0
    for i in empty_col:
        if i < position[1]:
            c = c+1
            
    return (position[0]+l*999999,position[1]+c*999999)

def distance(pos1,pos2):
    return (max(pos1[0],pos2[0]) - min(pos1[0],pos2[0])) + (max(pos1[1],pos2[1]) - min(pos1[1],pos2[1]))

input = open("input.txt")
position = []
empty_line = []
i = 0
empty_col = []
for L in input.readlines():
    if i == 0:
        empty_col = list(range(len(L.strip("\n"))))
    if not '#' in L :
        empty_line.append(i)
    else :
        j = 0
        for l in L.strip("\n"):
            if l == '#' :
                if j in empty_col:
                    empty_col.remove(j)
                position.append((i,j))
            j=j+1
    i=i+1
sum = 0
for p in range(len(position)):
    for q in range(p+1,len(position)):
        x = truePosition(position[p],empty_line,empty_col)
        y = truePosition(position[q],empty_line,empty_col)
        sum = sum + distance(x,y)
print(sum)