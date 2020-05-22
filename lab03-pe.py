# Implementa los Algoritmo de Programación Evolutva para la predicción de la siguiente secuencia climatológica (0: Nublado; 1: Soleado):
#                                             0111001010011100101001110010100111001010
# * Utilice como máximo 5 estados.
# * Utilice por lo menos 8 individuos en la población y como máximo 16.
# * Muestre los parámetros utilizados.
# * Muestre la población inicial.
# * Muestre la aptitud de los individuos en cada iteración.
# * Utilice por lo menos 6 tipos de mutación. En caso no usar las definidas en teória, indicarlas.
# * Muestre todos los puntos importantes para cada proceso de mutación.
# * Los demás parámetros los puede definir Ud.
# * A continuación se muestra una posible solución:


# generar individuos aleatorios que son mef
# calcular sus aptitudes

# empezar a iterar x veces
#     mutar cada individuo a un descendiente
#     terminado de mutar a los descendientes se empieza a calcular las aptitudes de todos
#     unir los mejores ascendentes y mejores descendientes
#     tenemos nueva poblacion
# termina bucle 

#LIBRERIAS
import pydot
from graphviz import Digraph
import random 
import math 

max_states = 5
min_size_pop = 8 # o 16
max_size_pop = 16

climate_sequence = '0111001010011100101001110010100111001010'

states = {'A', 'B', 'C', 'D', 'E'}

individuo = '20110BC10101DE10111BA10100CD00111DB'
individuo2 = '00111CC00100AD00100ED20101CD00110DD'

def divide_sequence(individuo):
    """ Divide la secuencia de un individuo o de un MEF en partes pertenecientes a cada estado para un total de 5 estados(A,B,C,D,E) """
    a = individuo[0:7]
    b = individuo[7:14]
    c = individuo[14:21]
    d = individuo[21:28]
    e = individuo[28:35]
    return a,b,c,d,e

def validate_state(vortex):
    """ state = 0:no activo, 1:activo, 2:estado inicial. input 1/2: entrada 0/1. output 1/2: salida 0/1. pointer 1/2: conjunto de estados adyacentes - retorna true o false"""
    state = ['0', '1', '2']
    input_1 = ['0', '1']
    input_2 = ['0', '1']
    output_1 = ['0', '1']
    output_2 = ['0', '1']
    pointer_1 = ['A','B','C','D','E']
    pointer_2 = ['A','B','C','D','E']
    if((vortex[0] in state) and (vortex[1] in input_1) and (vortex[2] in input_2) and (vortex[3] in output_1) and (vortex[4] in output_2) and (vortex[5] in pointer_1) and (vortex[6] in pointer_2)):
        return True    
    else:
        return False

def one_initial_state_v2(individuo):
    """ Solo debe tener un estado inicial """
    size_ind = len(individuo)
    count = 0
    i = 0
    while i < size_ind:
        if individuo[i] == '2':
            count += 1
        i += 7
    if count == 1:
        return True
    else:
        return False

def count_active_states(individuo):
    """ cuenta la cantidad de estados activos en un individuo o mef incluyendo el estado inicial """
    size_ind = len(individuo)
    count = 0
    i = 0
    while i < size_ind:
        if individuo[i] in ['1', '2']:
            count += 1
        i += 7 
    return count
    
def one_initial_state(individuo):
    """ Es para confirmar que el individuo o MEF solo tenga un estado inicial, no puede tener mas de uno, retorna true o false """
    counter = individuo.count('2')
    if counter == 1:
        return True
    else:
        return False

def validate_inputs_state(individuo):
    """ Valida que las entradas sean diferentes, no puede haber 2 ceros como entradas ni 2 unos como entradas """
    size_ind = len(individuo)
    i = 1
    flag = True
    while ((i < size_ind)) :
        if (individuo[i] == individuo[i+1]):
            flag = False
            break
        i += 7
    return flag

