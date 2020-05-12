""" 
Implementa un Algoritmo Genético para minimizar el siguiente problema TSP:
* Representación por Permutación.
* Cruzamiento OBX.
* Muestre los parámetros utilizados.
* Muestre la población inicial.
* Muestre la aptitud de los individuos en cada iteración.
* Muestre la selección de padres, el cruzamiento y mutación en cada iteración.
* Los demás parámetros los puede definir Ud.
- cantidad de individuso: 8
- cantidad de genes por individuo: 10
- seleccion por ruleta
- probabilidad de cruzamiento: 0.9
- cruzamiento obx
- probabilidad de mutacion: 0.05
- mutacion simple
"""


import numpy as np 
import random


A = {'A': 0, 'B':12, 'C':3, 'D':23, 'E':1, 'F':5, 'G':23, 'H':56, 'I': 12, 'J':11}
B = {'A': 12, 'B':0, 'C':9, 'D':18, 'E':3, 'F':41, 'G':45, 'H':5, 'I': 41, 'J':27}
C = {'A': 3, 'B':9, 'C':0, 'D':89, 'E':56, 'F':21, 'G':12, 'H':48, 'I': 14, 'J':29}
D = {'A': 23, 'B':18, 'C':89, 'D':0, 'E':56, 'F':21, 'G':12, 'H':48, 'I': 14, 'J':29}
E = {'A': 1, 'B':3, 'C':56, 'D':87, 'E':0, 'F':55, 'G':22, 'H':86, 'I': 14, 'J':33}
F = {'A': 5, 'B':41, 'C':21, 'D':46, 'E':55, 'F':0, 'G':21, 'H':76, 'I': 54, 'J':81}
G = {'A': 23, 'B':45, 'C':12, 'D':75, 'E':22, 'F':21, 'G':0, 'H':11, 'I': 57, 'J':48}
H = {'A': 56, 'B':5, 'C':48, 'D':17, 'E':86, 'F':76, 'G':11, 'H':0, 'I': 63, 'J':24}
I = {'A': 12, 'B':41, 'C':14, 'D':50, 'E':14, 'F':54, 'G':57, 'H':63, 'I': 0, 'J':9}
J = {'A': 11, 'B':27, 'C':29, 'D':42, 'E':33, 'F':81, 'G':48, 'H':24, 'I': 9, 'J':0}

table = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I':I, 'J':J }

N = 8
L = 10



# individuos iniciales o poblacion inicial
def convert_numpy_to_letters(vector):
    letras = []
    for item in vector:
        letras.append(chr(item))
    return letras

def baseInd():
    all_ind = [] # todos los individuos
    ranges = np.arange(65,75) #valores de A - Z = 65 - 74
    for i in range(N): #cantidad de individuos
        all_ind.append(convert_numpy_to_letters((np.random.permutation(ranges)).tolist()))
    # print(all_ind)
    return all_ind

all_base_ind = baseInd()


print("-------------INDIVIDUOS BASE------------------------")
print(all_base_ind) # imprime todos los individuos
print("------------")
# print(all_base_ind[0]) #imprime el primer individuo

def fitness(tour):
    total = 0
    for i in range(len(tour)-1):
        j = i+1
        if (j > i):
            # print("i", i)
            # print("j", j)
            total += table[(tour[i])][tour[j]]
            j += 1
    return total

# print(fitness(all_base_ind[0]))

def all_fitness(tourses):
    all_fit = []
    for route in tourses:
        all_fit.append(fitness(route))
    return all_fit

# print(all_fitness(all_base_ind))


#pertenece al mating pool
def roulette(tourses):
    print("RULETA")
    score = np.array(all_fitness(tourses))
    inv_score = 1/score
    suma = np.sum(inv_score)
    percent = inv_score / suma
    percent_acum = np.cumsum(percent)
    indices_selected = []
    # print(inv_score)
    # print(suma)
    # print(percent)
    # print(percent_acum)
    matr = np.concatenate((score ,inv_score, percent, percent_acum), axis=0) 
    print("FITNESS \t INVERSAS \t PORCENTAJES \t ACUMULADAS")
    print(np.transpose(np.reshape(matr, (4,8))))

    print("CREACION DEL MATING POOL")
    for i in range(N): #hasta 8 candidatos para el torneo
        lucky_number = round(random.uniform(0,1), 7)
        # print(lucky_number)
        indice = 0
        for nn in percent_acum:
            if(lucky_number <= nn):
                indice = np.where(percent_acum == nn)
                break
            else:
                continue
        # indices_selected.append((np.array(indice)).flatten())
        indice_cleaned = int((np.array(indice)).flatten())
        # print("indice",  indice_cleaned)
        indices_selected.append(indice_cleaned)
    # print(indices_selected)
    return lucky_number,indices_selected

        

