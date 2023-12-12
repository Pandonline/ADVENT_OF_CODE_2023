with open("input.txt") as input:
    sum = 0
    for L in input.readlines():
        list = []
        list.append([int(i) for i in L.strip("\n").split(" ")])
        allZero = False
        i = 0
        firstValue = [list[i][0]]
        while not allZero :
            nList = [list[i][j+1]-list[i][j] for j in range(len(list[i])-1)]
            firstValue.append(nList[0])
            allZero = nList.count(0) == len(nList)
            list.append(nList)
            i = i+1
        newValue = [0]
        for j in range(len(firstValue)-1):
            newValue.append(firstValue[-j-2]-newValue[j])
        sum = sum + newValue[-1]
    print(sum)
            