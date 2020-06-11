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

###############################################################
tsp = {'A': {'B': 22, 'C': 47, 'D':15, 'E':63}, 'B':{'A':22, 'C':18, 'D':62, 'E':41}}

print(tsp['A'])



