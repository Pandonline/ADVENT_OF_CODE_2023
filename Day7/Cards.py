with open("input.txt") as input:
    compareVal = ['A','K','Q','T','9','8','7','6','5','4','3','2','J']
    list = {}
    tri = [[],[],[],[],[],[],[]]
    for L in input.readlines():
        hand,val = L.split(" ")
        list[hand] = int(val)
        dico = {}
        for h in hand:
            if(dico.get(h) == None):
                dico[h] = 1
            else:
                dico[h] = dico[h]+1
        if not dico.get('J') == None and not dico.get('J') == 5:
            valJoker = dico['J']
            del dico['J']
            key = [k for k in dico.keys()]
            val = [v for v in dico.values()]
            dico[key[val.index(max(val))]] = dico[key[val.index(max(val))]] + valJoker
        match len(dico):
            case 5:
                tri[0].append(hand)
            case 4:
                tri[1].append(hand)
            case 3:
                for item in dico.values():
                    # 2 pair (2) 
                    if(item == 2) :
                        tri[2].append(hand)
                        break
                    # 3 of a kind (3)
                    elif(item == 3) :
                        tri[3].append(hand)
            case 2:
                for item in dico.values():
                    # full (4)
                    if(item == 3) :
                        tri[4].append(hand)
                        break
                    # four (5)
                    elif(item == 4) :
                        tri[5].append(hand)        
            case 1:
                tri[6].append(hand)
    rank = []
    for i in tri:
        copy = i.copy()
        while len(copy) > 0 :
            MIN = copy[0]
            for j in copy:
                if not MIN == j:
                    for k in range(5):
                        if compareVal.index(j[k]) > compareVal.index(MIN[k]):
                            MIN = j
                            break
                        elif compareVal.index(j[k]) < compareVal.index(MIN[k]):
                            break
            rank.append(MIN)
            copy.remove(MIN)
    sum = 0
    for i in range(len(rank)):
        sum = sum + list[rank[i]]*(i+1)
    print(sum)