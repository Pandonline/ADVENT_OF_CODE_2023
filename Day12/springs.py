def convert(sp,val):
    s = ""
    k = 0
    for i in sp:
        if i == "?":
            s = s+val[k]
            k=k+1
        else:
            s = s+i
    return s

def verif(sp,num):
    sum = 0
    for k in num:
        sum = sum+k
    if not sum == sp.count("#"):
        return False
    else:
        l = [i for i in sp.split(".") if not i == '']
        j = 0
        for i in l:
            if not len(i) == num[j]:
                return False
            j = j+1
    return True
sum = 0
input = open("input.txt")
for L in input.readlines():
    print(L)
    springs,num = L.strip("\n").split(" ")
    num = [int(n) for n in num.split(",")]
    
    nbInterogateur = springs.count("?")
    listVal = []
    for i in range(2**nbInterogateur):
        val = []
        tmp = i
        for j in range(nbInterogateur):
            if tmp%2 == 0:
                val.append("#")
            else:
                val.append(".")
            tmp = tmp//2
        listVal.append(val)
    combi = 0
    for i in listVal:
        if verif(convert(springs,i),num):
            combi = combi+1
    sum = sum + combi
print(sum)