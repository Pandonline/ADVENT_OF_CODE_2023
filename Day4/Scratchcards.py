with open("input.txt") as input:
    
    L = input.readlines()
    scr = [1 for i in range(len(L))]
    for line in L:
        win,number = line.strip("\n").split("|")
        card,win = win.split(":")
        nbCard = int(card.split(" ")[-1])
        print(nbCard)
        win = win.split(" ")
        number = number.split(" ")
        
        win = [int(i) for i in win if (i != " " and i != "")]
        number = [int(i) for i in number if (i != " " and i != "")]
                
        score = 0

        for i in number:
            if i in win:
                score = score +1
        i = 0
        while score > 0:
            scr[nbCard+i] = scr[nbCard+i] +scr[nbCard-1]
            i = i +1
            score = score -1
    sum = 0
    for i in scr:
        sum = sum + i
    print(sum)