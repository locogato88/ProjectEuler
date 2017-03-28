
count = 0
for i in range(1000000):
    i = str(i)
    if(i == i[::-1]):
        b = str("{0:b}".format(int(i)))
        if(b == b[::-1]):
            count +=int(i)
            print(i)


print (count)
        
