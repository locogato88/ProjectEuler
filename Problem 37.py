#Problem 37
import math

a = [2,3]
i = 3

prime = 1000
def isPrime(int):
    for i in range(round(math.sqrt(len(a)))+1):
        if int%a[i]==0:
            return False

    return True

while(len(a)<prime+1):
    if(isPrime(i)):
       a.append(i)

    i+=2
    
def trunkL(num):
    a = str(num)
    b = a[1:]
    c = int(b)
    return (c)

def trunkR(num):
    a = str(num)
    b = a[:-1]
    c = int(b)
    return (c)


num = 3791
b = str(num)

if(trunkL(num) in a):
    print ("True")
if(trunkR(num) in a):
    print("True")

