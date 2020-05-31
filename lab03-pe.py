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

# LIBRERIAS
import pydot
from graphviz import Digraph
import random
import math

max_states = 5
min_size_pop = 8  # o 16
max_size_pop = 16

climate_sequence = '0111001010011100101001110010100111001010'

states = ['A', 'B', 'C', 'D', 'E']

individuo = '20110BC10101DE10111BA10100CD00111DB'
individuo2 = '00111CC00100AD00100ED20101CD00110DD'


def divide_sequence(individuo):
    """ Divide la secuencia de un individuo o de un MEF en partes pertenecientes a cada estado para un total de 5 estados(A,B,C,D,E) """
    a = individuo[0:7]
    b = individuo[7:14]
    c = individuo[14:21]
    d = individuo[21:28]
    e = individuo[28:35]
    return a, b, c, d, e


def validate_state(vortex):
    """ state = 0:no activo, 1:activo, 2:estado inicial. input 1/2: entrada 0/1. output 1/2: salida 0/1. pointer 1/2: conjunto de estados adyacentes - retorna true o false"""
    state = ['0', '1', '2']
    input_1 = ['0', '1']
    input_2 = ['0', '1']
    output_1 = ['0', '1']
    output_2 = ['0', '1']
    pointer_1 = ['A', 'B', 'C', 'D', 'E']
    pointer_2 = ['A', 'B', 'C', 'D', 'E']
    if ((vortex[0] in state) and (vortex[1] in input_1) and (vortex[2] in input_2) and (vortex[3] in output_1) and (
            vortex[4] in output_2) and (vortex[5] in pointer_1) and (vortex[6] in pointer_2)):
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
    while ((i < size_ind)):
        if (individuo[i] == individuo[i + 1]):
            flag = False
            break
        i += 7
    return flag


def validate_mef(individuo):
    """ Valida la secuencia de un individuo o de un MEF dentro de los parametros asignados - retorna true o false"""
    a, b, c, d, e = divide_sequence(individuo)
    if one_initial_state(individuo) == True and one_initial_state_v2(individuo) and validate_inputs_state(
            individuo) == True and count_active_states(individuo) > 3:  # modificado el count_active_states de 2 -> 3
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
        raw_file = 'fsm' + str(i) + '.gv'
        plotdot(pop[i], raw_file)


def plotdot(individuo, filen):
    """ Grafica la maquina de estado finito dada en el argumento y lo guarda en PNG """
    a, b, c, d, e = divide_sequence(individuo)
    # ACTIVE | INPUT 1 | INPUT 2 | OUTPUT 1 | OUTPUT 2 | NODE 1 | NODE 2
    nodes = ['A', 'B', 'C', 'D', 'E']
    states_array = [a, b, c, d, e]
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

    f.attr('node', shape='point')
    f.node('q1')

    i = 0
    j = 0
    f.attr('node', shape='circle')
    while (i < len(individuo)):
        if (individuo[i] == '0'):
            f.node(nodes[j], color="red")
        else:
            f.node(nodes[j], color="blue")
        i += 7
        j += 1

    f.edge('q1', S, label='')
    ii = 0
    jj = 0
    while (ii < len(individuo)):
        if (individuo[ii] == '0'):
            f.edge(nodes[jj], states_array[jj][5], label=states_array[jj][1] + ' - ' + states_array[jj][3], color="red")
            f.edge(nodes[jj], states_array[jj][6], label=states_array[jj][2] + ' - ' + states_array[jj][4], color="red")
        else:
            f.edge(nodes[jj], states_array[jj][5], label=states_array[jj][1] + ' - ' + states_array[jj][3],
                   color="blue")
            f.edge(nodes[jj], states_array[jj][6], label=states_array[jj][2] + ' - ' + states_array[jj][4],
                   color="blue")
        ii += 7
        jj += 1
    #####################################
    # f.node('A')
    # f.node('B')
    # f.node('C')
    # f.node('D')
    # f.node('E')
    # f.attr('node', shape='point')
    # f.node('q1')

    # f.edge('q1', S, label='')

    # f.edge('A', a[5], label=a[1]+' - '+a[3])
    # f.edge('A', a[6], label=a[2]+' - '+a[4])

    # f.edge('B', b[5], label=b[1]+' - '+b[3])
    # f.edge('B', b[6], label=b[2]+' - '+b[4])

    # f.edge('C', c[5], label=c[1]+' - '+c[3])
    # f.edge('C', c[6], label=c[2]+' - '+c[4])

    # f.edge('D', d[5], label=d[1]+' - '+d[3])
    # f.edge('D', d[6], label=d[2]+' - '+d[4])

    # f.edge('E', e[5], label=e[1]+' - '+e[3])
    # f.edge('E', e[6], label=e[2]+' - '+e[4])
    #####################################

    # f.view()
    f.save()
    # /EN TERMINAL/  dot -Tpdf -O fsm.gv


