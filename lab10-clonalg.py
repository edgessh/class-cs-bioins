# Implemente el Algoritmo de Selección Clonal (CLONALG) para resolver el siguiente problema TSP:
#
# • sizeP = 7
# • sizeF = 5
# • sizePclone = 15
# • sizePhyper = 15
# • sizeS = 5
# • sizeR = 2
# • nDim = 10
# • maxIter = 200


import numpy as np
import random
from tabulate import tabulate
import itertools

def enunciate(fun):
    print("""
    PARAMETROS:
        sizeP = 7
        sizeF = 5
        sizePclone = 15
        sizePhyper = 15
        sizeS = 5
        sizeR = 2
        nDim = 10
        maxIter = 200
    """)
    return fun

def p_population(sizeP, cits):
    p_p = []
    for i in range(sizeP):
        p_p.append(random.sample(cits, 10))
    # print(list(p_p))
    return p_p

def cost(route):
    total = 0
    for i in range(len(route)-1):
        total += tabla_rutas[dict_cities[route[i]]][dict_cities[route[i+1]]]
    return total

def sort(_pop, _costs):
    data_pop = np.array([_pop])[0]
    data_cost = np.reshape(np.array([_costs]), (len(_costs), 1))
    # merging
    numpy_combined = np.concatenate((data_pop, data_cost), axis=1)
    sorted_array = numpy_combined[ np.argsort(numpy_combined[ :, -1 ]) ]
    # print(sorted_array)
    # spliting
    final_pop = list( sorted_array[:,0:-1 ])
    final_cost = list(map(float ,sorted_array[:, -1]))
    # print(final_cost)
    ll = []
    for item in final_pop:
        ll.append(list(item))
    # print(ll)
    return ll, final_cost
    # return _pop, _costs

def imprint(pop, show=False):
    rows = [] #costs
    if show:
        for item in pop:
            print(str(''.join(item)) + ' ' + str(cost(item)))
            rows.append(cost(item))
        return sort(pop,rows)
    else :
        for item in pop:
            print(str(''.join(item)) + ' ')
            rows.append(cost(item))
        return sort(pop,rows)

def f_population(sizeF, pop, costs):
    for i in range(len(pop)):
        pop[i].append(costs[i])
    mins = sorted(costs)[0:sizeF]
    fpop = [j[:-1] for j in pop if j[-1] in mins]
    # fpop = [j for j in pop if j[-1] in mins]
    # print(mins)
    # print(pop)
    # print(fpop)
    # sorted(fpop)
    # for i in range(sizeF):
    return fpop


def get_pclone(pf):
    i = len(pf)
    j = 0
    new_pf = []
    # print('GET CLONE')
    while i > 0:
        # print([pf[0]]*i)
        new_pf.append([pf[j]]*i)
        i -= 1
        j += 1
    # print(new_pf)
    new_pf_flat = [ x for sublist in new_pf for x in sublist ] # code brutal
    # print(new_pf_flat)
    return new_pf_flat

def mutation(route, cant):
    indexes = []
    for i in range(cant):
        r1 = random.randint(0, len(ciudades) - 1)
        r2 = random.randint(0, len(ciudades) - 1)
        temp = route[r1]
        route[r1] = route[r2]
        route[r2] = temp
        indexes.append([r1,r2])
        print('mutaciones: ', len(indexes))
    # print(route)
    # print(indexes)
    return route, indexes


def s_population(clones, size): # size = 5 en este caso
    hypers = []
    pop_s = []
    i = 0
    k = size
    print(clones)
    print('=====================')

    while i < len(clones):
        j = i
        l = k
        m = 1
        while l > 0:
            [clones[j], ind]  = mutation(clones[j], m)
            print('estado de j: ',j)
            print(clones[j])
            print(ind)
            j  += 1
            l -= 1
        i += k
        k -= 1
        m += 1

    # print(clones)
    # print(hypers)

    # [line, inds] = mutation(clones[0], 2)


@enunciate
def main(iterat):
    print(tabulate(tabla_rutas, headers=ciudades, showindex=ciudades, tablefmt='grid'))
    p = p_population(7, ciudades)
    print('\nPoblación [ P ]')
    [p, c] = imprint(p, True)
    # print('tamaño: ', len(p))
    for i in range(iterat):
        print('iteration: ', iterat)
        print('\nPoblación [ F ]')
        [f,fc] = imprint(f_population(5, p, c ), True)
        print('\nPoblación P-Clone')
        [pclone, pclone_c] = imprint(get_pclone(f))
        print('\nPoblación P-Hyper')
        # el de menor costo requiere pocas mutaciones, y el de mayor costo requiere de varias mutaciones
        print(pclone[0])
        # phyper = mutation(pclone, len(f))
        s_population(pclone, len(f)) #p_hyper
        # [s,sc] = imprint(s_population(pclone, len(f)))




        # get_pclone(f)
        # print(pclone)






ciudades = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
dict_cities = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}


tabla_rutas = np.array([
    [np.inf, 1, 3, 23, 11, 5, 83, 21, 28, 45],
    [1, np.inf, 1, 18, 3, 41, 20, 61, 95, 58],
    [3, 1, np.inf, 1, 56, 21, 43, 17, 83, 16],
    [23, 18, 1, np.inf, 1, 46, 44, 45, 50, 11],
    [11, 3, 56, 1, np.inf, 1, 93, 38, 78, 41],
    [5, 41, 21, 46, 1, np.inf, 1, 90, 92, 97],
    [83, 20, 43, 44, 93, 1, np.inf, 1, 74, 29],
    [21, 61, 17, 45, 38, 90, 1, np.inf, 1, 28],
    [28, 95, 83, 50, 78, 92, 74, 1, np.inf, 1],
    [45, 58, 16, 11, 41, 97, 29, 28, 1, np.inf]
])

main(1)
