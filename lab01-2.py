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
- cruzamiento pbx
- probabilidad de mutacion: 0.05
- mutacion simple
"""

# import numpy as np
# import random 

# Number_indvs = 8
# nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# print(nodes)

# Initial_population = 


################################################################
import random
import numpy as np

matrix_routes = np.array([
    [0, 12, 3, 23, 1, 5, 23, 56, 12, 11],
    [12, 0, 9, 18, 3, 41, 45, 5, 41, 27],
    [3, 9, 0 ,89, 56, 21, 12, 48, 14, 29],
    [23, 18, 89, 0, 87, 46, 75, 17, 50, 42],
    [1, 3, 56, 87, 0, 55, 22, 86, 14, 33],
    [5, 41, 21, 46, 55, 0, 21, 76, 54, 81],
    [23, 45, 12, 75, 22, 21, 0, 11, 57, 48],
    [56, 5, 48, 17, 86, 76, 11 ,0, 63, 24],
    [12, 41, 14, 50, 14, 54, 57, 63, 0, 9],
    [11, 27, 29, 42, 33, 81, 48, 24, 9, 0]
])

citiesDic = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9}
citiesString = ['A','B','C','D','E','F','G','H','I','J']

# print (np.random.permutation(citiesString))
#pendiente


total = 10
def makePopulation():
    listOfcities = np.array([])
    for i in range(total):
        listOfcities = np.append(listOfcities, np.random.permutation(citiesString))
    # print(listOfcities.reshape(10,10))
    return listOfcities.reshape(10,10)

#poblacion inicial
population=makePopulation()

# print (population)

#fitness o aptitud /suma de todos los caminos de una ruta
def shortRoute(cities):
    sum = 0
    n = np.size(cities)
    for i in range(n):
        if((i+1)<n):
            sum += matrix_routes[citiesDic[cities[i]]][citiesDic[cities[i+1]]]
    # print('suma: ',sum)
    return sum

# tsp = np.array([])
# tsp = np.append(tsp, shortRoute(population[0]))
def fullMatrix(pobl):
    fm = np.array([])
    for i in range(np.size(pobl,axis=1)):
        fm = np.append(fm, shortRoute(population[i]))
    pobl = np.append(pobl, fm.reshape(10,1), axis=1)
    # print (pobl)
    return pobl

# POBLACION INICIAL Y SUS APTITUDES
fullPopulation = fullMatrix(population)
print('poblacion inicial y su ruta mas corta')
print(fullPopulation)


# select(p) ingresa un array y retorna un elemento del array aleatoriamente
def select(p):
    index = np.random.randint(1,10,1)
    selected = p[index]
    return selected


# parametros:
#aletatorios
# diccionario de letra y su indices
# par 1
# par 2
def swap(aleatorios ,Odict, par1, par2): 
    #ingresa lista ordenada
    Oaleatorios = sorted(aleatorios)
    print("PARES")
    print(par1)
    print(par2)
    print("SWAP")
    # print(par1)
    # print(par2)
    print(Odict)
    print(aleatorios)
    # print(Oaleatorios)
    
    # matt = np.array([])
    # for i in Odict:
    #     # print(i)
    #     # print(Odict[i])
    #     matt = np.append(matt, [i, Odict[i]])
    # print("MATT:")
    # matt = np.reshape(matt, (3,2))
    # print(matt)

    values_view = Odict.values()
    keys_view = Odict.keys()
    # print(keys_view)
    # print(values_view)
    N_keys_view = []
    N_values_view = []
    for i in keys_view:
        N_keys_view.append(i)
    for i in values_view:
        N_values_view.append(i)
    print(N_keys_view)
    print(N_values_view)

    for i in range(np.size(Oaleatorios)):
        par2[int(Oaleatorios[i])] = N_keys_view[i]
        par1[int(Oaleatorios[i])] = par1[int(N_values_view[i])]
    
    # print("PARRRRRR")
    # print(par1)
    # print(par2)
    return [par1,par2]

        

    # for index in Oaleatorios:
    #     print('\t',index)
    #     par2[index] = Odict.keys().first()
    #     print(par2)

        # par2[int(index)]=
        # first = next(iter(Odict.values()))
        # res = Odict.popitem()
        # print(res[0], res[1])
    
    # print(Odict)
    
    

    


#crossover: 
# vector de indices seleccionaros
# indivudio
# individuo
def crossover(_aleatorios, _pares1, _pares2):
    #remueve la ultima columna de aptitudes
    pares1 = np.delete(_pares1, -1, axis=1)
    pares1 = pares1.flatten() #flatten
    pares2 = np.delete(_pares2, -1, axis=1)
    pares2 = pares2.flatten() #flatten
    
   
    n = _aleatorios.size
    print ('cantidad de indices ' , n)

    lista = {}
    # print(pares2[0][int(_aleatorios[0])])
    # print(pares2[0])
    for i in range(n):
        letter = pares2[int(_aleatorios[i])] #con flatten()
        # letter = pares2[0][int(_aleatorios[i])] #sin flatten()
        number = int(_aleatorios[i])
        lista[letter] = number
    listaDict = dict(lista)
    print(listaDict)
    OrdListaDict = dict(sorted(listaDict.items()))
    print(OrdListaDict)
    p1, p2 = swap( _aleatorios,OrdListaDict, pares1, pares2)
    nueva_poblacion = [p1,p2]
    return nueva_poblacion
    
    
    

    # unordletras = np.array([])
    # for i in _aleatorios:
    #     unordletras = np.append(unordletras, pares2[0][int(i)])
    #     # print (i)
    # # print(unordletras)
    # ordletras = np.sort(unordletras)
    # # print(ordletras)
    # ordnumeros = np.array([])
    # for i in range(ordletras.size):
    #     for j in range(unordletras.size):
    #         if ordletras[i] == unordletras[j]:
    #             ordnumeros = np.append(ordnumeros, _aleatorios[j])
    

    # for j in _aleatorios:
    #     for i in range(ordletras.size):
    #         if ordletras[int(i)] == ordletras[int(j)]:
    #             ordnumeros = np.append(ordnumeros, j)

    # print('ordnumeros: ', ordnumeros)
    



def obx(pares1, pares2):
    # pares1 = select(fullPopulation)
    # pares2 = select(fullPopulation)
    print ('Pares: ')
    print (pares1)
    print (pares2)
    size = 10
    #funcion para generar aleatorios entre 1 y 10 sin repetir
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
        
    #posiciones o indices aleatorios
    print('indices aleatorios', ind )
    a,b = crossover(ind, pares1, pares2)
    return a,b



    
# par = np.array([])
# obx(par)

def exec():
    p1 = select(fullPopulation)
    p2 = select(fullPopulation)
    for i in range(10):
        print("ITERACION: ", i)
        a,b =obx(p1,p2)
        print(a)
        print(b)


exec()