def generate_random_individuo():
    """ Genera aleatoriamente un individuo o MEF"""
    # 2 01 10 BC - 10101DE - 10111BA - 10100CD - 00111DB
    graph = ''
    for i in range(max_states):
        condition = random.randint(0, 2)
        inputs = '01'
        outputs = [random.randint(0, 1), random.randint(0, 1)]
        next_states = [chr(random.randint(65, 69)) for i in range(2)]
        graph += str(condition) + inputs + str(outputs[0]) + str(outputs[1]) + str(next_states[0]) + str(next_states[1])
    return graph


def recursive_mef(ind):
    """Genera recursivamente un indiviudo válido
    Arguments:
        ind {string} -- individuo de tipo string que representa una maquina de estado finito
    Returns:
        string -- un indiviudo válido
    """
    if (validate_mef(ind)):
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
        list_of_inds.append(recursive_mef(inds))
    return list_of_inds


def internal_mef(state, input):
    """procesado interno del mef
    Arguments:
        state {string} -- valor de el diccionario con clave state
        input {char} -- entrada, puede ser 1 o 0
    Returns:
        char, char -- salida de un estado , estado objetivo
    """
    output = ''
    new_state = ''
    if (input == state[1]):
        output = state[3]
        new_state = state[5]
    if (input == state[2]):
        output = state[4]
        new_state = state[6]
    return output, new_state


def mef(sinput, ind, table, sinit):
    """maquina de estado finito que calcula la cadena de salida dado la cadena de entrada y sus estados
    Arguments:
        sinput {string} -- secuencia de entrada dado por el enunciado
        ind {string} -- individuo 
        table {dict} -- diccionario con key=estados, values=secuencia perteneciente a ese estado
        sinit {char} -- estado inicial
    Returns:
        string -- Secuencia de salida
    """
    input_size = len(sinput)
    soutput = ''
    s_actual = sinit
    for i in range(input_size):
        op, ns = internal_mef(table[s_actual], sinput[i])
        s_actual = ns
        soutput += op
        # print('Estado actual: ', s_actual)
        # print('Salidas: ', soutput)
    return soutput


def calc_seq_out(sec, ind):
    """Calcula la secuencia de salida dada la secuencia de entrada y un individuo

    Arguments:
        sec {string} -- Secuencia de entrada dada por el enunciado
        ind {string} -- Individuo generado aleatoriamente

    Returns:
        string -- Secuencia de salida
    """
    a, b, c, d, e = divide_sequence(ind)
    calc = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e}
    sec_in = sec
    # seq_out =
    print("calc - tabla de estados")
    print(calc)
    S = ''
    if (ind[0] == '2'):
        S = 'A'
    elif (ind[7] == '2'):
        S = 'B'
    elif (ind[14] == '2'):
        S = 'C'
    elif (ind[21] == '2'):
        S = 'D'
    elif (ind[28] == '2'):
        S = 'E'
    else:
        pass
    sec_out = mef(sec_in, ind, calc, S)
    return sec_out


