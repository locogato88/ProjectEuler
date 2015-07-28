#Problem 7
import math
import time

startTime = time.time()


a = [2,3]
i = 3

count = 5
def isPrime(int):
    for i in range(round(math.sqrt(len(a)))+1):
        if int%a[i]==0:
            return False
    
    return True

while (True):
    if isPrime(i):
        
        a.append(i)
        count +=i
        if i>2000000:
            count -=i
            print (count)
            break
    i+=2

#print (count)

print ("The search took %d seconds" %(time.time()-startTime))                                                 