def validate_mef(individuo):
    """ Valida la secuencia de un individuo o de un MEF dentro de los parametros asignados - retorna true o false"""
    a,b,c,d,e = divide_sequence(individuo)
    if one_initial_state(individuo) == True and one_initial_state_v2(individuo) and validate_inputs_state(individuo) == True and count_active_states(individuo) > 2 :
        if (validate_state(a) and validate_state(b) and validate_state(c) and validate_state(d) and validate_state(e)):
            return True
        else: 
            return False
    else:
        return False

def save_plots_pop(pop):
    """ Guarda en archivos gv los individuos o grafos generados de la poblacion """
    n = len(pop)
    for i in range(n):
        raw_file = 'fsm'+str(i)+'.gv'
        plotdot(pop[i], raw_file)

def plotdot(individuo, filen):
    """ Grafica la maquina de estado finito dada en el argumento y lo guarda en PNG """
    a,b,c,d,e = divide_sequence(individuo)
    # ACTIVE | INPUT 1 | INPUT 2 | OUTPUT 1 | OUTPUT 2 | NODE 1 | NODE 2
    S = ''
    
    if '2' in a:
        S = 'A'
    elif '2' in b:
        S = 'B'
    elif '2' in c:
        S = 'C'
    elif '2' in d:
        S = 'D'
    elif '2' in e:
        S = 'E'
    else:
        pass

    # f = Digraph('finite_state_machine', filename="fsm.gv")
    f = Digraph('finite_state_machine', filename=filen)
    f.attr(rankdir='LR', size='8,5')

    f.attr('node', shape='circle')
    f.node('A')
    f.node('B')
    f.node('C')
    f.node('D')
    f.node('E')

    f.attr('node', shape='point')
    f.node('q1')

    f.edge('q1', S, label='')

    f.edge('A', a[5], label=a[1]+' - '+a[3])
    f.edge('A', a[6], label=a[2]+' - '+a[4])

    f.edge('B', b[5], label=b[1]+' - '+b[3])
    f.edge('B', b[6], label=b[2]+' - '+b[4])

    f.edge('C', c[5], label=c[1]+' - '+c[3])
    f.edge('C', c[6], label=c[2]+' - '+c[4])

    f.edge('D', d[5], label=d[1]+' - '+d[3])
    f.edge('D', d[6], label=d[2]+' - '+d[4])

    f.edge('E', e[5], label=e[1]+' - '+e[3])
    f.edge('E', e[6], label=e[2]+' - '+e[4])

    # f.view()
    f.save()
    # /EN TERMINAL/  dot -Tpdf -O fsm.gv

def generate_random_individuo():
    """ Genera aleatoriamente un individuo o MEF"""
    # 2 01 10 BC - 10101DE - 10111BA - 10100CD - 00111DB
    graph = ''
    for i in range(max_states):
        condition = random.randint(0,2)
        inputs = '01'
        outputs = [random.randint(0,1), random.randint(0,1)]
        next_states = [chr(random.randint(65,69)) for i in range(2)]
        graph += str(condition) + inputs + str(outputs[0]) + str(outputs[1]) + str(next_states[0]) + str(next_states[1])
    return graph

def recursive_mef(ind):
    """Genera recursivamente un indiviudo válido
    Arguments:
        ind {string} -- individuo de tipo string que representa una maquina de estado finito
    Returns:
        string -- un indiviudo válido
    """
    if(validate_mef(ind)):
        return ind
    return recursive_mef(generate_random_individuo())

def generate_population(cant):
    """Genera aleatoriamente la cantidad de individuos para conformar una poblacion inicial
    Arguments:
        cant {int} -- cantidad de individuos
    """
    list_of_inds = []
    for i in range(cant):
        inds = generate_random_individuo()
        print("imprimiendo individuo: ", i)
        list_of_inds.append(recursive_mef(inds))
    return list_of_inds


def main():
    """Función principal
    """
    init_pop = generate_population(max_size_pop)
    print(init_pop)
    save_plots_pop(init_pop)


main()


# print(generate_population(min_size_pop))

# print(generate_random_individuo(1))

# print(count_active_states(individuo))

# # print(validate_mef(individuo))

# print(one_initial_state(individuo))

# print(validate_inputs_state(individuo))

# print(validate_mef(individuo2))

# plotdot(individuo)
