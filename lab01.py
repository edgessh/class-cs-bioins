""" 
Implementa un Algoritmo Genético para minimizar la siguiente función. Considere los siguientes parámetros:
f „x;y” = − cos„x” × cos„y” × exp„−„x − π”2 − „y − π”2”
−10 ≤ x ≤ 10
−10 ≤ y ≤ 10 
"""

import math
import numpy as np 
import random

# numero de individuos
Number_individuals = 8

#poblacion inicial
def fillP(n):
    pop = []
    for i in range(0,8):
        xx = round(random.uniform(-10, 10), 5)
        yy = round(random.uniform(-10, 10), 5)

        pop = np.append(pop, [xx,yy])
    return pop

print(fillP(8))

# InicialP = [for i in Number_individuals:
#     round(random.uniform(-10,10),5)]



def f(x, y):
    return -1*math.cos(x)*math.cos(y)*math.exp(-1*(x-math.pi)**2 - (y-math.pi)**2)

# print(f(3,4))



# for i in range(30):
#     a = round(random.uniform(-10,10),5)
#     print(a)





