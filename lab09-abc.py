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
SN = 3
f = lambda x, y: (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2

# Fuentes iniciales de alimentos
xy = [[random.uniform(-10, 10), random.uniform(-10, 10)] for i in range(SN)]
fuente = np.array(xy)



print(fuente)



