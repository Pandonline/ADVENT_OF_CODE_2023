with open("input.txt") as input:
    Coordonne = []
    sum = 0
    L = input.readlines()
    for i in range(len(L)):
        for j in range(len(L[i])):
            if (L[i][j] == '*'):
                Coordonne.append((i,j))
   
    for i,j in Coordonne:
        target = []
        for x in {i-1,i,i+1}:
            for y in {j-1,j,j+1}:
                if x >= 0 and x < len(L) and y >= 0 and y < len(L[x]):
                    if L[x][y].isdigit():
                        target.append((x,y))
        i = 0
        ratio = []
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
            ratio.append(tmp)
            if move:
                i = i+1
        if len(ratio) == 2:
            sum = sum + ratio[0]*ratio[1]
    
    print(sum)