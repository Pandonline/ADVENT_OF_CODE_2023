with open("input.txt") as input:
    
    
    sum = 0
    for L in input.readlines():
        DICO = {'red': 0,'green': 0, 'blue': 0}
        game,manche = L.strip("\n").split(': ')
        for m in manche.split('; '):
            for n in m.split(', '):
                v,c = n.split(' ')
                DICO[c] = max(DICO[c],int(v))
        sum = sum + DICO['red']*DICO['green']*DICO['blue']
    print(sum)