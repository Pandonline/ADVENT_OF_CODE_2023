import re
with open("input.txt") as txt :
    
    X = ["1","2","3","4","5","6","7","8","9","one","two","three","four","five","six","seven","eight","nine"]
    
    
    sum = 0
    for L in txt.readlines():
        T = []
        for i in X:
            T.append([L.find(i),L.rfind(i)])
        print(T)
        MAX = -1
        MIN = -1
        maxVal = None
        minVal = None
        for i in T:
            for j in i:
                if MIN == -1 or ((not j == -1) and (j < MIN)) :
                    MIN = j
                    minVal = T.index(i)
                if MAX < j:
                    MAX = j
                    maxVal = T.index(i)
        sum = sum + (minVal%9 +1)*10 + maxVal%9 +1
        
    print(sum)