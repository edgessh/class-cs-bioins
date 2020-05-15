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
+ cantidad de descendientes: 1 -> lambda

 """

import numpy as np 
import random 
import math
import scipy.stats

var_mu = 8 #cantidad de individuos
var_lambda = 6 #cantidad de descendientes
sigma = 0.2 #desviacion estandar inicial
torneos = 2
iteraciones = 1000
delta_sigma = 1/math.sqrt(2*math.sqrt(2)) # 2 = n


# crea la poblacion inicial var_mu = 8
def init_population():
    pop = []
    for i in range(var_mu):
        pop.append([[round(random.uniform(-10,10), 5), round(random.uniform(-10,10), 5)], [sigma,sigma]])
    return pop


#fitness / función a minimizar
def fitness(x, y):
    return -1 * math.cos(x) * math.cos(y) * math.exp( -1*(x-math.pi)**2 - (y-math.pi)**2)


def evalue(init_pop):
    pass

# print((init_population()))

def print2D(matrix):
    print("\nImprimiendo... ↓ \n")
    x = len(matrix)
    y = len(matrix[0])
    print(x, y)
    for i in range(x):
        print(matrix[i])
    print()
#

# retorna la matriz de individuos con sus aptitudes
def Allfitness_2(matrix):
    # print(matrix)
    n = len(matrix)
    fit = []
    mat = []
    
    for i in range(n):
        fit.append(fitness(matrix[i][0][0], matrix[i][0][1]))
    for i in range(n):
        mat.append([matrix[i][0], matrix[i][1], fit[i]])
    
    print("MATT")
    print(mat[0])
    
    # mat=np.append(mat, fn, axis = 1)
    
    return mat
    

def Allfitness(matrixy):
    print("FITTNESS")
    m = np.array(matrixy)
    vfit = m[:,0]
    # fit=np.array([])
    # print(vfit)
    fit = -1 * np.cos(vfit[:,0]) * np.cos(vfit[:,1]) * np.exp( -1*(vfit[:,0]-np.pi)**2 - (vfit[:,1]-np.pi)**2)
    list_fit = list(fit)
    for i in range(var_mu):
        matrixy[i].append(list_fit[i])
    return list(fit)
    
# normal
def cdf(_sigma, _prob):
    # scipy.stats.norm.ppf -> (probabilidad, mu o la media, sigma)
    return scipy.stats.norm.ppf(_prob,0,_sigma)

# cruce de los padres y cruce de sus desvios standar
#mutaciones para generar el nuevo individuo
# def cross_mute(cand, r1, r2):
#     p1 = list(cand[r1,:]) #padre 1
#     p2 = list(cand[r2,:]) #padre 2
#     print("CROSS - MUTATION")
#     x = (p1[0][0] + p2[0][0]) / 2
#     y = (p1[0][1] + p2[0][1]) / 2
#     sinmutar = [x, y]
#     print("DESCENDIENTE:\n ", sinmutar)
#     _sigmaXY = []
#     news = []
#     for i in range(2): 
#         #mutaciones 
#         #aleatorios para el primer gen i 
#         A1 = random.uniform(0,1)
#         A2 = random.uniform(0,1)
#         print("ALEATORIO 1: " , A1)
#         print("ALEATORIO 2: " , A2)
#         new_sigma = p1[1][i]*math.exp(cdf(delta_sigma, A1))
#         _sigmaXY.append(new_sigma)
#         print("NEW SIGMA 1: ", new_sigma)
#         new_x = sinmutar[i] + cdf(new_sigma, A2)
#         news.append(new_x)
#         # new_y

#     print()
#     print("Nuevo individuo descendiente: ", news)    
#     print("Sigma vector: ", _sigmaXY)
#     print()

#     # return news # retorna el individuo descendiente
#     return np.array([news, _sigmaXY, fitness(news[0], news[1])])
    
# union de la poblacion y descendientes    
def union(pop, des):
    d = np.array(des)
    pop = np.append(pop, d)
    return pop
    
# def selectBest(matrix_numpy):
#     print("\nELEGIR LOS <MU> =>", var_mu,"INDIVIDUOS MEJORES PARA LA NUEVA POBLACION: ")
#     matrix_numpy = np.reshape(matrix_numpy, (var_mu+1, 3))
#     ord_matrix = sorted(list(matrix_numpy), key=lambda x: x[2]) # para ordenar
#     print()
#     print("INDIVIDUOS ORDENADOS POR APTITUD")
#     print(ord_matrix)
#     ord_matrix = np.delete(ord_matrix, -1, axis=0)
#     print("NUEVOS INDIVIDUOS - FIN DE LA ITERACIÓN")
#     print(ord_matrix)
    

    return ord_matrix # el vector 

# candidates = poblacion , var_lambda = var_lambdaidad de descendientes = 1
def descendiente(candidates):
    i = 0
    candidates = np.array(candidates)
    parents = np.array([])
    new_descendiente = []
    new_population = []
    while(i < var_lambda):
        # selecciona los padres aleatorios 
        random1 = random.randint(0,var_mu-1)
        random2 = random.randint(0,var_mu-1)
        if(random1 != random2):
            print("PADRES → ", random1, " VS ", random2)
            print(list(candidates[random1,:]), " <<< VS >>> ", list(candidates[random2,:]))
            new_descendiente.append(cross_mute(candidates, random1, random2)) # el nuevo descendiente  en este caso solo 1 por iteracion
            print("UNION DE LOS <MU> => ",var_mu ,"INDIVIDUOS CON EL DESCENDIENTE <LAMBDA> =>", var_lambda)
            print(union(candidates,new_descendiente))
            new_population = selectBest(union(candidates, new_descendiente))


        else:
            print("ERROR ---------------------------------------------------------------------------------------------")
            print("ERROR -----------------------VUELVA A EJECUTAR-----------------------------------------------------")
        i += 1
    return new_population


def tournament(candidates):
    print("<<< TORNEO >>>")
    players=[]
    
    winner = []
    for i in range(2):
        random1 = random.randint(0,var_mu-1)
        random2 = random.randint(0,var_mu-1)
        if(random1 != random2):
            print("PADRES → ", random1, " VS ", random2)
            a, b = candidates[random1], candidates[random2] 
            print(a, " <<< VS >>>" , b)
            if( a[2] < b[2] ): 
                players.append(a)
            else:
                players.append(b)
        else:
            print("PADRES → ", 4, " VS ", 5) #3 y 5 los nuevos aleatorios
            a, b = candidates[4], candidates[5] 
            print(a, " <<< VS >>>" , b)
            if( a[2] < b[2] ): 
                players.append(a)
            else:
                players.append(b)
    print("PADRE 1 , PADRE 2:")
    print(players)
    return players

def fitness_line(descent):   
    fit = fitness(descent[0][0], descent[0][1])
    descent.append(fit)
    
    return descent
    
def crossing(plays):
    print("CRUZAMIENTO")
    x = plays[0]
    y = plays[1]
    print(x,y)

    genX = (x[0][0]+y[0][0])/2
    genY = (x[0][1]+y[0][1])/2

    sigmaX = math.sqrt((x[1][0]*y[1][0]))
    sigmaY = math.sqrt((x[1][1]*y[1][1]))
    
    result = [[genX,genY], [sigmaX, sigmaY]]
    # return ([[genX, genY], [sigmaX, sigmaY]])
    
    return fitness_line(result)

def descendientes(actualP):
    descend = []
    final_descend = []
    for i in range(var_lambda):
        print("DESCENDIENTE: ", i)
        players = tournament(actualP) # winner son los padres 1 y padre 2 del torneo
        descend.append(crossing(players))
        print("DESCENDIENTES")
        print(descend)

    for item in descend:
        print("MUTACIONES:")
        print(item)
        _sigmaXY = []
        news = []
        for i in range(2):
            #mutaciones 
            #aleatorios para el primer gen i 
            A1 = random.uniform(0,1)
            A2 = random.uniform(0,1)
            print("ALEATORIO 1: " , A1)
            print("ALEATORIO 2: " , A2)
            new_sigma = item[1][i]*math.exp(cdf(delta_sigma, A1))
            _sigmaXY.append(new_sigma)
            print("NUEVO SIGMA 1: ", new_sigma)
            new_x = item[0][i] + cdf(new_sigma, A2)
            news.append(new_x)
            # new_y
        print("DESCENDIENTE FINAL")
        final_descend.append(fitness_line([news, _sigmaXY]))
        print(final_descend)

    return final_descend




#convertir en lista
def fix(numpy_news):
    # return list(numpy_news)
    print("NUMPY NEWS")
    print(numpy_news)
    return 0

# ordena y selecciona los mejores
def ordered(conj):
    print("\nELEGIR LOS <MU> =>", var_mu,"INDIVIDUOS MEJORES PARA LA NUEVA POBLACION: ")
    
    ord_matrix = sorted(conj, key=lambda x: x[2]) # para ordenar
    print()
    print("INDIVIDUOS ORDENADOS POR APTITUD")
    print2D(ord_matrix)
    ord_matrix.remove(ord_matrix[-1])
    print("NUEVOS INDIVIDUOS - FIN DE LA ITERACIÓN")
    print2D(ord_matrix)
    return ord_matrix

#une a todos los individuos y descendientes
def merge_mu_descen(mu_individuals, v_descents ):
    print("UNION DE LOS <MU> => ",var_mu ,"INDIVIDUOS CON EL DESCENDIENTE <LAMBDA> =>", var_lambda)
    print2D(mu_individuals)
    print("·······································································································")
    for vec in v_descents:
        mu_individuals.append(vec)
    print2D(mu_individuals)
    return mu_individuals

def exec():
    print("MU+1")
    actual_p = init_population()
    print2D(actual_p)
    aptitudes_lista = []
    new_p = np.array([])

    for i in range(10): #iteraciones
        print("----------- ITERACIONES : ", i, "--------------")
        actual_p = Allfitness_2(actual_p) # retorna las aptitudes  en un solo vector, y actual_p se actualiza con la columna aptitudes
        # print2D(actual_p)
        #generar descendiente lambda = 1 | # seleccion por descendiente
        
        vec_descendientes = descendientes(actual_p)
        print("ACTUALLLLL")
        merged_pop = merge_mu_descen(actual_p, vec_descendientes)

        new_population = ordered(merged_pop)
        actual_p = new_population
        print(".................NUEVA POBLACIÓN..................")
        print2D(actual_p)

        #actual_p = new_p
        
        # actual_p = fix(new_p)
        
        print()
        print()
        



    #cruzamiento


    #mutacion




exec()
