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

size_pop = 8
size_genes = 7
funciones = ['+', '-', '*', '/']
terminal_const = [n for n in range(-5, 6) if n != 0]  # de -5 a 5
terminal_var = 'X'
prob_repro = 0.2
prob_cruz = 0.4
prob_mut = 0.4


#  crear poblacion inicial
#  evaluar aptitud
#  probabilidad de repro, cruz, muta
#  termimna el bucle


print(funciones)
print(terminal_const)

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



def generar_individuos():
    pass