def random_indices_4OBX():
    # indices aleatorios 
    ind = np.array([])
    for i in range(3):
        rr = int(random.randint(0,9))
        if (rr not in ind):
            ind = np.append(ind, rr)
        else:
            if(rr not in ind):
                rr = int(random.randint(0,9))
                ind = np.append(ind, rr)
            else:
                rr = int(random.randint(0,9))
                ind = np.append(ind, rr)
    return ind


# t1 y t2 vectores parciales ordenados
def fixing(t1, t2, ind_array): 
    dixi = {}
    for i in range(np.size(t1)):
        dixi[t2[i]] = t1[i] # por la forma de cruzamiento de OBX se toma primero el segundo padre
    ####################
    print("DIXI")
    OrdDixi = dict(sorted(dixi.items()))
    keys_view = OrdDixi.keys()
    values_view = OrdDixi.values()
    # print(keys_view)
    # print(values_view)
    N_keys_view = []
    N_values_view = []
    for i in keys_view:
        N_keys_view.append(i)
    for i in values_view:
        N_values_view.append(i)
    # print(N_values_view) #t1
    # print(N_keys_view) #t2
    ####################
    t1 = N_values_view
    t2 = N_keys_view    
    print(t1)
    print(t2)
    return t1,t2


#mutacion simple
def mutacion(p1, p2):
    n = np.size(p1)
    indicex = 5
    indicey = 3
    print("MUTACION")
    for i in range(n):
        temp1 = p1[indicex]
        temp2 = p2[indicey] 
        p1[indicex] = p2[indicex]
        p2[indicex] = temp1
        p1[indicey] = p2[indicey]
        p2[indicey] = temp2

    return p1, p2




# cruzamiento obx
def crossOBX(_p1, _p2):
    print("PADRES:" )
    print(_p1, " <-> ", _p2)
    print("===================")
    
    #posiciones o indices aleatorios
    ind = sorted(random_indices_4OBX())
    print('indices aleatorios', ind )
    tp2 = []
    tp1 = []
    for ii in ind:
        tp2.append(_p2[int(ii)])
        tp1.append(_p1[int(ii)])
    print("|||||||||||||||")
    print(tp1)
    print(tp2)
    tp1, tp2 = fixing(tp1, tp2, ind) # tp1 y tp2 ordenados 

    print("***************")
    for i in range(np.size(ind)):
        _p1[int(ind[i])] = tp1[i]
        _p2[int(ind[i])] = tp2[i]
        # print(_p1[int(ind[i])])
        # print(_p2[int(ind[i])])
        # print(tp1[int(ind[i])])
        # print(tp2[int(ind[i])])

    mutacion_random = random.uniform(0,1)
    if(mutacion_random < 0.05):
        _p1, _p2 = mutacion(_p1, _p2)
    return _p1, _p2
    


#seleccion de padres = 4 porque generan 2 hijos para un total de 8
def mating_pool(tourses):
    ln,indices = roulette(tourses)#lucky numbers, indices de los lucky numbers
    print("INDICES DE LA POBLACION ELEGIDA") 
    print(indices) #indices de los candidatos
    print("POBLACION ELEGIDA")
    
    times = 4 # 4 veces elegira 2 pares , haciendo un total de 8
    New_population = []
    for item in indices:
        print(tourses[item])
    while(times > 0):
        left = random.randint(0,7)
        right = random.randint(0,7)
        p1 = tourses[indices[left]]
        p2 = tourses[indices[right]]
        h1, h2 = crossOBX(p1,p2)
        New_population.append(h1)
        New_population.append(h2)
        times -= 1

    print("NUEVA POBLACION")
    print(New_population)
    return New_population



# roulette(all_base_ind)

# mating_pool(all_base_ind)



def exec():
    poblacion_inicial = all_base_ind
    # SELECCION POR RULETA
    Numero_aleatorio, indices_seleccionados = roulette(poblacion_inicial)
    

    # mating_pool(poblacion_inicial)
    for gen in range(10):
        print("------------------------------->>> ITERACION: ", gen)
        Nueva_poblacion = mating_pool(poblacion_inicial)
        poblacion_inicial = Nueva_poblacion
        score = np.array(all_fitness(poblacion_inicial))
        inv_score = 1/score
        suma = np.sum(inv_score)
        percent = inv_score / suma
        percent_acum = np.cumsum(percent)
        matriz = np.concatenate((score ,inv_score, percent, percent_acum), axis=0) 
        # print(np.reshape(Nueva_poblacion, (8,1)))
        print("FITNESS \t INVERSAS \t PORCENTAJES \t ACUMULADAS")
        print(np.transpose(np.reshape(matriz, (4,8))))







exec()