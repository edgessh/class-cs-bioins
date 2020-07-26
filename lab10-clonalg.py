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
    CLONALG
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

def sort(_pop, _costs): #revisar
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

def sort_v2(_pop, _costs):
    temp_costs = _costs
    sorted_costs = sorted(temp_costs)
    dic = {}
    for i in range(len(temp_costs)):
        dic[temp_costs[i]] = _pop[i]
    lista_sdic = sorted(dic.items())
    new_pop = []
    new_costs = []
    print(lista_sdic[0][0])
    print(lista_sdic[0][1])
    print(lista_sdic[-1])
    print(lista_sdic)
    #
    for j in range(len(temp_costs)):
        new_costs.append(lista_sdic[j][0])
        new_pop.append(lista_sdic[j][1])
    new_pop = new_pop[0:5]
    new_costs = new_costs[0:5]
    print('-------------------------------------------------------')
    print(new_pop)
    print(new_costs)

    return new_pop, new_costs


def imprint(pop, show=False, hyper=False):
    rows = [] #costs
    if hyper:
        if show:
            for item in pop:
                print(str(''.join(item)) + ' ' + str(cost(item)))
                rows.append(cost(item))
            return pop, rows
        else:
            for item in pop:
                print(str(''.join(item)) + ' ')
                rows.append(cost(item))
            return pop, rows
    else:
        if show:
            for item in pop:
                print(str(''.join(item)) + ' ' + str(cost(item)))
                rows.append(cost(item))
            return sort(pop,rows)
        else:
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

def f_population_v2(sizeF, pop, costs):
    [fpop, fpopc] = sort(pop, costs)
    return fpop[0:sizeF]
    # return pop[0:sizeF]


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
        # print('cantidad de mutaciones: ', cant)
        r1 = random.randint(0, len(ciudades) - 1)
        r2 = random.randint(0, len(ciudades) - 1)
        temp = route[r1]
        route[r1] = route[r2]
        route[r2] = temp
        indexes.append([r1,r2])
        # print('\naleatorios: ', [r1, r2])
        # print('\nmutaciones: ', len(indexes))
    # print(route)
    # print(indexes)
    return route, indexes


def s_population(clones, size): # size = 5 en este caso
    hypers = []
    pop_s = []
    best_s = []
    hyp_indexes = []
    i = 0
    k = size
    m = 1
    # print(clones)
    print('=====================')
    while i < len(clones):
        j = i
        l = k    
        while l > 0:
            [clones[j], ind]  = mutation(clones[j], m)
            # print('estado de j: ',j)
            # print(clones[j])
            # hyp_indexes.append(ind)
            print('{0} ==> {1}'.format(clones[j], ind))

            j += 1
            l -= 1
        i += k
        k -= 1
        m += 1
    #print(clones)
    print('========================')
    [hyp, hypc] = imprint(clones, True, True)

    s_pop = []
    s_pop_c = []
    h_i = 0
    h_k = size
    # print(hypc[h_i])
    while h_i < len(clones):
        h_j = h_i
        h_l = h_k
        minimun = hypc[h_j]
        # print('minimo: ',minimun)
        # print(minimun == hypc[h_j])
        route_minimun = hyp[h_j]
        while h_l > 0:
            if hypc[h_j] < minimun:
                minimun = hypc[h_j]
                route_minimun = hyp[h_j]

            h_j += 1
            h_l -= 1
        s_pop.append(route_minimun)
        s_pop_c.append(minimun)
        h_i += h_k
        h_k -= 1

    print('\nPoblación S')
    print('============================')
    # print(s_pop)
    # print(s_pop_c)
    return s_pop



def r_population(n):
    r_p = []
    for i in range(n):
        r_p.append(random.sample(ciudades, 10))
    print('\nPoblación R')
    print('============================')
    return r_p

def merge(sp, sc, rp, rc,  fp, fc):
    new_pp = sp
    ordered = sort(fp, fc)
    new_fp = ordered[0][0:2]
    new_fpc = ordered[1][0:2]
    # print(new_fp)
    # print(new_fpc)

    parcialp = rp + new_fp
    parcialc = rc + new_fpc

    final = sort(parcialp, parcialc)

    # print(final)

    # print(parcialp)
    # print(parcialc)

    # new_pp.append(result)
    print('\nPoblación P')
    return new_pp + final[0][0:2]

@enunciate
def main(iterat):
    print(tabulate(tabla_rutas, headers=ciudades, showindex=ciudades, tablefmt='grid'))
    p = p_population(7, ciudades)
    print('\nPoblación [ P ]')
    [p, pc] = imprint(p, True)
    # print('tamaño: ', len(p))
    for i in range(iterat):
        print('\n\n\t ITERACIÓN: ', i)
        print('=========')
        print('\nPoblación [ F ]')
        [f,fc] = imprint(f_population_v2(5, p, pc ), True, False)
        print('\nPoblación P-Clone')
        [pclone, pclone_c] = imprint(get_pclone(f))
        print('\nPoblación P-Hyper')
        # el de menor costo requiere pocas mutaciones, y el de mayor costo requiere de varias mutaciones

        # s_population(pclone, len(f)) #p_hyper
        [s,sc] = imprint(s_population(pclone, len(f)), True, False)

        [r, rc] = imprint(r_population(2), True, False)

        [p, pc] = imprint(merge(s, sc, r, rc, f, fc), True, False) # de tamaño = 7

        





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

main(200)
"""
Comentario: No siempre llega al minimo ABCDEFGHIJ de costo 9
* Esto se debe a que por la aleatoriedad de los numeros se queda sin generar cambios totales a la ruta optima
* Requiere de mas iteraciones para que al menos R empiece con 'A' y tenga mayor aproximación al optimo 
* Y en la practica hay un error. No se ha considerado el menor de la poblacion R (282)  en la 1ra iteración siendo menor que los mejores de F:
 Población R 
1) DIHECGJABF	304.0
2) GBJFAHIEDC	282.0
 

"""
print(cost(['A','B','C','D','E','F','G','H','I','J']))