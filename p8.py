
def product_term(i,value,x):
    pro = 1
    for j in range(i):
        pro = pro*(value-x[j])
    return pro

def calculate_formula(value,x,y,n):
    sum = y[0][0]
    for i in range(1,n):
        sum = sum+product_term(i,value,x) * y[0][i]
    return sum
def dividedDiffTable(x,y,n):
    for i in range(1,n):
        for j in range(n-i):
            y[j][i] = ((y[j][i-1] - y[j+1][i-1])/(x[j]-x[i+j]))
    return y

def printdiffTable(y,n):
    for i in range(n):
        for j in range(n-i):
            print(round(y[i][j],4),'\t',end = ' ')
        print('')
n = 6
x = [4,5,7,10,11,13]
y = [[None]*n for j in range(len(x))]
y[0][0] = 48
y[1][0] = 100
y[2][0] = 294
y[3][0] = 900
y[4][0] = 1210
y[5][0] = 2028

y = dividedDiffTable(x,y,n)
printdiffTable(y,n)
value = 15
print("the value is :",calculate_formula(value,x,y,n))