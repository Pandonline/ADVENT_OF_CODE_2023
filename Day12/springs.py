from functools import *

CACHE = {}

def genKey(sp,num):
    return sp+str(num)

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
        CACHE[key] = False
        return False
    else:
        l = [i for i in sp.split(".") if not i == '']
        j = 0
        for i in l:
            if not len(i) == num[j]:
                CACHE[key] = False
                return False
            j = j+1
    CACHE[key] = True
    return True

@cache
def ListBinaire(nbInterogateur):
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
    return listVal
    
def recur(str,num):
    key = genKey(str,num)
    if key in CACHE:
        return CACHE[key]
    
    if len(str) == 0 and len(num) == 0:
        CACHE[key] = 1
        return 1
    if len(str) == 0 and not len(num) == 0:
        CACHE[key] = 0
        return 0
    if str[0] == '.':
        tmp = recur(str[1:],num)
        CACHE[key] = tmp
        return tmp
    if str[0] == '?':
        tmp = 0
        tmp = tmp + recur('#'+str[1:],num)
        tmp = tmp + recur('.'+str[1:],num)
        CACHE[key] = tmp
        return tmp
    if str[0] == '#':
        if len(num) == 0 or num[0]>len(str):
            CACHE[key] = 0
            return 0
        for i in range(num[0]):
            if str[i] == '.':
                CACHE[key] = 0 
                return 0
        if len(str) == num[0]:    
            if len(num) == 1:
                CACHE[key] = 1
                return 1   
            else:
                CACHE[key] = 0
                return 0
        else:
            if str[num[0]] == '#':
                CACHE[key] = 0
                return 0
            n_str = str[num[0]:]
            if str[num[0]] == '?':
                n_str = '.' + str[num[0]+1:]
            tmp = recur(n_str,num[1:])
            CACHE[key] = tmp
            return tmp
    return 0

sum = 0
input = open("input.txt")
for L in input.readlines():
    
    springs,num = L.strip("\n").split(" ")
    num = [int(n) for n in num.split(",")]
    
    springs = springs+'?'+springs+'?'+springs+'?'+springs+'?'+springs
    num = num+num+num+num+num
    
    sum = sum + recur(springs,num)
print(sum)