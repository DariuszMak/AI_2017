# ćw 5 propagacja wsteczna błędu
import math
import copy

u = [
[0, 0, 1],
[1, 0, 1],
[0, 1, 1],
[1, 1, 1]
]

z = [0, 1, 1, 0]

wold = [
[0, 0, 0],
[0, 0, 0],
]

wnew = [
[0, 1, 2],
[0, 1, 2],
]

sold = [0, 0, 0]

snew = [0,1,2]


c = 0.1  # 1.0
eps = 0.0001  # 0.000001
beta = 1.0  # 3.0

################################################################################

def f(u):
    return 1 / (1 + math.exp(-beta * u))


def fp(u):
    return beta * f(u) * (1 - f(u))

def is_greater_than_eps(wnew, wold, snew, sold):
    for i in range(len(wnew)):
        for j in range(len(wnew[i])):
            if abs(wnew[i][j] - wold[i][j]) >= eps:
                return True

    for i in range(len(snew)):
        if abs(snew[i] - sold[i]) >= eps:
            return True

    return False

################################################################################

while is_greater_than_eps(wnew, wold, snew, sold):
    wold = copy.deepcopy(wnew)
    sold = copy.deepcopy(snew)

    # x
    x = [
        [None,None,None],
        [None,None,None],
        [None,None,None],
        [None,None,None],
    ]

    for p in range(4):
        for i in range(2):
            x[p][i] = f( wold[i][0] * u[p][0] + wold[i][1] * u[p][1] + wold[i][2] * u[p][2] )
        x[p][2] = 1

    # y

    y = [None, None, None, None]
    for p in range(4):
        y[p] = f( sold[0] * x[p][0] + sold[1] * x[p][1] + sold[2] * x[p][2] )

    # pochES

    ES = [None,None,None]

    for i in range(3):
        suma = 0
        for p in range(4):
            suma += (y[p] - z[p] ) * fp( sold[0]*x[p][0] +  sold[1]*x[p][1] + sold[2]*x[p][2] ) * x[p][i]
        ES[i] = suma

    # pochEW

    EW = [
        [None, None, None],
        [None, None, None],
    ]

    for i in range(2):
        for j in range(3):
            suma = 0
            for p in range(4):
                # import pdb;pdb.set_trace()
                suma += (y[p] - z[p] ) * fp( sold[0]*x[p][0] +  sold[1]*x[p][1] + sold[2]*x[p][2] ) * \
                        sold[i] * fp( wold[i][0]*u[p][0] + wold[i][1]*u[p][1] + wold[i][2]*u[p][2] ) * u[p][j]
            EW[i][j] = suma

    # nowe wartości
    for i in range(len(snew)):

        snew[i] = sold[i] -c*ES[i]

    for i in range(len(wnew)):
        for j in range(len(wnew[i])):
            wnew[i][j] = wold[i][j] - c*EW[i][j]



print('koniec','\n')
print('iteracja','\n')
print('x=',x,'\n')
print('y=',y,'\n')
print('EW=',EW,'\n')
print('ES=',ES,'\n')
print('wnew=',wnew,'\n')
print('snew=',snew,'\n')









u =[0, 0.8, 1]




x = [None,None,None]


for i in range(2):
    x[i] = f( wold[i][0] * u[0] + wold[i][1] * u[1] + wold[i][2] * u[2] )
    print( f( wold[i][0] * u[0] + wold[i][1] * u[1] + wold[i][2] * u[2] ))
x[2] = 1

# y

y = None
y = f( sold[0] * x[0] + sold[1] * x[1] + sold[2] * x[2] )

# pochES

