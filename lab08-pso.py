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
        self.nparticuales = _nparticulas
        self.phi = _phi
        self.iteraciones = _iteraciones
        self.particulas = [[random.uniform(-10, 10), random.uniform(-10,10)] for i in range(self.nparticuales)]
        self.velocidades = [[random.uniform(-1, 1), random.uniform(-1,1)] for i in range(self.nparticuales)]
        self.f = lambda x1, x2: (x1 + 2 * x2 - 7) ** 2 + (2 * x1 + x2 - 5) ** 2



    def exe(self):
        print('\nCúmulo de particulas iniciales')
        numeracion = [ i for i in range(0, self.nparticuales) ]
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

        # Segunda parte
        # actual_particulas =
        for i in range(self.iteraciones):
            print('\nITERACION N°', i)
            w = random.uniform(0, 1)
            print('Factor de inercia: ', w)
            rand1, rand2 = random.uniform(0,1), random.uniform(0,1)
            print('rand1: {0}, rand2: {1} '.format(rand1, rand2))
            print('Calculando velocidad')











lab = PSO(6, 2, 10)
lab.exe()