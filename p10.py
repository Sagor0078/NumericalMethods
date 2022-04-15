
def f(x):
    return x*x*x - 2*x - 5

def bisection_method(a,b):
    if f(a) * f(b) >= 0:
        print('You not assumed a and b\n')
        return
    c = a
    while(b-a) >= 0.0001:
        c = (a+b) / 2
        if(f(c) == 0.0):
            break
        if(f(c)*f(a) < 0):
            b = c
        else:
            a = c
    print('The value of root is : ',round(c,4))
a = -1
b = 3
bisection_method(a,b)