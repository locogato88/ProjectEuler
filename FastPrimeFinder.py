#Problem 7
import math
import time


prime = int(input("What prime number do you wish to find? "))
startTime = time.time()
a = [2,3]
i = 3

def isPrime(int):
    for i in range(round(math.sqrt(len(a)))+1):
        if int%a[i]==0:
            return False
 
    return True

while (len(a)<prime+1):
    if isPrime(i):
        a.append(i)
    i+=2


print ("The %d prime number is %d" % (prime, (a[prime-1])))

print ("The search took %d seconds" %(time.time()-startTime))                                                 

