
class Data:
    def __init__(self, x,y):
        self.x = x
        self.y = y

def lagrange_interpolate(f : list , xi : int, n: int) -> float:
    result = 0.0
    for i in range(n):
        term = f[i].y
        for j in range(n):
            if j!=i :
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)
        result += term
    return result

if __name__ == '__main__' :
    f = [Data(5,12),Data(6,13),Data(9,14),Data(11,16)]
    print('Value of f(10) is : ', lagrange_interpolate(f,10,len(f)))