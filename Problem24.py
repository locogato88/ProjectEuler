#Problem 24
import itertools

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
tabList = []

for p in itertools.permutations(l, 10):
   tabList.append(p)
   if(len(p)>1000000):
       break
    
print (tabList[999999])

print (itertools.permutations(l, 2))


        
