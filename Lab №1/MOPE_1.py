from prettytable import PrettyTable
import numpy as np
from random import uniform

MIN, MAX = 0, 20
a0, a1, a2, a3 = 1, 2, 2, 3

X = np.empty((8, 3), dtype=float)
Y = np.empty(8)
X0 = np.empty(3)
DX = np.empty(3)
XNormalized = np.empty((8, 3), dtype=float)

td_1 = []
td_2 = []

for i in range(8):
    for j in range(3):
        X[i, j] = uniform(MIN, MAX)
        td_1.append(X[i,j].round(7))

for i in range(8):
    Y[i] = a0 + a1 * X[i, 0] + a2 * X[i, 1] + a3 * X[i, 2]


for i in range(3):
    X0[i] = (X[:, i].max() + X[:, i].min()) / 2
    DX[i] = X[:, i].max() - X0[i]

Y_et = a0 + a1 * X0[0] + a2 * X0[1] + a3 * X0[2]

for i in range(8):
    for j in range(3):
        XNormalized[i, j] = (X[i, j] - X0[j]) / DX[j]
        td_2.append(XNormalized[i, j].round(4))

dY = 999999  #dY це різниця між Y та Y_et. Таке велике значення обране для того, щоб не пропустити значення із масиву Y-ів.
number = -1

for i in range(8):                              
    if Y[i] - Y_et < dY and Y[i] - Y_et > 0:
        dY = Y[i] - Y_et
        number = i

Y2 = a0 + a1 * X[number, 0] + a2 * X[number, 1] + a3 * X[number, 2]

columns = 3
th_1 = ['X1','X2','X3']
th_2 = ['Xн1','Xн2','Xн3']
table_1 = PrettyTable(th_1)
table_2 = PrettyTable(th_2)
td_data_1 = td_1[:]
td_data_2 = td_2[:]
while td_data_1:
    table_1.add_row(td_data_1[:columns])
    td_data_1 = td_data_1[columns:]
while td_data_2:
    table_2.add_row(td_data_2[:columns])
    td_data_2 = td_data_2[columns:]

print(table_1)
print("Y:\n", Y)
print("X0: \n", X0)
print("Y_et = ", Y_et)
print(table_2)
print("number = ", number)