def fitness(secuencia, individuo):
    """Calcula la aptitud de un individuo
    Arguments:
        secuencia {string} -- secuencia de entrada conformada de 1s y 0s
        individuo {string} -- indiviudo conformado por maquina de estados finitos deterministas
    Returns:
        float -- retorna un valor float como el valor de aptitud del individuo
    """
    seq_in = secuencia
    seq_out = calc_seq_out(seq_in, individuo)
    size_ind = len(individuo)
    size_seq = len(seq_in)
    matchs = 0
    i = 1
    while (i < size_seq):
        if (seq_in[i] == seq_out[i - 1]):
            matchs += 1
        i += 1
    print("\n=====================================================================================")
    print("OPERACIÓN: CALCULAR FITNESS")
    print("SECUENCIA DE ENTRADA:\t", seq_in)
    print("SECUENCIA DE SALIDA:\t", seq_out)

    return matchs / (size_seq - 1)


#############################################################################################################
def processor(func, ind, stat, type):
    """
    procesa los diferentes tipos demutacion
    Arguments:
         func {funcion} --  funcion ingresada como argumento
         ind {string}   --  individuo
         stat {char}    --  estado seleccionado
         type {int}     --  typo de mutacion
    Returns:
        string          --  nuevo individuo mutado
    """
    new_ind = ''
    a, b, c, d, e = func(ind)
    a, b, c, d, e = list(a), list(b), list(c), list(d), list(e)

    if type == 1:
        if stat == 'A':
            print(a)
            if a[0] == '2':  # revisar, no es correcto
                a[0] = '0'
                b[0] = '2'
            else:
                a[0] = '0'
        if stat == 'B':
            print(b)
            if b[0] == '2':  # revisar, no es correcto
                b[0] = '0'
                c[0] = '2'
            else:
                b[0] = '0'
        if stat == 'C':
            print(c)
            if c[0] == '2':  # revisar, no es correcto
                c[0] = '0'
                d[0] = '2'
            else:
                c[0] = '0'
        if stat == 'D':
            print(d)
            if d[0] == '2':  # revisar, no es correcto
                d[0] = '0'
                e[0] = '2'
            else:
                d[0] = '0'
        if stat == 'E':
            print(e)
            if e[0] == '2':  # revisar, no es correcto
                e[0] = '0'
                a[0] = '2'
            else:
                e[0] = '0'
        new_ind = a + b + c + d + e
    if type == 2:
        if a[0] == '2':
            a[0] = '1'
        elif b[0] == '2':
            b[0] = '1'
        elif c[0] == '2':
            c[0] = '1'
        elif d[0] == '2':
            d[0] = '1'
        elif e[0] == '2':
            e[0] = '1'
        else:
            pass

        if stat == 'A':
            print(a)
            a[0] = '2'
        if stat == 'B':
            print(b)
            b[0] = '2'
        if stat == 'C':
            print(c)
            c[0] = '2'
        if stat == 'D':
            print(d)
            d[0] = '2'
        if stat == 'E':
            print(e)
            e[0] = '2'
        new_ind = a + b + c + d + e
    if type == 3:
        if stat == 'A':
            print(a)
            if a[1] == '0':
                a[1] = '1'
                if a[2] == '0':
                    a[2] = '1'
                else:
                    a[2] = '0'
            else:
                a[1] = '0'
                if a[2] == '0':
                    a[2] = '1'
                else:
                    a[2] = '0'
        if stat == 'B':
            print(b)
            if b[1] == '0':
                b[1] = '1'
                if b[2] == '0':
                    b[2] = '1'
                else:
                    b[2] = '0'
            else:
                b[1] = '0'
                if b[2] == '0':
                    b[2] = '1'
                else:
                    b[2] = '0'
        if stat == 'C':
            print(c)
            if c[1] == '0':
                c[1] = '1'
                if c[2] == '0':
                    c[2] = '1'
                else:
                    c[2] = '0'
            else:
                c[1] = '0'
                if c[2] == '0':
                    c[2] = '1'
                else:
                    c[2] = '0'
        if stat == 'D':
            print(d)
            if d[1] == '0':
                d[1] = '1'
                if d[2] == '0':
                    d[2] = '1'
                else:
                    d[2] = '0'
            else:
                d[1] = '0'
                if d[2] == '0':
                    d[2] = '1'
                else:
                    d[2] = '0'
        if stat == 'E':
            print(e)
            if e[1] == '0':
                e[1] = '1'
                if e[2] == '0':
                    e[2] = '1'
                else:
                    e[2] = '0'
            else:
                e[1] = '0'
                if e[2] == '0':
                    e[2] = '1'
                else:
                    e[2] = '0'
        new_ind = a + b + c + d + e
    if type == 4:
        if stat == 'A':
            print(a)
            if a[3] == '0':
                a[3] = '1'
            else:
                a[3] = '0'
        if stat == 'B':
            print(b)
            if b[3] == '0':
                b[3] = '1'
            else:
                b[3] = '0'
        if stat == 'C':
            if c[3] == '0':
                c[3] = '1'
            else:
                c[3] = '0'
            print(c)
        if stat == 'D':
            print(d)
            if d[3] == '0':
                d[3] = '1'
            else:
                d[3] = '0'
        if stat == 'E':
            print(e)
            if e[3] == '0':
                e[3] = '1'
            else:
                e[3] = '0'
        new_ind = a + b + c +d +e
    if type == 5:
        if stat == 'A':
            print(a)
            a[random.randint(5, 6)] = states[int(random.randint(0, max_states-1))]
        if stat == 'B':
            print(b)
            b[random.randint(5, 6)] = states[int(random.randint(0, max_states - 1))]
        if stat == 'C':
            print(c)
            c[random.randint(5, 6)] = states[int(random.randint(0, max_states - 1))]
        if stat == 'D':
            print(d)
            d[random.randint(5, 6)] = states[int(random.randint(0, max_states - 1))]
        if stat == 'E':
            print(e)
            e[random.randint(5, 6)] = states[int(random.randint(0, max_states - 1))]
        new_ind = a + b + c + d + e
    # if type == 6:
    #     if stat == 'A':
    #         print(a)
    #     if stat == 'B':
    #         print(b)
    #     if stat == 'C':
    #         print(c)
    #     if stat == 'D':
    #         print(d)
    #     if stat == 'E':
    #         print(e)
    #     new_ind = a + b + c + d + e

    return ''.join(map(str, new_ind))


