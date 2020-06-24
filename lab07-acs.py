# Muestre las dos primeras iteraciones de un Sistema de Colonia de Hormigas (Ant Colony System) para resolver el
# siguiente problema TSP:
# • Feromona inicial: 0.1
# • Cantidad de Hormigas: 4
# • α = 1
# • β = 1
# • ρ = 0:01
# • Q = 1:0
# • Considere una ciudad inicial para todas las hormigas.
# • Por lo menos considere 1 decimal y como máximo 3 decimales.

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
# valor ro / p para la actualizacion de feromona  global
p = 0.99
# constante Q
Q = 1
# cantidad de hormigas
ant_cant = 6
# constante q0 para la construccion de la solucion intesificacion(<) divercificacion(>)
q0 = 0.5
#constante phi para la actualizacion de feromona  local
phi = 0.5
# iteraciones
iters = 100
###############################################################

class AntSystem:
    """Clase AntSystem"""
    def __init__(self, _distancias, _fi, _alfa, _beta, _p, _Q, _ant_cant, _phi, _q0,_iters, _ciudad_inicial):
        self.distancias = _distancias # d_ij
        self.fi = _fi
        self.alfa = _alfa
        self.beta = _beta
        self.p = _p
        self.Q = _Q
        self.phi = _phi
        self.q0 = _q0
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
                        ca_var = ciudad_actual
                        print('TRAMOS POSIBLES:')
                        print(tramo)
                        q = random.uniform(0,1)
                        print('Valor de q = ', q)
                        if q < q0:
                            print('Construcción de solución por Intensificación')
                            # ciudad_actual = random.choice(pila_ciudades)
                            try:
                                siguiente_ciudad = self.seleccionar_intensificacion(tramo, pila_ciudades)
                                ciudad_actual = siguiente_ciudad
                                ruta_hormiga.append(siguiente_ciudad)
                                print('ACTUALIZANDO TRAMO: {0} - {1}'.format(ca_var, siguiente_ciudad))
                                # print(ca_var)
                                # print(siguiente_ciudad)
                                # ACTUALIZACION ONLINE
                                self.feromonas[ self.ciudades.index(ca_var) ][
                                    self.ciudades.index(siguiente_ciudad) ] = (1 - self.phi) * self.feromonas[
                                    self.ciudades.index(ca_var) ][
                                    self.ciudades.index(siguiente_ciudad) ] + self.phi * 0.1
                                print(self.feromonas[ self.ciudades.index(ca_var) ][
                                    self.ciudades.index(siguiente_ciudad) ])
                            except ValueError:
                                print('Secuencia vacia')

                            # self.seleccionar(tramo, pila_ciudades) #test
                            # siguiente_ciudad = self.seleccionar(tramo, pila_ciudades)
                        else: # q > q0
                            # ACTUALIZACION ONLINE
                            print('Construcción de solución por Diversificación')
                            siguiente_ciudad = self.seleccionar_diversificacion(tramo, pila_ciudades)
                            ciudad_actual = siguiente_ciudad
                            ruta_hormiga.append(ciudad_actual)
                            print('ACTUALIZANDO TRAMO: {0} - {1}'.format(ca_var, siguiente_ciudad))
                            # print(ca_var)
                            # print(siguiente_ciudad)
                            self.feromonas[self.ciudades.index(ca_var)][
                                self.ciudades.index(siguiente_ciudad)] = (1 - self.phi) * self.feromonas[
                                self.ciudades.index(ca_var)][
                                self.ciudades.index(siguiente_ciudad)] + self.phi * 0.1
                            print(self.feromonas[ self.ciudades.index(ca_var) ][
                                      self.ciudades.index(siguiente_ciudad) ])
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
            # mejor hormiga global
            self.actualizacion_offline(list_routes, costos_rutas)
            # self.feromonas =  self.fparciales(list_routes, costos_rutas)
            print('NUEVA TABLA DE FEROMONAS')
            print(tabulate(self.feromonas, headers=self.ciudades, showindex=self.ciudades, tablefmt='grid'))

    def seleccionar_intensificacion(self, tramos, ciudades):
        """Selecciona las siguientes ciudades que elegirá la hormiga por diversificación
            Args:
                tramos (list): Todos los tramos posibles que una hormiga puede presentar
                ciudades (list): Pila de ciudades disponibles
            Returns:
            char: Siguiente ciudad
        """
        print('FUNCION SELECCIONAR POR INTENSIFICACION')
        excel = np.array([])
        for tramo in tramos:
            tij = self.feromonas[self.ciudades.index(tramo[0]), self.ciudades.index(tramo[1])]
            nij = self.visibilidad[self.ciudades.index(tramo[0]), self.ciudades.index(tramo[1])]
            tijxnij = (tij ** self.alfa) * (nij ** self.beta)
            # print('========================')
            # print(tij)
            # print(nij)
            # print(tijxnij)
            row = np.array([tij, nij, tijxnij])
            excel = np.append(excel, row, axis=0)
            # excel = np.concatenate((excel, row))
        # print(np.size(tramos))
        # print(tramos[0])
        excel = np.reshape(excel, (np.size(tramos) // 2, 3))
        print('IMPRIMIR TRAMOS NUMPY')
        # print(excel.shape)
        sumatoria = np.sum(excel[:, -1])
        # print(excel)
        pij = excel[:, -1] / sumatoria
        pij = np.reshape(pij, (np.size(tramos) // 2, 1))
        # ruleta = np.cumsum(pij, axis=0)
        # print(pij)
        # print(ruleta)
        excel = np.append(excel, pij, axis=1)
        # excel = np.append(excel, ruleta, axis=1)
        numpy_header = ['i', 'j', 'ti', 'nij', 'tij*nij', 'Pij']
        print(tabulate(np.append(np.reshape(tramos, (np.size(tramos) // 2, 2)), excel, axis=1), tablefmt='grid',
                       headers=numpy_header))  # version 1
        # print(excel) # version 2
        print('Sumatoria Pij: ', sumatoria)

        indice = np.argmax(excel[:, -1], axis=0) # extrae el indice del mayor valor

        sig_ciudad = tramos[indice][-1] #indice de la siguiente ciudad , recordar que tramo es [origen, destino]
        print('indice:', indice)
        print('Siguiente ciudad: ', sig_ciudad)
        print()
        return sig_ciudad

        # aleatorio = random.uniform(0, 1)
        # print('Número aleatorio: ', aleatorio)
        # # indice = np.where(excel[:,-1] <= aleatorio)[0][-1]
        # indice = np.where(aleatorio <= excel[:, -1])[0][0]  # extrae el primer indice del array de indices
        # sig_ciudad = tramos[indice][-1] #indice de la siguiente ciudad , recordar que tramo es [origen, destino]
        # print('indice: ', indice)
        # print('Siguiente ciudad', sig_ciudad)
        # print()
        # return sig_ciudad


    def seleccionar_diversificacion(self, tramos, ciudades):
        """Selecciona las siguientes ciudades que elegirá la hormiga por diversificación
        Args:
            tramos (list): Todos los tramos posibles que una hormiga puede presentar
            ciudades (list): Pila de ciudades disponibles
        Returns:
            char: Siguiente ciudad
        """
        print('FUNCION SELECCIONAR POR DIVERSIFICACION')
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

    def get_step_indexes(self, i, j, max_ruta, costos):
        """ Obtiene los indices por donde pasa la hormiga
        Args:
            i (int): indice x
            j (int): indice y
            max ruta (list): maxima ruta
            costos (list): lista de los costos
        Returns:
            list: lista de indices
        """
        # cant_hormigas = len(costos)
        a = self.ciudades[i]
        b = self.ciudades[j]
        indices = []
        string_ruta = ''
        for w in max_ruta:
            string_ruta = ''.join(w)
        if (a+b) in string_ruta:
            indices.append(i)
            indices.append(j)
        return indices




    def actualizacion_offline(self, list_routes, costos_rutas):
        maximo = np.max(costos_rutas)
        indice = np.where(costos_rutas == maximo)[0][0]
        print(indice)
        print('Ruta del máximo global: ', list_routes[indice])
        print('Costo máximo global: ', maximo)

        self.feromonas *= (1 - self.p)
        second = np.copy(self.feromonas) * 0
        max_ruta = list_routes[indice]

        i = 0
        while i < len(self.feromonas[0]):
            j = i + 1
            while j < len(self.feromonas[0]):
                if [i,j] == self.get_step_indexes(i, j, max_ruta, costos_rutas):
                    self.feromonas[i, j] += self.feromonas[i,j]*self.p
                    self.feromonas[j, i] += self.feromonas[j,i]*self.p
                j += 1
            i += 1


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

print('PARAMETROS')
# Constantes
print('feromona inicial', fi)
print('valor alfa: ', alfa)
print('valor beta:', beta)
print('valor de p: ', p)
print('constante Q: ', Q)
print('cantidad de hormigas: ', ant_cant)
print('q0: ', q0)
print('constante phi: ', phi)
print('iteraciones: ', iters)

ant_system = AntSystem(tabla_rutas, fi, alfa, beta, p, Q, ant_cant, phi, q0, iters, 'A')

ant_system.exe()
