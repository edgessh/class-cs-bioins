NUEVA_POBLACION = ['10100DA10110EC20110CD10111BE10100CA', '10100DA00110EC20110CD10111BE11000CA', '10100DA00110EC20110CD10111BE10100CA', '11000DA10110EC20110CD10111BE00110CA', '10100DA10110AC20110CD10111BE10100CA', '10100DA10110EC20110CD10111BE10110CA', '10100DA10110EC20110CD10111BE10110CA', '10100DA10110AC20110CD10111BE00100CA', '00100DA10110EC20110CD10111BE10100CA', '10100DA10110EC20110CD10111BE10110CA', '10100DA20100EC10110DD10111BE10100CA', '00100DA10110EC20110CD10111BE00100CA', '10100DA20110EC00110DD10111BE10100CA', '10100DA20100EC10110DD10111BE10100CA', '10100DA20110EC10110DD10111BE10100CA', '20100DA10110EC00110DD10111BE10100CA']

from graphviz import Digraph
import pydot


def divide_sequence(individuo):
    """ Divide la secuencia de un individuo o de un MEF en partes pertenecientes a cada estado para un total de 5 estados(A,B,C,D,E) """
    a = individuo[0:7]
    b = individuo[7:14]
    c = individuo[14:21]
    d = individuo[21:28]
    e = individuo[28:35]
    return a, b, c, d, e


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


save_plots_pop(NUEVA_POBLACION)