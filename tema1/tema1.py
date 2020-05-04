""" 
Bioinspirada: tema 2
Parámetros:
- Cantidad de Individuos: 8
- Cantidad de Genes por Individuo: 5
- Selección por torneo (2)
- Probabilidad de Cruzamiento: 0.7
- Cruzamiento de un Punto (Punto 3)
- Probabilidad de Mutación: 0.05
- Mutación Bit Flip
- Cantidad de Iteraciones: 500
"""

import numpy as np 
import math
import random

TotalIndividuals = 8
TotalGensPerIndividual = 5
P_cross = 0.7
Cross_in_one_pint = 3
P_Mutate = 0.05
Iteractions = 500

Inicial_population = ['00010','01110','00000','00001','01011','10101','11101','01101']

#print(Inicial_population[3][::-1]) #para invertir el string

def converting_binaries2dec(matrix):
    matrix_dec = []
    for row in matrix:
        decimal = 0
        #print(row)
        inverser_row = row[::-1]
        for i in range(0,len(row)):
            decimal += pow(2, i) * int(inverser_row[i])
        matrix_dec.append(decimal)
    # print(matrix_dec)
    return matrix_dec

print(Inicial_population)
converting_binaries2dec(Inicial_population)

# print(random.uniform(0,1))
randomly = [(random.uniform(0,1),random.uniform(-10,10)) for i in range(8)]
print(randomly)

def f(x):
    return -1*pow(x,2)+15*x
decimal_array = converting_binaries2dec(Inicial_population)
def fitness(decimal_array):
    print(decimal_array)
    fitness_array = []
    for i in decimal_array:
        fitness_array.append(f(i))
    print(fitness_array)

#fitness(decimal_array)


def mating_pool():
    return 0



