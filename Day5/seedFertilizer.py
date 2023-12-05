with open("input.txt") as input:
    L = (input.readline().strip("\n").split(": "))[1].split(" ")
    listSeed = [ (int(L[2*i]),int(L[2*i+1])) for i in range(len(L)//2)  ]
    print("listSeed : ",listSeed)
    input.readline() ##empty line
    
    for i in range(7):
        L = input.readline() ##title line
        L = input.readline() ##erase title
        map = []
        while not (L == "\n" or L == ""):
            map.append( [ int(i) for i in L.strip("\n").split(" ") ] )             
            L = input.readline()
        newList = []
        for i in range(len(listSeed)):
            cut = False
            for m in map:
                seed_start = listSeed[i][0]
                seed_end = listSeed[i][0] + listSeed[i][1] -1
                seed_size = listSeed[i][1]
                
                search_start = m[1]
                search_end = m[1]+m[2]-1
                
                convert_start = m[0]
                convert_end = m[0]+m[2]-1
                
                if seed_start > search_end:
                    pass
                elif seed_start < search_start:
                    if seed_end < search_start:
                        pass
                    elif seed_end >= search_start:
                        cut = True
                        newList.append((seed_start,search_start-seed_start))
                        newList.append((convert_start,min(seed_end-search_start+1,m[2])))
                        if seed_end > search_end:
                            newList.append((search_end+1,seed_end-search_end+1))
                        break
                elif seed_start >= search_start:
                    cut = True
                    newList.append((convert_start+seed_start-search_start,min(seed_size,search_end-seed_start+1)))
                    if seed_end > search_end:
                        newList.append((search_end+1,seed_end-search_end))
                    break
            if not cut:
                newList.append((listSeed[i][0],listSeed[i][1]))
        listSeed = newList
    print(min(listSeed))