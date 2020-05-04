""" 
Implementa un Algoritmo Genético para minimizar la siguiente función. Considere los siguientes parámetros:
f „x;y” = − cos„x” × cos„y” × exp„−„x − π”2 − „y − π”2”
−10 ≤ x ≤ 10
−10 ≤ y ≤ 10 
------------------------
PARAMETROS:
- codificacion real de 2 genes
- menos de 5 decimales
- seleccion por torneo
- cruzamiento blx-0.5 
- mutacion simple


"""

import math
import numpy as np 
import random

# numero de individuos
Number_individuals = 8

#poblacion inicial
# funcion que crea la poblacion inicial
def fillP(n):
    pop = np.array([])
    for i in range(0,8):
        xx = round(random.uniform(-10, 10), 5)
        yy = round(random.uniform(-10, 10), 5)

        pop = np.append(pop, [xx,yy])
    pop = np.reshape(pop, (Number_individuals, 2))
    return pop
#round(random.uniform(-10,10),5)]
Initial_population = fillP(Number_individuals)
print("\nPOBLACION INICIAL\n")
print(Initial_population)
# size of rows = 0, size of columns = 1
print(np.size(Initial_population, 0))

# funcion f que se utiliza para calcular el fitness o aptitud
def f(x, y):
    return -1*math.cos(x)*math.cos(y)*math.exp(-1*(x-math.pi)**2 - (y-math.pi)**2)
# print(f(3,4))

# funcion para calcular el fitness de toda una poblacion
def Fitness(array):
    fit = np.array([])
    for item in array:
        fit = np.append(fit, f(item[0], item[1]))
    return fit
fitness_arrays = Fitness(Initial_population)

# seleccion por torneo
print ("MATING POOL")

def mating_pool(population):
    #seleccion de 8 peleas y 16 competidores
    i = 0
    while(i<Number_individuals):
        r1 = random.randint(0,Number_individuals)
        r2 = random.randint(0,Number_individuals)
        if(r1 != r2):
            print("random: r1 y r2 ", r1, r2)
            print("i", i)
        else:
            continue
        i += 1        

    print(population[0,:])

mating_pool(Initial_population)




def exec():
    return 0


# for i in range(30):
#     a = round(random.uniform(-10,10),5)
#     print(a)





