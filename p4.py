
INF = float('inf')
def print_matrix(m):
    r,c = len(m),len(m[0])
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=' ')
        print()
v,e = map(int,input().split())
m = [[None]*v for i in range(v)]

for i in range(v):
    for j in range(v):
        if i == j :
            m[i][j] = 0
        else :
            m[i][j] = INF
# print_matrix(m)

for i in range(e):
    src,dst,wt = map(int,input().split())
    m[src][dst] = wt
print('\n')
for k in range(v):
    for i in range(v):
        for j in range(v):
            m[i][j] = min(m[i][j],m[i][k]+m[k][j])

print_matrix(m)