def type_1(indi):  # desactivar 1 estado
    print("# desactivar 1 estado")
    print("## INDIVIDUO: ", indi)
    r = random.randint(0, max_states - 1)
    print("ESTADO ELEGIDO ALEATORIAMENTE: ", states[int(r)])
    new_indi = processor(divide_sequence, indi, states[int(r)], 1)  # 1 es el tipo de mutacion elegida
    # print(list([char for char in a]))
    print(new_indi)
    return new_indi


def type_2(indi):  # cambiar estado inicial
    print("# cambiar estado inicial")
    print("## INDIVIDUO: ", indi)
    r = random.randint(0, max_states - 1)
    print("ESTADO ELEGIDO ALEATORIAMENTE: ", states[int(r)])
    new_indi = processor(divide_sequence, indi, states[int(r)], 2)  # 2 es el tipo de mutacion elegida
    print(new_indi)
    return new_indi


def type_3(indi):  # cambiar simbolos de entrada
    print("# cambiar simbolos de entrada")
    print("## INDIVIDUO: ", indi)
    r = random.randint(0, max_states - 1)
    print("ESTADO ELEGIDO ALEATORIAMENTE: ", states[int(r)])
    new_indi = processor(divide_sequence, indi, states[int(r)], 3)  # 3 es el tipo de mutacion elegida
    print(new_indi)
    return new_indi


def type_4(indi):  # cambiar 1 simbolo de salida
    print("# cambiar 1 simbolo de salida")
    print("## INDIVIDUO: ", indi)
    r = random.randint(0, max_states - 1)
    print("ESTADO ELEGIDO ALEATORIAMENTE: ", states[int(r)])
    new_indi = processor(divide_sequence, indi, states[int(r)], 4)  # 4 es el tipo de mutacion elegida
    print(new_indi)
    return new_indi


