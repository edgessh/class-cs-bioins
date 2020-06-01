# Implemente un Algoritmo de Programación Genética para encontrar una función matemática que se ajuste al siguiente
# conjunto de entradas y salidas:
#
# Input Output
# 0       0
# 0.1     0.005
# 0.2     0.02
# 0.3     0.045
# 0.4     0.08
# 0.5     0.125
# 0.6     0.18
# 0.7     0.245
# 0.8     0.32
# 0.9     0.405
#
# Tamaño de la población: 8 individuos.
# Cantidad de genes: 7 .
# Funciones: +; −; ∗; /
# Terminales (Constantes): −5; −4; −3; −2; −1; 1; 2; 3; 4; 5
# Terminales (Variables): X
# Probabilidad de Reproducción: 20%
# Selección para Reproducción: Torneo 3
# Probabilidad de Cruzamiento: 40%
# Selección para Cruzamiento: Torneo 2
# Cruzamiento de un Punto (Punto Aleatorio)
# En el caso de que solo quede un espacio en la nueva población y se debe realizar un Cruzamiento, escoger aleatoriamente un descendiente para la nueva población.
# Probabilidad de Mutación: 40%
# Selección para Mutación: Torneo 3
# Mutación simple.
# Utilce el ECM como función de aptitud.
# Muestre con detalle el cálculo de la aptitud.
# Muestre con detalle la selección en la reproducción, cruzamiento y mutación.
# Muestre con detalle el resultado de la reproducción, cruzamiento y mutación.
# Utilice el caracter | como separador de genes en cada individuo.

# ---------------------------------------------------------------------------------------

#  LIBRERIAS
import random
import numpy as np

#  PARAMETROS
size_pop = 8
size_genes = 7
funciones = ['+', '-', '*', '/']
terminal_const = [str(n) for n in range(-5, 6) if n != 0]  # de -5 a 5
terminal_var = ['X']
prob_repro = 0.2
prob_cruz = 0.4
prob_mut = 0.4


#  crear poblacion inicial
#  evaluar aptitud
#  probabilidad de repro, cruz, muta
#  termimna el bucle


print('FUNCIONES: ', funciones)
print('TERMINALES: ', terminal_const + terminal_var)

tableIO = [[0, 0],
           [0.1, 0.005],
           [0.2, 0.02],
           [0.3, 0.045],
           [0.4, 0.08],
           [0.5, 0.125],
           [0.6, 0.18],
           [0.7, 0.245],
           [0.8, 0.32],
           [0.9, 0.405]]


class Arbol(object):

    def __init__(self):
        self.izq = None
        self.der = None
        self.dato = None


    def insertar(self, funcs, term1, term2):
        terms = term1 + term2
        #  funciones
        self.dato = funcs[random.randint(0,len(funcs)-1)]
        self.izq = Arbol()
        self.izq.dato = funcs[random.randint(0,len(funcs)-1)]
        self.der = Arbol()
        self.der.dato = funcs[random.randint(0,len(funcs)-1)]
        #  terminales
        self.izq.izq = Arbol()
        self.izq.izq.dato = terms[random.randint(0, len(term1+term2)-1)]
        self.izq.der = Arbol()
        self.izq.der.dato = terms[random.randint(0, len(term1+term2)-1)]
        self.der.izq = Arbol()
        self.der.izq.dato = terms[random.randint(0, len(term1+term2)-1)]
        self.der.der = Arbol()
        self.der.der.dato = terms[random.randint(0, len(term1+term2)-1)]
        return self
    
    def leer(self):
        secuencia = [self.izq.izq.dato, self.izq.dato, self.izq.der.dato, self.dato, self.der.izq.dato, self.der.dato, self.der.der.dato]
        return secuencia

# individuo = Arbol()
# individuo.insertar(funciones, terminal_const, terminal_var)
# ind_sec = individuo.leer()
# print(ind_sec)

def fun(op, v1, v2):
    """  funcion que suma, resta, multi o divide a dos parametros """
    if op == '+':
        return v1+v2
    elif op == '-':
        return v1-v2
    elif op == '*':
        return v1*v2
    elif op == '/':
        return v1

def validar_no_div_zero(indi):
    """ valida que no haya división por cero en el individuo """
    if indi[1] == '/' and indi[2] == '0':
        return False
    elif indi[5] == '/' and indi[6] == '0':
        return False
    elif indi[3] == '/' and indi[4] != 'X' and indi[6] != 'X' and fun( '/', int(indi[4]), int(indi[6])) == 0:
        return False
    else:
        return True


def generar_individuo_recursivo(individuo):
    """ genera un individuo recursivamente con el fin de que no haya división por cero en ello """
    individuo.insertar(funciones, terminal_const, terminal_var)
    if validar_no_div_zero(individuo.leer()):
        return individuo.leer()
    individuo = Arbol()
    return generar_individuo_recursivo(individuo)
    

def generar_poblacion():
    """ genera una poblacion de individuos """
    poblacion = []
    ind = Arbol()
    for i in range(size_pop):
        poblacion.append(generar_individuo_recursivo(ind))
    return poblacion


# poblacion inicial
pobl_ini = generar_poblacion()


def convertir_a_funcion(ind, param):
    """ convierte la secuencia del arbol en una función """
    op = {'+': lambda a,b:a+b, '-': lambda a,b:a-b, '*': lambda a,b: a*b, '/':lambda a,b: a/b}
    if 'X' not in ind:
        return op[ind[3]] ( op[ind[1]] (int(ind[0]), int(ind[2])), op[ind[5]] (int(ind[4]), int(ind[6])))
        # return op[ind[3]]( op[ind[1]](int(ind[0]), int(ind[2]))), op[ind[5]](int(ind[4]), int(ind[6]))
    else:
        indice = ind.index('X')
        if indice == 0:
            return op[ind[3]] ( op[ind[1]] (param, int(ind[2])), op[ind[5]] (int(ind[4]), int(ind[6])))
        elif indice == 2:
            return op[ind[3]] ( op[ind[1]] (int(ind[0]), param), op[ind[5]] (int(ind[4]), int(ind[6])))
        elif indice == 4:
            return op[ind[3]] ( op[ind[1]] (int(ind[0]), int(ind[2])), op[ind[5]] (param, int(ind[6])))
        elif indice == 6:
            return op[ind[3]] ( op[ind[1]] (int(ind[0]), int(ind[2])), op[ind[5]] (int(ind[4]), param))



print(pobl_ini[0])
print(convertir_a_funcion(pobl_ini[0], 1))
print('===================================')
def aptitud(tabla, pop):
    print('CALCULO DE APTITUDES')
    n = len(tabla)
    tab = tabla
    for ii in range (len(pop)):
        diffs = []
        print('INDIVIDUO: ', ii)
        for i in range (n):
            actual = convertir_a_funcion(pop[ii], tab[i][0])
            tab[i].append(actual)
            diffs.append(tab[i][1] - actual)
            tab[i].append(tab[i][1] - actual)
        print('individuo - secuencia: ', pop[ii])
        val = np.array(diffs)
        ap = np.sum(np.power(diffs, 2)) / n
        print('APTITUD = ', ap)
    

print(aptitud(tableIO, pobl_ini))






