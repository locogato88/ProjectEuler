#Problem 55

def palindrome(int):
    a = str(int)
    b = (a[::-1])
    return (a == b)

def Lychrel(num):
    i =0
    while(i<50):
    
        a = str(num)
        b  =(a[::-1])
        c = int(b)
        if(palindrome(num+c)):
            return True
        else:
            i +=1
            num = (c+num)
    return False

print("Starting")
count = 0
for i in range(10000):
    if(Lychrel(i) == False):
        count +=1
    
print (count)
print("Finished")



