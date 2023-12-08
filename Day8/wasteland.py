import math

with open("input.txt") as input :
    readTrajet = True
    trajet = ""
    while(readTrajet):
        t = input.readline().strip("\n")
        if not t == "":
            trajet = trajet + t
        else:
            readTrajet = False
    DICO = {}
    for L in input.readlines():
        path,way = L.strip("\n").split(" = ")
        left,right = (way.replace("(","").replace(")","").replace(",","")).split(" ")
        DICO[path] = (left,right)
      
    listStart = []
    for key in DICO.keys():
        if key[2] == 'A':
            listStart.append(key)
            
    listSum = []
    for i in listStart:
        sum = 0
        node = i
        while not node[2] == 'Z':
            if trajet[sum%len(trajet)] == "L":
                node = DICO[node][0]
            elif trajet[sum%len(trajet)] == "R":
                node = DICO[node][1]
            sum = sum +1
        listSum.append(sum)
    print(listSum)
    s= math.lcm(*listSum)
    print(s)
    