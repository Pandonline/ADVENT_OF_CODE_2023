with open("input.txt") as input:
    listSeed = [ int(i) for i in (input.readline().strip("\n").split(": "))[1].split(" ") ]
    print("listSeed : ",listSeed)
    input.readline() ##empty line
    
    for i in range(7):
        L = input.readline() ##title line
        L = input.readline() ##erase title
        map = []
        while not (L == "\n" or L == ""):
            map.append( [ int(i) for i in L.strip("\n").split(" ") ] )             
            L = input.readline()
        
        for i in range(len(listSeed)):
            for m in map:
                ecart = listSeed[i] - m[1]
                if ecart >= 0 and ecart < m[2]:
                    listSeed[i] = m[0]+ecart
                    break
    
    print(min(listSeed))