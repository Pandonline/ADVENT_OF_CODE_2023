with open("input.txt") as input:
    x,L1 = input.readline().strip("\n").split(":")
    x,L2 = input.readline().strip("\n").split(":")
    L1 = int(L1.replace(" ",""))
    L2 = int(L2.replace(" ",""))
    
    sum = 0
    for j in range(L1):
        if (L1-j)*j > L2:
            sum = sum +1
    print(sum)
        