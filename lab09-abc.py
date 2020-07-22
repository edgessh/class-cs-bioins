# Implemente el Algoritmo ABC (Artificial Bee Colony) para minimizar la siguiente función:
# f „x;y” = „x + 2y − 7”2 + „2x + y − 5”2
# −10:0 ≤ x ≤ 10:0
# −10:0 ≤ y ≤ 10:0
#
# • SN = 3.
# • itermax ≤ 200.
# • Los demás parámetros los puede definir Ud.
# • Defina una cantidad de decimales para todos los valores.

import numpy as np
import random
from tabulate import tabulate

#funciones
f = lambda x, y: (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2
inv = lambda value : (1 / (1 + value))

def get_fia(f_cant,  xy):
    # INICIALIZAR
    fila  = np.array([])
    for i in range(f_cant):
        x = xy[i, 0]
        y = xy[i, 1]
        fun = float(f(x,y))
        fit = float(inv(fun))

        row = np.array([i, x,y,fun,fit,0])
        fila = np.append(fila, row)
    fila = np.reshape(fila, (f_cant, 6))
    return fila

def mejor_fuente(fuentes):
    if np.size(fuentes[0]) == 6:
        indice = np.where(fuentes[:,3] == min(fuentes[:,3]))
        return fuentes[indice[0]]



# envio de obreras | soluciones candidatas
def operador(fuent, phi, i, j,  k):
    if j == 0:
        xandy = fuent[ i, 1 ] + phi * (fuent[ i, 1 ] - fuent[ k, 1 ])
        return xandy
    else:
        xandy = fuent[ i, 2 ] + phi * (fuent[ i, 2 ] - fuent[ k, 2 ])
        return xandy

def evaluar(fuente_i, fuente_c):
    mejora = np.array([])
    contador = np.array([0,0,0])
    for i in range(SN):
        if fuente_i[i, 3] < fuente_c[i, 5]:
            mejora = np.append(mejora, ['NO'])
            contador[i] += 1
        else:
            mejora = np.append(mejora, ['SI'])
    mejora = np.reshape(mejora, (SN, 1))
    contador = np.reshape(contador, (SN, 1))
    mejora = np.append(mejora, contador, axis=1)
    return mejora

def soluciones_cand(fuente_ini):
    sol = np.array([])
    for i in range(SN):
        x,y = 0,0
        j = random.randint(0,1)
        k = random.randint(0, SN - 1)
        phi = random.uniform(0,1)
        while i == k:
            k = random.randint(0, SN - 1)
        x_y = operador(fuente_ini, phi, i, j, k)
        if j == 0:
            x = x_y
            y = fuente_ini[ i, 2 ]
        else:
            x = fuente_ini[ i, 1 ]
            y = x_y
        fila = np.array([k, j, phi, x, y])
        # print(fila)
        sol = np.append(sol, fila, axis=0)
    sol = np.reshape(sol, (SN, 5)) #np.size(fila)
    # print(tabulate(sol))
    funs = np.array([])
    invs = np.array([])
    for ii in range(SN):
        funs = np.append(funs, f(sol[ii, 3], sol[ii, 4]))
        invs = np.append(invs, (1 / (1+f(sol[ii, 3], sol[ii, 4]))))
    funs = np.reshape(funs,(SN, 1))
    invs = np.reshape(invs,(SN, 1))
    # print(funs)
    # print(invs)
    sol = np.append(sol, funs, axis=1)
    sol = np.append(sol, invs, axis=1)
    # print('===================')
    # print(tabulate(sol))
    me = evaluar(fuente_ini, sol)
    # print('===================')
    # print(me)
    sol = np.append(sol, me, axis=1)
    # print(tabulate(sol))
    return sol

# probabilidad de seleccion de cada fuente
def calcular_prob_ini(cands, fu):
    soluciones_prob = np.delete(fu, -1, 1)
    indices = np.where(cands[:,7] == 'SI')
    # print(indices[0])
    # print(soluciones_prob)
    if np.size(indices[0])>0:
        for id in indices[0]:
            soluciones_prob[id,1:] = cands[id,3:7]

    suma = np.sum(soluciones_prob[:,4])
    inversa = soluciones_prob[:,4] / suma
    acumulada = np.cumsum(inversa)
    soluciones_prob = np.insert(soluciones_prob, len(soluciones_prob[0]), inversa, 1)
    soluciones_prob = np.insert(soluciones_prob, len(soluciones_prob[0]), acumulada, 1)
    soluciones_prob = np.insert(soluciones_prob, len(soluciones_prob[0]), cands[:,-1], 1)
    # print(tabulate(soluciones_prob))
    return soluciones_prob


def get_index(ale, probs):
    ind = np.where(ale <= probs[:,6])
    # print('IND_> ', ind[0][0])
    return ind[0][0]

def actualizar_fuente_prob(fuente_prob, indice, phi, k, j):
    x, y = 0, 0
    linea_obs = []
    new_fuente_prob = np.array([])
    if j == 0:
        x = fuente_prob[ indice, 1 ] + phi * (fuente_prob[ indice, 1 ] - fuente_prob[ k, 1 ])
        y = fuente_prob[ indice, 2 ]
    else:
        x = fuente_prob[ indice, 1 ]
        y = fuente_prob[ indice, 2 ] + phi * (fuente_prob[ indice, 2 ] - fuente_prob[ k, 2 ])
    fun = f(x,y)
    invv = inv(fun)
    if fun < fuente_prob[ indice, 3 ]:
        linea_obs = [phi, x, y, fun, invv, 'SI', 0]
        # linea_obs = np.insert(linea_obs, -1, ['SI'], 1)
        print(encabezado_observ)
        print(linea_obs)
    else:
        cont = fuente_prob[ indice, -1 ] + 1
        linea_obs = [ phi, x, y, fun, invv, 'NO', cont]
        # linea_obs = np.insert(linea_obs, -1, ['NO'], 1)
        print(encabezado_observ)
        print(linea_obs)
    # print(tabulate(linea_obs))
    if linea_obs[5] == 'SI':
        new_fuente_prob = fuente_prob[:,0:5]
        xx = linea_obs[1]
        yy = linea_obs[2]
        funcion = linea_obs[3]
        inversa = linea_obs[4]
        new_fuente_prob[indice, 1] = xx
        new_fuente_prob[indice, 2] = yy
        new_fuente_prob[indice, 3] = funcion
        new_fuente_prob[indice, 4] = inversa

        # for indi in range(SN):

        #     new_fuente_prob = np.append([indi, xx, yy, funcion, inversa])
            # fuente_prob[indice,1:] = np.array([linea_obs[]])

        total = np.sum(new_fuente_prob[:, 4])
        inver = new_fuente_prob[:, 4] / total
        acum = np.cumsum(inver)
        # print('TOTAL: ', total)
        # print('INVER: ', inver)
        # print('ACUM: ', acum)
        new_fuente_prob = np.insert(new_fuente_prob, len(new_fuente_prob[0]), inver, 1)
        new_fuente_prob = np.insert(new_fuente_prob, len(new_fuente_prob[0]), acum, 1)
        new_fuente_prob = np.insert(new_fuente_prob, len(new_fuente_prob[0]), fuente_prob[:,-1], 1)
        new_fuente_prob[indice,-1] = linea_obs[-1]
        # sumatoria = np.sum(new_fuente_prob[ :, 4 ])
        # inversa = new_fuente_prob[ :, 4 ] / sumatoria
        # acumulada = np.cumsum(inversa)
        # new_fuente_prob = np.insert(new_fuente_prob, len(new_fuente_prob[ 0 ]), inversa, 1)
        # new_fuente_prob = np.insert(new_fuente_prob, len(new_fuente_prob[ 0 ]), acumulada, 1)
        # new_fuente_prob = np.insert(new_fuente_prob, len(new_fuente_prob[ 0 ]), cands[ :, -1 ], 1)

        # print('NUEVA FUENTE PROBABILIDAD <SI>\n\n')
        # print(new_fuente_prob.shape)
        # print(new_fuente_prob)
    else:
        new_fuente_prob = fuente_prob

        new_fuente_prob[indice,-1] = linea_obs[-1] #+ 1
        # print('NUEVA FUENTE PROBABILIDAD <NO>\n\n')
        # print(new_fuente_prob)


    return new_fuente_prob

# funcion principal
def main():
    fuentes = np.copy(fia)
    candidatas = soluciones_cand(fuentes) #tiene formato
    fuente_prob = calcular_prob_ini(candidatas, fuentes)

    for i in range(iters):
        print('\nIteración: ', i)
        print('\nEnvío de ABEJAS OBRERAS | SOLUCIONES CANDIDATAS')
        print(tabulate(candidatas, headers=encabezado_solucion))
        print('\nCalcular la probabilidad de selección de cada fuente')
        print(tabulate(fuente_prob, headers=encabezado_probabilidad))
        print('\nEnvío de ABEJAS OBSERVADORAS')
        for i in range(SN):
            print('Abeja obervadora: ', i)
            new_phi = random.uniform(0,1)
            obs_ale = random.uniform(0,1)
            ind_choice = get_index(obs_ale, fuente_prob)
            obs_k = random.randint(0, SN-1)
            while ind_choice == obs_k:
                obs_k = random.randint(0, SN-1)
            obs_j = random.randint(0,1)
            print('Aleatorio: {0}, K: {1}, J: {2}'.format(obs_ale, obs_k, obs_j))
            # print(fuente_prob[ind_choice])
            fuente_prob = actualizar_fuente_prob(fuente_prob, ind_choice, new_phi, obs_k, obs_j)
            if fuente_prob[ind_choice,-1] > limite:
                exe_x = random.uniform(-10,10)
                exe_y = random.uniform(-10,10)
                exe_fun = f(exe_x, exe_y)
                exe_div = inv(exe_fun)
                fuente_prob[ind_choice,1:5] = [exe_x,exe_y,exe_fun,exe_div]
                fuente_prob[ind_choice, -1] = 0


            print(tabulate(fuente_prob,headers=encabezado_probabilidad))

        print('Envío de ABEJAS EXPLORADORAS')
        print(tabulate(fuente_prob, headers=encabezado_probabilidad))

    print('Mejor fuente de alimento')
    idex = np.where(fuente_prob[:,3] == np.min(fuente_prob[:,3]))[0]
    print(fuente_prob[idex][0])



print("""
Implemente el Algoritmo ABC (Artificial Bee Colony) para minimizar la siguiente funcion:
f (x,y) = (x + 2y − 7)^2 + (2x + y − 5)^2
−10 < = x < = 10
−10 < = y < = 10
 SN = 3
 itermax < =  200.
 Limite = 6
 Decimales > = 3
""")


SN = 3
iters = 100
limite = 6
encabezado_fuente = ['Fuente', 'X', 'Y', 'f(X,Y)', 'Fit', 'Cont']
encabezado_solucion = ['K','J', 'phi', 'X', 'Y', 'f(X,Y)', 'Fit', 'Mejora?',  'Cont']
encabezado_probabilidad = ['Fuente', 'X', 'Y', 'f(X, Y)', 'fit', 'inv fit', 'Prob', 'Cont']
encabezado_observ = ['phi','X','Y','f(X,Y)','fit','Mejora?', 'Cont']
# Fuentes iniciales
xy = [[random.uniform(-10, 10), random.uniform(-10, 10)] for i in range(SN)]
fuente = np.array(xy)
# fuentes iniciales de alimentos
fia = get_fia(SN, fuente)
print('FUENTE DE ALIMENTOS INICIALES')
print(tabulate(fia, headers=encabezado_fuente))
# print(np.size(fia))
# print(mejor_fuente(fia))
main()


