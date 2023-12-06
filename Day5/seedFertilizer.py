with open("input.txt") as input:
    L = (input.readline().strip("\n").split(": "))[1].split(" ")
    listSeed = [ (int(L[2*i]),int(L[2*i+1])) for i in range(len(L)//2) ]
    print("listSeed : ",listSeed)
    input.readline() ##empty line
    
    for i in range(7):
        L = input.readline() ##title line
        print(L)
        L = input.readline() ##erase title
        map = []
        while not (L == "\n" or L == ""):
            map.append( [ int(i) for i in L.strip("\n").split(" ") ] )             
            L = input.readline()
        newList = []
        for i in range(len(listSeed)):
            for m in map:
                print(listSeed)
                startI = listSeed[i][0]
                sizeI = listSeed[i][1]
                endI = startI+sizeI-1
                if(startI >= m[1] and startI < m[1]+m[2]):
                    if(endI >= m[1] and endI < m[1]+m[2]):
                        newList.append((m[0]+startI-m[1],sizeI))
                        break
                    elif(endI >= m[1]+m[2]-1):
                        newList.append((m[0]+startI-m[1],m[1]+m[2]-startI))
                        newList.append((m[1]+m[2],endI-(m[1]+m[2]-1)))
                        break
                elif(startI < m[1] and endI >= m[1]):
                    if (endI < m[1]+m[2]):
                        newList.append((startI,m[1]-startI+1))
                        newList.append((m[0],sizeI-(m[1]-startI)))
                        break
                    else:
                        newList.append((startI,m[1]-startI+1))
                        newList.append((m[0],m[2]))
                        newList.append((m[1]+m[2],endI-m[1]+m[2]+1))
                        break
                else:
                    newList.append(listSeed[i])
        listSeed = newList
    MIN = listSeed[0][0]
    for i in listSeed:
        MIN = min(MIN,i[0])
    print(MIN)