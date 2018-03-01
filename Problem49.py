from itertools import permutations
import time
import math
startTime = time.time()

a = [2,3]
i = 3
#prime = 76000

def isPrime(int):
    for i in range(round(math.sqrt(len(a)))+1):
        if int%a[i]==0:
            return False
    return True

def rotate(strg):
    return strg[1:] + strg[:1]

while (a[len(a)-1]<10000):
    if isPrime(i):
        a.append(i)
    i+=2


#Start Problem 49 Now

count = 0
for j in range(len(a)):
  
    if a[j]<1000:
        continue
    if a[j]>10000:
        break
    
    count = 0
    b = str(a[j])
    permList = []
    perms = [''.join(p) for p in permutations(b)]
    
    for h in range(len(perms)):
        if int(perms[h]) in a:
            if perms[h] not in permList:
                permList.append(perms[h])
            
        if len(permList)==3:
            if abs(int(permList[0])-int(permList[1])) == abs(int(permList[1])-int(permList[2])):
                print(permList)
                break
