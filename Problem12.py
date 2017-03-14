import time
import math
start = time.time()

def findDivisors(num):
    count = 0
    for i in range(1,int(math.sqrt(num)+1)):
        if num%i ==0:
            
            count +=1
    return 2*count

i = 1
while(True):
    if(findDivisors(int(i*(i-1)/2))>500):
        print(int(i*(i-1)/2))
        break
    i+=1

print("This took %d seconds" % (time.time()-start))
        
