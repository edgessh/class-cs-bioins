# Minimizar la siguiente función (Considere los límites de las variables solo para la población inicial):
# f (x,y,a,b) = (x + 2y − 7)
# 2 + (2x + y − 5)
# 2 + (a + 2b − 7)
# 2 + (2a + b − 5)
# 2
# −10.0 ≤ x ≤ 10.0
# −10.0 ≤ y ≤ 10.0
# −10.0 ≤ a ≤ 10.0
# −10.0 ≤ b ≤ 10.0
#  Cantidad de Individuos: < 15
#  Lo demás parámetros los puede definir Ud.

# ------------------------------------------------------------------------------------------------
import numpy as np
import random
# --------------------------------------------------------------------------------------------------
size_gens = 4
cant_individuos = 12
F_const = 0.6
C_const = 0.5
iters = 1
# --------------------------------------------------------------------------------------------------
poblacion_inicial = [[random.uniform(-10, 10) for gen in range(0, size_gens)] for row in range(cant_individuos)]

f = lambda x, y, a, b: (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2 + (a + 2 * b - 7) ** 2 + (2 * a + b - 5) ** 2
# --------------------------------------------------------------------------------------------------


def imprimir(pobl):
    for row in pobl:
        print(row)
    print()


# imprimir(poblacion_inicial)
def titulos(func):
    print('---------------------------------')
    print('Algoritmo de evolución diferencial')
    print('Parámetros:')
    print('Cantidad de individuos: ', cant_individuos)
    print('Cantidad de dimensiones: ', size_gens)
    print('Constante de mutación: ', F_const)
    print('Constante de cruzamiento: ', C_const)
    print('Cantidad de iteraciones: ', iters)
    print('---------------------------------')
    func()
    print('---------------------------------')
    print('Fin del algoritmo')
    print('---------------------------------')


def aptitudes(pobl):
    for indi in pobl:
        print(indi)


@titulos
def main():
    print('POBLACIÓN INICIAL')
    imprimir(poblacion_inicial)
    print('CALCULAR LA APTITUD DE CADA INDIVIDUO')
    aptitudes(poblacion_inicial)
    for i in range(iters):
        print('---> ITERACIÓN N° ', i)
