# Implemente el Algoritmo PSO (Particle Swarm Optimization) para minimizar la siguiente función:
# f „x;y” = „x + 2y − 7”2 + „2x + y − 5”2
# −10:0 ≤ x ≤ 10:0
# −10:0 ≤ y ≤ 10:0
# Tamaño de la población ≤ 10.
# Considerar los límites de los valores solo para la población inicial.
# Los demás parámetros los puede definir Ud. - Debe especificarlos en el archivo de salida
# valores iniciales para vi = [-1 , 1]
# factor  de inercia w = [0, 1]
# rand1 y rand2 = [0, 1]
# phi1, phi2 = 2.0
# iteraciones = 10

# LIbrerias
import numpy as np
import random
import math
from tabulate import tabulate

# Implementacion
class PSO:
    def __init__(self, _nparticulas, _phi, _iteraciones):
        self.nparticulas = _nparticulas
        self.phi = _phi
        self.iteraciones = _iteraciones
        self.particulas = [ [random.uniform(-10, 10), random.uniform(-10,10)] for i in range(self.nparticulas) ]
        self.velocidades = [ [random.uniform(-1, 1), random.uniform(-1,1)] for i in range(self.nparticulas) ]
        self.f = lambda x1, x2: (x1 + 2 * x2 - 7) ** 2 + (2 * x1 + x2 - 5) ** 2



    def exe(self):
        print('\nCúmulo de particulas iniciales')
        numeracion = [ i for i in range(0, self.nparticulas) ]
        cabeceras = ['X1', 'X2', 'V1', 'V2']
        muestra = np.array(self.particulas)
        muestra = np.append(muestra, self.velocidades, axis=1)
        # print(tabulate(self.particulas, tablefmt='grid', showindex=numeracion, headers=cabeceras))
        print(tabulate(muestra, showindex=numeracion, headers=cabeceras))
        print('\nFitness')
        aptitudes = [[self.f(row[0], row[1])] for row in self.particulas]
        print(tabulate(aptitudes, showindex=numeracion))
        pi_best = self.particulas.copy()
        # print(pi_best)
        gi_best_index = aptitudes.index(min(aptitudes))
        # print(gi_best_index)
        print('\nMejores locales')
        cabecera_mejores = ['X1', 'X2', 'Fitness']
        numpy_locales = np.array(pi_best)
        numpy_aptitudes = np.array(aptitudes)
        numpy_locales = np.append(numpy_locales, numpy_aptitudes, axis=1)
        print(tabulate(numpy_locales, headers=cabecera_mejores, showindex=numeracion))
        print('\nMejor global')
        numpy_global = numpy_locales[gi_best_index]
        numpy_global = np.reshape(numpy_global, (1,3))
        print(tabulate(numpy_global, headers=cabecera_mejores))

        #copias de los actuales
        actual_particulas = np.copy(muestra)  # x1, x2, v1, v2
        actual_locales = np.copy(numpy_locales) # x1, x2, fitness
        actual_global = np.copy(numpy_global) # x1, x2, fitness

        print(actual_particulas)
        print(actual_locales)
        print(actual_global)

        # Segunda parte
        # actual_particulas =
        # for i in range(1): # iteraciones
        for i in range(self.iteraciones):
            print('\nITERACION N°', i)
            print('------------------------------------------------')
            w = random.uniform(0, 1)
            print('Factor de inercia: ', w)
            nuevas_particulas = np.copy(actual_particulas) * 0
            nuevos_locales = np.copy(actual_locales) * 0
            # print(nuevas_particulas)
            # print(nuevos_locales)
            for indp in range(self.nparticulas): # indices de las particulas
                rand1, rand2 = random.uniform(0,1), random.uniform(0,1)
                print('rand1: {0}, rand2: {1} '.format(rand1, rand2))
                print('Calculando velocidad')
                # v1 y v2, despues calcular x1, x2
                nuevas_particulas[indp, 2] = w * actual_particulas[indp, 2] + self.phi * rand1 * (actual_locales[indp, 0] - actual_particulas[indp, 0]) + self.phi * rand2 * (actual_global[0][0] - actual_particulas[indp, 0])
                nuevas_particulas[indp, 3] = w * actual_particulas[indp, 2] + self.phi * rand1 * (actual_locales[indp, 1] - actual_particulas[indp, 1]) + self.phi * rand2 * (actual_global[0][1] - actual_particulas[indp, 1])
                nuevas_particulas[indp, 0] = actual_particulas[indp, 0] + nuevas_particulas[indp, 2]
                nuevas_particulas[indp, 1] = actual_particulas[indp, 1] + nuevas_particulas[indp, 3]

            print('\nNuevas particulas x1,x2,v1,v2')
            print(nuevas_particulas)
            naptitudes = [[self.f(row[0], row[1])] for row in nuevas_particulas]
            print('\nNuevo fitness ')
            print(naptitudes)
            print('\nNuevos mejores locales')
            nuevos_locales = self.actualizar_locales(actual_locales, nuevas_particulas, naptitudes)
            print('\nNuevo mejor global')
            new_gi_best_index = np.where( nuevos_locales[:,2] == min(nuevos_locales[:,2]))
            # print(nuevos_locales[new_gi_best_index[0][0]]) #revisar
            nuevo_global = nuevos_locales[new_gi_best_index[0][0]]
            print(nuevo_global)
            # ------------ actualizando los actuales por los nuevos
            actual_locales = np.copy(nuevos_locales)
            actual_particulas = np.copy(nuevas_particulas)
            # actual_global = np.copy(nuevo_global)






    def actualizar_locales(self, actual_locales, nuevas_particulas, naptitudes):
        # importan los valores minimos
        resultado = np.copy(nuevas_particulas[:,0:2]) # es una copia de los locales actuales que despues van cambiando
        naptitudes = np.array(naptitudes)
        resultado = np.append(resultado, naptitudes, axis=1)
        # print(naptitudes.shape)
        for i in range(self.nparticulas):
            if actual_locales[i, 2] < resultado[i, 2]:
                resultado[i] = actual_locales[i]
        print(tabulate(resultado, headers=['X1', 'X2', 'fitness'], showindex=self.nparticulas))

        return resultado


print('PSO')
print('Parametros:')
print(' −10:0 ≤ x ≤ 10:0¡')
print( '−10:0 ≤ x ≤ 10:0')
print( '−10:0 ≤ y ≤ 10:0')
print( 'Tamaño de la población ≤ 10.')
print( 'Considerar los límites de los valores solo para la población inicial.')
print( 'Los demás parámetros los puede definir Ud. - Debe especificarlos en el archivo de salida')
print( 'valores iniciales para vi = [-1 , 1]')
print( 'factor  de inercia w = [0, 1]')
print( 'rand1 y rand2 = [0, 1]')
print( 'phi1, phi2 = 2.0')
print( 'iteraciones = 100')

lab = PSO(6, 2, 100)
lab.exe()