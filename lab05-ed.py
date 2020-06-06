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
#  Librerias
import numpy as np
import random

# --------------------------------------------------------------------------------------------------
#  Variables globales
size_gens = 4
cant_individuos = 12
F_const = 0.6
C_const = 0.5
iters = 100
# --------------------------------------------------------------------------------------------------
# poblacion incial
# funcion f dada por el problema
poblacion_inicial = [[random.uniform(-10, 10) for gen in range(0, size_gens)] for row in range(cant_individuos)]
# ejemplo de individuo: [5.218463460594267, -8.229967436387987, 5.692386759420723, -6.829114399698888]
f = lambda x, y, a, b: (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2 + (a + 2 * b - 7) ** 2 + (2 * a + b - 5) ** 2


# --------------------------------------------------------------------------------------------------


# imprime poblacion incial
def imprimir(pobl, apt=None):
    if apt is not None:
        print('APT IS NOT NONE')
        for i in range(cant_individuos):
            print(pobl[i], '\t', apt[i])
        print()
        return  # no muy seguro si es efectivo
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


# vector de las aptitudes
def aptitudes(pobl):
    aptis = []
    for indi in pobl:
        aptis.append(f(indi[0], indi[1], indi[2], indi[3]))
    return aptis


#  vector de mutacion
def mutaciones(pop, xm, xk, xl):
    matriz = np.array(pop)
    diff = matriz[xk, :] - matriz[xl, :]
    diff_pond = F_const * diff
    diff_mut = matriz[xm] + diff_pond
    print('VECTOR DE DIFERENCIAS: (Xk - Xl)')
    print(diff)
    print('VECTOR DE MUTACIÓN PONDERADA: F * (Xk - Xl)')
    print(diff_pond)
    print('VECTOR DE MUTACIÓN: Xm + F * (Xk - Xl')
    print(diff_mut)
    return list(diff_mut)


# vector de cruzamiento, retorna un vector trial
def cruzamiento(pop, mut, target,  cx, cy, ca, cb):
    trial_vector = []
    if cx > C_const:
        trial_vector.append(pop[target][0])
    else:
        trial_vector.append(mut[0])
    if cy > C_const:
        trial_vector.append(pop[target][1])
    else:
        trial_vector.append(mut[1])
    if ca > C_const:
        trial_vector.append(pop[target][2])
    else:
        trial_vector.append(mut[2])
    if cb > C_const:
        trial_vector.append(pop[target][3])
    else:
        trial_vector.append(mut[3])
    print('VECTOR TRIAL')
    print(trial_vector)
    return trial_vector


# comparar vector actual vs trial -> los fitness
def compare(actual, trial, target):
    fvar_target = f(actual[target][0], actual[target][1], actual[target][2], actual[target][3])
    fvar_trial = f(trial[0], trial[1], trial[2], trial[3])
    if  fvar_target < fvar_trial :
        print('--> --> --> Se mantiene el vector target para la nueva población')
        return actual[target]
    else:
        print('--> --> --> El vector target es reemplazado por el vector trial en la nueva población')
        return trial


# funcion principal
@titulos
def main():
    print('POBLACIÓN INICIAL')
    imprimir(poblacion_inicial)
    print('CALCULAR LA APTITUD DE CADA INDIVIDUO')
    imprimir(poblacion_inicial, aptitudes(poblacion_inicial))
    poblacion_actual = poblacion_inicial
    for i in range(iters):
        poblacion_nueva = []
        print('--> ITERACIÓN N° ', i)
        for j in range(cant_individuos):  # vector 1, vector 2 ... vector j+1
            print('--> --> VECTOR: ', j)
            Xm, Xk, Xl = random.randint(0, cant_individuos - 1), random.randint(0, cant_individuos - 1), random.randint(0, cant_individuos - 1)
            cr_x, cr_y, cr_a, cr_b = random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)
            print('FASE DE MUTACIÓN: Xm = %d, Xk = %d, Xl = %d ' % (Xm, Xk, Xl))
            vector_muts = mutaciones(poblacion_actual, Xm, Xk, Xl)
            print('FASE DE CRUZAMIENTO: x => %f | y => %f | a => %f | b => %f' % (cr_x, cr_y, cr_a, cr_b))
            vector_trial = cruzamiento(poblacion_actual, vector_muts, j, cr_x, cr_y, cr_a, cr_b)
            poblacion_nueva.append(compare(poblacion_actual, vector_trial, j))
        print('NUEVA POBLACIÓN')
        poblacion_actual = poblacion_nueva
        imprimir(poblacion_nueva, aptitudes(poblacion_nueva))
        print('\n\n')
        # poblacion_actual = poblacion_nueva
        # imprimir(poblacion_actual)
