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

def fwinner(p1, p2):
    #gana el que tenga menor aptitud (minimizar funcion)
    _p1 = f(p1[0],p1[1])
    _p2 = f(p2[0], p2[1])
    print("Aptitudes → ", _p1 , " «» ", _p2)
    
    if(_p1 < _p2):
        return p1
    else:
        return p2
    

def mating_pool(population):
    #seleccion de 8 peleas y 16 competidores
    i = 0
    new_selected = np.array([])
    while(i<Number_individuals):
        r1 = random.randint(0,Number_individuals-1) #cuidado con sobrepasar la numero de invidiuos [0 a 7]
        r2 = random.randint(0,Number_individuals-1)
        if(r1 != r2):
            print("Enfrentamiento: ", i)
            print(r1, 'vs', r2)
            print(population[r1,:] , " VS ", population[r2,:])
            winner = fwinner(population[r1,:], population[r2,:])
            print("Ganador → ", winner)
            new_selected = np.append(new_selected, winner, 0)
            print()
            # print(population[r1,:])
            # print(" VS ")
            # print(population[r2,:])
            # print("i", i)
            i += 1        
        else:
            continue
    
    # print(population[0,:])
    # print(population[8,:])
            

    # print(population[0,:])
    new_selected = np.reshape(new_selected, (Number_individuals, 2))
    print(new_selected)
    return new_selected

# mating_pool(Initial_population)
new = mating_pool(Initial_population)



def mating_pool_2(candidates):
    i = 0
    parents = np.array([])
    while(i < Number_individuals):
        random1 = random.randint(0,Number_individuals-1)
        random2 = random.randint(0,Number_individuals-1)
        if(random1 != random2):
            if(candidates[random1,0] != candidates[random2,0]):
                print("PARENTS → ", random1, " <3 ", random2)
                print(candidates[random1,:], " <3 ", candidates[random2,:])
                parents = np.append(parents, np.array([candidates[random1,:], candidates[random2,:]]))
                i += 1
            else:
                continue
        else:
            continue
    return parents
    

def choose_parents(candidates):
    a = mating_pool_2(candidates) 
    print(a)
    
choose_parents(new)



def exec():
    return 0


# for i in range(30):
#     a = round(random.uniform(-10,10),5)
#     print(a)





