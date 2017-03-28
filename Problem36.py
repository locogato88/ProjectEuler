import time
start = time.time()
count = 0
for i in range(1000000,2):
    i = str(i)
    if(i == i[::-1]):
        b = str("{0:b}".format(int(i)))
        if(b == b[::-1]):
            count +=int(i)


print (count)
print ("this took", time.time()-start)
