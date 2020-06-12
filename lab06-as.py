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
ant_cant = 4

###############################################################
data = {
    'A':{'B':12,'C':3,'D':23,'E':1,'F':5,'G':23,'H':56,'I':12,'J':11},
    'B':{'A':12,'C':9,'D':18,'E':3,'F':41,'G':45,'H':5,'I':41,'J':27},
    'C':{'A':3,'B':9,'D':89,'E':56,'F':21,'G':12,'H':48,'I':14,'J':29},
    'D':{'A':23,'B':18,'C':89,'E':87,'F':46,'G':75,'H':17,'I':50,'J':42},
    'E':{'A':1,'B':3,'C':56,'D':87,'F':55,'G':22,'H':86,'I':14,'J':33},
    'F':{'A':5,'B':41,'C':21,'D':46,'E':55,'G':21,'H':76,'I':54,'J':81},
    'G':{'A':23,'B':45,'C':12,'D':75,'E':22,'F':21,'H':11,'I':57,'J':48},
    'H':{'A':56,'B':5,'C':48,'D':17,'E':86,'F':76,'G':11,'I':63,'J':24},
    'I':{'A':12,'B':41,'C':14,'D':50,'E':14,'F':54,'G':57,'H':63,'J':9},
    'J':{'A':11,'B':27,'C':29,'D':42,'E':33,'F':81,'G':48,'H':24,'I':9}
}

class AntSystem:
    def __init__(self, _distancias, _fi, _alfa, _beta, _ro, _Q, _ant_cant):
        self.tsp = _distancias # d_ij
        self.fi = _fi
        self.alfa = _alfa
        self.beta = _beta
        self.ro = _ro
        self.Q = _Q
        self.ant_cant = _ant_cant
        self.feromonas = np.abs(np.identity(np.size(_distancias[0]), dtype=float) - 1) * _fi # t_ij
        self.indices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        self.visibilidad = 1 / _distancias # 1/(d_ij)

    def exe(self):
        print('Tabla de rutas TSP')
        print(tabulate(self.tsp, headers=self.indices, showindex=self.indices, tablefmt='grid', stralign='center'))
        print('\n\n Tabla de visibilidad')
        print(tabulate(self.visibilidad, headers=self.indices, showindex=self.indices, stralign='center', tablefmt='grid'))
        print('\n\n Tabla de feromonas')
        print(tabulate(self.feromonas, headers=self.indices, showindex=self.indices, stralign='center', tablefmt='grid'))





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

ant_system = AntSystem(tabla_rutas, fi, alfa, beta, ro, Q, ant_cant)

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