def type_5(indi):  # cambiar 1 estado de salida
    print("# cambiar 1 estado de salida")
    print("## INDIVIDUO: ", indi)
    r = random.randint(0, max_states - 1)
    print("ESTADO ELEGIDO ALEATORIAMENTE: ", states[int(r)])
    new_indi = processor(divide_sequence, indi, states[int(r)], 5)  # 5 es el tipo de mutacion elegida
    print(new_indi)
    return new_indi


def type_6(indi):  # activar 1 estado
    print("# activar 1 estado \n Buscando estados desactivados")
    print("## INDIVIDUO: ", indi)
    chain = indi[0:len(indi):7]
    indi = list(indi)
    i = 0
    for char in chain:
        if char == '0':
            indi[int(7*i)] = '1'
            break
        i += 1
    indi = ''.join(map(str, indi))
    print(indi)
    return indi


def mutation_operator(population):
    """Operador de mutación, a partir de esta función se genera los descendientes del individuo
    Arguments:
        population {list(string)} -- poblacion actual
    Returns:
        list(string) -- poblacion de descendientes
    """
    print("INICIANDO PROCESO DE MUTACIÓN")
    new_p = []
    mutant = ''
    for i in range(len(population)):
        rand_number = random.uniform(0, 1)
        print("### MUTACIÓN DEL INDIVIDUO N°: ", i)
        print("* Numero aleatorio: ", rand_number)
        if (rand_number > 0.0 and rand_number < 0.1):
            mutant = type_1(population[i])
        elif (rand_number > 0.1 and rand_number < 0.3):
            mutant = type_2(population[i])
        elif ((rand_number > 0.3 and rand_number < 0.5)):
            mutant = type_3(population[i])
        elif (rand_number > 0.5 and rand_number < 0.7):
            mutant = type_4(population[i])
        elif (rand_number > 0.7 and rand_number < 0.9):
            mutant = type_5(population[i])
        elif (rand_number > 0.9 and rand_number < 1.0):
            mutant = type_6(population[i])
        new_p.append(mutant)
    return new_p


def merge_asc_desc(ascends, descends):
    print("UNIENDO ASCENDENTES Y DESCENDENTES")
    asc = []
    des = []
    merged = []
    new_size = int(max_size_pop/2)
    print(len(ascends))
    print(len(descends))
    for ind in ascends:
        asc.append([ind, fitness(climate_sequence, ind)])
        #ord = sorted(asc, key=lambda x: x[2])  # para ordenar
    for ind in descends:
        des.append([ind, fitness(climate_sequence, ind)])
    print("#############COMPLETO ########################")
    print(asc)
    print("#############DIVIDIDO########################")
    asc_ord = sorted(asc, key=lambda x:x[1])
    asc_ord = asc_ord[new_size::1]
    print(asc_ord)
    ##############################################################
    print("#############COMPLETO ########################")
    print(des)
    print("#############DIVIDIDO########################")
    des_ord = sorted(des, key=lambda x: x[1])
    des_ord = des_ord[new_size::1]
    print(des_ord)
    ##########################################################
    for i in range(new_size):
        merged.append(asc_ord[i][0])
        merged.append(des_ord[i][0])
    return merged


def main():
    """Función principal"""
    init_pop = generate_population(max_size_pop)
    print("··························POBLACIÓN INICIAL·······················")
    print('POBLACION INICIAL', init_pop)
    print('APTITUD del primer individuo: ', fitness(climate_sequence, init_pop[0]))
    # save_plots_pop(init_pop)
    actual_pop = init_pop
    for i in range(10): #iteraciones (i)
        print("\n\n================================================ ITERACIÓN ", i)
        childs = mutation_operator(actual_pop)
        print('ASCENDIENTES: ', actual_pop)
        print('DESCENDIENTES: ', childs)
        actual_pop = merge_asc_desc(actual_pop, childs)  # evaluar fitness aqui
        print('NUEVA POBLACION: ', actual_pop)


main()

# print(generate_population(min_size_pop))

# print(generate_random_individuo(1))

# print(count_active_states(individuo))

# # print(validate_mef(individuo))

# print(one_initial_state(individuo))

# print(validate_inputs_state(individuo))

# print(validate_mef(individuo2))

# plotdot(individuo)
