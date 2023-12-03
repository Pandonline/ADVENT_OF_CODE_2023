with open("input.txt") as input:
    Coordonne = []
    sum = 0
    L = input.readlines()
    for i in range(len(L)):
        for j in range(len(L[i])):
            if not (L[i][j] == '.' or L[i][j].isdigit() or L[i][j] == '\n'):
                Coordonne.append((i,j))
    target = []
    for i,j in Coordonne:
        for x in {i-1,i,i+1}:
            for y in {j-1,j,j+1}:
                if x >= 0 and x < len(L) and y >= 0 and y < len(L[x]):
                    if L[x][y].isdigit():
                        target.append((x,y))
    i = 0
    while i < len(target):
        x,y = target[i]
        tmp = 0
        move = True
        while(L[x][y].isdigit() and y >= 0):
            y = y-1
        y = y+1
        while(L[x][y].isdigit()):
            tmp = tmp*10 + int(L[x][y])
            if (x,y) in target:
                target.remove((x,y))
                move = False
            y = y+1
        sum = sum + tmp
        if move:
            i = i+1
    
    print(sum)