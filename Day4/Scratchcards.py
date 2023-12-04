with open("input.txt") as input:
    
    sum = 0
    
    for line in input.readlines():
        win,number = line.strip("\n").split("|")
        card,win = win.split(":")
        
        win = win.split(" ")
        number = number.split(" ")
        
        win = [int(i) for i in win if (i != " " and i != "")]
        number = [int(i) for i in number if (i != " " and i != "")]
        
        score = 0

        for i in number:
            if i in win:
                if score == 0:
                    score = 1
                else:
                    score = 2*score
        
        sum = sum + score
    print(sum)