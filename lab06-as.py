# Muestre las dos primeras iteraciones de un Sistema de Hormigas (Ant System) para resolver el siguiente problema TSP:

# tabla


#  Feromona inicial: 0.1
#  Cantidad de Hormigas: 4
#  α = 1
#  β = 1
#  ρ = 0:99
#  Q = 1:0
# Por lo menos considere 1 decimal y como máximo 3 decimales.
###############################################################
# Librerias
import numpy as np
import random
from tabulate import tabulate
###############################################################
# Constantes
# feromona inicial
fi = 0.1
# valor alfa
alfa = 1
# valor beta
beta = 1
# valor ro
ro = 0.99
# constante Q
Q = 1
# cantidad de hormigas
ant_cant = 6
# iteraciones
iters = 1000
###############################################################

class AntSystem:
    """Clase AntSystem"""
    def __init__(self, _distancias, _fi, _alfa, _beta, _ro, _Q, _ant_cant, _iters, _ciudad_inicial):
        self.distancias = _distancias # d_ij
        self.fi = _fi
        self.alfa = _alfa
        self.beta = _beta
        self.ro = _ro
        self.Q = _Q
        self.ant_cant = _ant_cant
        self.feromonas = np.abs(np.identity(np.size(self.distancias[0]), dtype=float) - 1) * _fi # t_ij
        self.ciudades = [chr(word) for word in range(65, 65 + np.size(self.distancias[0]))]
        self.visibilidad = 1 / _distancias # 1/(d_ij)
        self.iters = _iters
        self.ciudad_inicial = _ciudad_inicial

    def exe(self):
        """ Ejecución del objeto de la clase"""
        print('Tabla de distancias')
        print(tabulate(self.distancias, headers=self.ciudades, showindex=self.ciudades, tablefmt='grid', stralign='center'))
        print('\n\n Tabla de visibilidad')
        print(tabulate(self.visibilidad, headers=self.ciudades, showindex=self.ciudades, stralign='center', tablefmt='grid'))
        print('\n\n Tabla de feromonas')
        print(tabulate(self.feromonas, headers=self.ciudades, showindex=self.ciudades, stralign='center', tablefmt='grid'))
        print(self.ciudades)
        for ite in range(iters): #iteracion ite
            print('\n ITERACIÓN Nº: ', ite)
            list_routes = []

            for iant in range(ant_cant): # hormiga iant
                pila_ciudades = self.ciudades.copy()
                ciudad_actual = self.ciudad_inicial
                ruta_hormiga = [self.ciudad_inicial]
                print('\n HORMIGA Nº: ', iant) # hormiga iant
                try:
                    while pila_ciudades: # NO ESTE VACIO
                        pila_ciudades.pop(pila_ciudades.index(ciudad_actual))
                        tramo = [[ciudad_actual, destino] for destino in pila_ciudades]
                        print('\n CIUDAD ACTUAL: ', ciudad_actual )
                        print('TRAMOS POSIBLES:')
                        print(tramo)
                        # ciudad_actual = random.choice(pila_ciudades)
                        # self.seleccionar(tramo, pila_ciudades) #test
                        siguiente_ciudad = self.seleccionar(tramo, pila_ciudades)
                        ciudad_actual = siguiente_ciudad
                        ruta_hormiga.append(ciudad_actual)
                except IndexError:
                    print('No hay mas ciudades disponibles')
                print('--> Ruta elegida por la hormiga Nº ', iant)
                print(ruta_hormiga)
                list_routes.append(ruta_hormiga) # lista de rutas elegidas por las hormigas
            ## ======================================================
            print('LISTA DE RUTAS ELEGIDAS POR LAS HORMIGAS')
            i = 0
            for route in list_routes:
                print('HORMIGA N° {0}: {1}'.format(i, route))
                i += 1
            ## ======================================================
            # calculando el costo de las rutas
            costos_rutas = self.calc_costos(list_routes, self.Q)
            print(costos_rutas)
            ## ======================================================
            # Actualizando las tabla de feromonas.
            self.feromonas =  self.fparciales(list_routes, costos_rutas)
            print('NUEVA TABLA DE FEROMONAS')
            print(tabulate(self.feromonas, headers=self.ciudades, showindex=self.ciudades, tablefmt='grid'))


    def seleccionar(self, tramos, ciudades):
        """Selecciona las siguientes ciudades que elegirá la hormiga
        Args:
            tramos (list): Todos los tramos posibles que una hormiga puede presentar
            ciudades (list): Pila de ciudades disponibles
        Returns:
            char: Siguiente ciudad
        """
        print('FUNCION SELECCIONAR')
        excel = np.array([])
        for tramo in tramos:
            tij = self.feromonas[self.ciudades.index(tramo[0]), self.ciudades.index(tramo[1])]
            nij = self.visibilidad[self.ciudades.index(tramo[0]), self.ciudades.index(tramo[1])]
            tijxnij = (tij ** self.alfa) * (nij ** self.beta)
            # print('========================')
            # print(tij)
            # print(nij)
            # print(tijxnij)
            row = np.array([tij,nij,tijxnij])
            excel = np.append(excel, row, axis=0)
            # excel = np.concatenate((excel, row))
        # print(np.size(tramos))
        # print(tramos[0])
        excel = np.reshape(excel, (np.size(tramos) // 2, 3))
        print('IMPRIMIR TRAMOS NUMPY')
        # print(excel.shape)
        sumatoria = np.sum(excel[:,-1])
        # print(excel)
        pij = excel[:,-1] / sumatoria
        pij = np.reshape(pij, (np.size(tramos) // 2, 1))
        ruleta = np.cumsum(pij, axis=0)
        # print(pij)
        # print(ruleta)
        excel = np.append(excel,pij, axis=1)
        excel = np.append(excel, ruleta, axis=1)
        numpy_header = ['i', 'j', 'ti', 'nij', 'tij*nij', 'Pij', 'ruleta']
        print(tabulate(np.append(np.reshape(tramos, (np.size(tramos)//2, 2)), excel ,axis=1), tablefmt='grid', headers=numpy_header)) #version 1
        # print(excel) # version 2
        print('Sumatoria Pij: ', sumatoria)
        aleatorio = random.uniform(0,1)
        print('Número aleatorio: ', aleatorio)
        # indice = np.where(excel[:,-1] <= aleatorio)[0][-1]
        indice = np.where(aleatorio <= excel[:,-1])[0][0] #extrae el primer indice del array de indices
        sig_ciudad = tramos[indice][-1]
        print('indice: ',indice)
        print('Siguiente ciudad', sig_ciudad)
        print()
        return  sig_ciudad

    def calc_costos(self, routes_list, q):
        """
        Args:
            routes_list (list): lista de rutas
            q (int): constante q
        Returns:
            int: Q/Lk
        """
        costos = np.array([])
        for route in routes_list:
            ii, jj, suma = 0, 1, 0
            while ii < len(route) - 1:
                x, y = route[ii], route[jj]
                suma += self.distancias[self.ciudades.index(x), self.ciudades.index(y)]
                ii += 1
                jj += 1
            costos = np.append(costos, suma)
        print('COSTOS: ', costos)
        return q/costos

    def get_step_indexes(self, i, j, rutas, costos):
        """ Obtiene los indices por donde pasa la hormiga
        Args:
            i (int): indice x
            j (int): indice y
            rutas (list): lista de las rutas
            costos (list): lista de los costos
        Returns:
            list: lista de indices
        """
        cant_hormigas = len(costos)
        a = self.ciudades[i]
        b = self.ciudades[j]
        indices = []
        for i in range(cant_hormigas):
            string_ruta = ''.join(rutas[i])
            if (a+b) in string_ruta:
                indices.append(i)
        return indices


    def suma_parcial(self, indexes, costos):
        """sumatoria parcial
        Args:
            indexes (list): lista de indices
            costos (list): lista de costos
        Returns:
            float: suma total
        """
        suma = 0
        for i in range(len(indexes)):
            suma += costos[indexes[i]]
        return suma

    def fparciales(self, lista_rutas, lista_costos):
        """Feromonas parciales

        Args:
            lista_rutas (list): lista de rutas
            lista_costos (list): lista de costos

        Returns:
            numpy.array: actualizacion de las feromonas
        """
        fero = np.copy(self.feromonas)
        first = fero * self.ro
        second = np.copy(self.feromonas) * 0
        i = 0
        while i < len(fero[0]):
            j = i + 1
            indices_paso = []
            while j < len(fero[0]):
                indices_paso = self.get_step_indexes(i, j, lista_rutas, lista_costos)
                second[i,j] = second[j, i] = self.suma_parcial(indices_paso, lista_costos)
                j += 1
            i += 1
        return first + second



tabla_rutas = np.array([
    [np.inf, 12, 3, 23, 1, 5, 23, 56, 12, 11],
    [12, np.inf, 9, 18, 3, 41, 45, 5, 41, 27],
    [3, 9, np.inf, 89, 56, 21, 12, 48, 14, 29],
    [23, 18, 89, np.inf, 87, 46, 75, 17, 50, 42],
    [1, 3, 56, 87, np.inf, 55, 22, 86, 14, 44],
    [5, 41, 32, 46, 55, np.inf, 21, 76, 54, 81],
    [23, 45, 12, 75, 22, 21, np.inf, 11, 63, 24],
    [56, 5, 48, 17, 86, 76, 11, np.inf, 63, 24],
    [12, 41, 14, 50, 14, 54, 57, 63, np.inf, 9],
    [11, 27, 29, 42, 33, 81, 48, 24, 9, np.inf]
])

ant_system = AntSystem(tabla_rutas, fi, alfa, beta, ro, Q, ant_cant, iters, 'A')

ant_system.exe()




###########################################################################################33
#indices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
# print(tabulate(table, headers=indices, showindex=indices, tablefmt='grid', stralign='center'))
# print()
# matriz_feromonas = np.abs(np.identity(10, dtype=float) - 1) * fi
# print(tabulate(matriz_feromonas, headers=indices, showindex=indices, stralign='center', tablefmt='grid'))


###########################################################################################33
# Imprime tabla a partir de los datos de
# una lista de listas:
# indice = ['A','B','C','D']
# headers = ['A','B']
# rios1 = [['Almanzora', 105],
#          ['Guadiaro', 79],
#          ['Guadalhorce', 154],
#          ['Guadalmedina', 51.5]]

# print(tabulate(rios1, headers=headers, tablefmt='grid', showindex=indice, stralign='center'))
# print(tabulate(data, tablefmt='grid'))


