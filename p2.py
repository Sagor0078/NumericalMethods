
import numpy as np
with open('input.txt','r',encoding='utf-8') as g:
    A = list(map(int,g.readlines()))
with open('input2.txt','r',encoding='utf-8') as f:
    B = list(map(int,f.readlines()))
output = [(i,j) for i in A for j in B if i>j]
output2 = [1 if i>j else 0 for i in A for j in B ]
data = np.array(output2).reshape(len(A),len(B))
print(output)

print(data)