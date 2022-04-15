
from itertools import product
with open("test.txt",'r',encoding='utf-8') as g:
    s = list(map(int,g.readlines()))
print("s = " + str(s))

res = [(i,j) for i,j in product(s,repeat=2) if i%j == 0 or j%i == 0]
res2 = [(i,j) for i,j in product(s,repeat=2) if i<=j]

print("res = " + str(res))
print('res2 = ' + str(res2))