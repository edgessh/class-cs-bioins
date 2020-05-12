""" Implementa los Algoritmo de Estretegia Evolutivas 
(1 + 1), 
(µ + 1), 
(µ + λ) y 
(µ,λ) 
para minimizar la siguiente
función. Considere los siguientes parámetros:

f (x,y) = − cos(x) × cos(y) × exp(−(x − π)^2 − (y − π)^2)

−10 ≤ x ≤ 10
−10 ≤ y ≤ 10

- Utilice codificación real con 2 genes.
- Utilice por los menos 5 decimales.
- Muestre los parámetros utilizados.
- Muestre la población inicial.
- Muestre la aptitud de los individuos en cada iteración.
- Muestre la selección, cruzamiento y mutación en cada iteración. Dependiendo del caso.
- Los demás parámetros los puede definir Ud.
+ sigma = 0.2 como valor inicial
+ iteraciones = 10
+ 1 individuo

 """


import numpy as np 
import random 
import math
import scipy.stats


# crea in individuo aleatorio
def make_individual():
    return [round(random.uniform(-10,10),5) , round(random.uniform(-10,10),5)]

# normal distribution cumulatife distribution function
# sigma: desviacion estandar, prob: numero aleatorio
# https://www.it-swarm.dev/es/python/como-calcular-la-distribucion-normal-acumulada-en-python/957966298/
# https://www.it-swarm.dev/es/python/calcule-la-probabilidad-en-la-distribucion-normal-dada-la-media-estandar-en-python/1069685455/
def cdf(_sigma, _prob):
    # scipy.stats.norm.ppf -> (probabilidad, mu o la media, sigma)
    return scipy.stats.norm.ppf(_prob,0,_sigma)

# crea una individuo mutado
#parametros:
#deviant: individuo a mutar, random_numbers= par de numeros aleatorios, standard_deviattion= vector de desvios estandar
#retorna: la nueva mutacion
def mutation(deviant, random_numbers, standard_deviation):
    print("NÚMERO ALEATORIO: ", random_numbers)
    x, y = cdf(standard_deviation[0], random_numbers[0]), cdf(standard_deviation[1], random_numbers[1])
    print("NÚMEROS ALEATORIOS GAUSS CDF: ", x, y)
    newDeviant = [deviant[0] + x, deviant[1] + y]
    return newDeviant
    # return [deviant, random_numbers, standard_deviation]
    
#fitness / función a minimizar
def fitness(x, y):
    return -1 * math.cos(x) * math.cos(y) * math.exp( -1*(x-math.pi)**2 - (y-math.pi)**2)

#Ejecusión
def exec():
    #inicializar x, sigma
    X_0 = make_individual()
    sigma_0 = [0.2, 0.2]
    print("INDIVIDUO: ", X_0[0], X_0[1])
    actual_fitness = fitness(X_0[0], X_0[1])
    print("APTITUD: ", actual_fitness)
    X_n = X_0 
    sigma_n = sigma_0
    for i in range(1000):
        print("ITERACIÓN: ", i)
        print("INDIVIDUO: ", X_n)
        random_pairs = [random.uniform(0,1), random.uniform(0,1)]
        new_guy = mutation(X_n, random_pairs, sigma_n)
        new_fitness = fitness(new_guy[0], new_guy[1])
        print("NUEVO INDIVIDUO/FITNESS: ")
        print(new_guy, new_fitness)
        if(new_fitness < actual_fitness):
            print("SE MUTA AL NUEVO INDIVIDUO")
            actual_fitness = new_fitness
            X_n = new_guy
            sigma_n = list(np.array(sigma_n)*1.5)
        else:
            print("NO MUTA EL INDIVIDUO")
            sigma_n = list(np.array(sigma_n)*(1.5)**(-1/4))
        
        print("POBLACION: ", X_n)

        print("·····················································")
        print()

exec()




