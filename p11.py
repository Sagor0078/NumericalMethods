

MAX_ITER = 1000000

def f(x): 
    return (x*x*x - 2*x - 5)

def regular_falsi(a,b):
    if f(a) * f(b) >= 0:
        print("you not assumed right a and b")
        return -1
    c = a
    for i in range(MAX_ITER):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))
        if f(c) == 0:
            break
        elif f(c)*f(a) < 0:
            b = c
        else:
            a = c
    print('The Value of root : ',round(c,4))
a = -200
b = 300
regular_falsi(a,b)
