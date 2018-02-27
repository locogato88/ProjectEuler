import math
import time
startTime = time.time()

a = [2,3]
i = 3
#prime = 76000
prime = 79000
def isPrime(int):
    for i in range(round(math.sqrt(len(a)))+1):
        if int%a[i]==0:
            return False
    return True


while (len(a)<prime+1):
    if isPrime(i):
        a.append(i)
    i+=2


sum = 0
count = 0
largestCount = 0
largestPrime = 0
for h in range(len(a)-1):
    count = 0
    sum = 0
    for j in range(h, len(a)-1):
        
        sum = sum + a[j]
        count +=1

        if sum >1000000:
            break
        if (sum in a):
            if (count > largestCount):
    
                largestCount = count
                largePrime = sum
                continue
        
        

        
print(largestPrime, largestCount)
print ("The program took %d seconds" %(time.time()-startTime))
