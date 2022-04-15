
#calculating u*(u-1)*(u-2) ........
def u_cal(u,i):
    temp = u
    for i in range(1,n):
        temp = temp*(u-i)
    return temp
#calculating nicher factorial

def fact(n):
    f = 1
    for i in range(2,n+1):
        f = f*i
    return f

n = 6
x = [1911,1921,1931,1941,1951,1961]
y = [[None]*n for j in range(len(x))]
y[0][0] = 12
y[1][0] = 15
y[2][0] = 20
y[3][0] = 27
y[4][0] = 39
y[5][0] = 52

# calculating forward diffrence table
for i in range(1,n):
    for j in range(n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]
#displaying divided diff. table
for i in range(n):
    print(x[i],end='\t')
    for j in range(n-i):
        print(y[i][j],end='\t')
    print('')
#calculating u
value = 1946
first = (value - x[0])
diff = (x[1] - x[0])
u = first / diff
#apply newton-forward diffrence formula x = f(a) + u* Df(a) + u*(u-1)*D^2 f(a) / 2! + .........
sum = y[0][0]
for i in range(1,n):
    sum = sum + (u_cal(u,i)*y[0][i]) / fact(i)
print(sum)