import numpy as np
from pulp import *

A = [[0.05, 0.35, 0.44, 0.15], [0.75, 0.55, 0.36, 0.25], [0.1, 0.05, 0.1, 0.45], [0.1, 0.05, 0.1, 0.15]]
S = 15055

q = A - np.eye(4) #коэффициенты

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
problem = pulp.LpProblem('0', pulp.LpMaximize)
problem += x1 + x2 + x3 + x4, "Функция цели"
for i in range(0, len(A)):
    problem += q[i, 0] * x1 + q[i, 1] * x2 + q[i, 2] * x3 + q[i, 3] * x4 == 0, str(i)
problem += x1 + x2 + x3 + x4 <= S
problem.solve()
for variable in problem.variables():
    print (variable.name, "=", variable.varValue)
