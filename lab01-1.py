""" 
Implementa un Algoritmo Genético para minimizar la siguiente función. Considere los siguientes parámetros:
f „x;y” = − cos„x” × cos„y” × exp„−„x − π”2 − „y − π”2”
−10 ≤ x ≤ 10
−10 ≤ y ≤ 10 
------------------------
PARAMETROS:
- codificacion real de 2 genes
- menos de 5 decimales
- seleccion por torneo
- mutacion uniforme
- probabilidad de cruzamiento : 80%
- probabilidad de mutacion : 10%
- cruzamiento blx-0.5
- iteraciones o generaciones: 100



"""

import math
import numpy as np 
import random
import emoji

# numero de individuos
Number_individuals = 8
alfa = 0.5
minimun = -10.0
maximun = 10.0
filesaved = open("lab01-1.txt", 'a')

#poblacion inicial
# funcion que crea la poblacion inicial
def fillP(n):
    pop = np.array([])
    for i in range(0,8):
        xx = round(random.uniform(-10, 10), 5)
        yy = round(random.uniform(-10, 10), 5)

        pop = np.append(pop, [xx,yy])
    pop = np.reshape(pop, (Number_individuals, 2))
    return pop
#round(random.uniform(-10,10),5)]
Initial_population = fillP(Number_individuals)
# print("\nPOBLACION INICIAL\n")
# print(Initial_population)
# size of rows = 0, size of columns = 1
# print(np.size(Initial_population, 0))

# funcion f que se utiliza para calcular el fitness o aptitud
def f(x, y):
    return -1*math.cos(x)*math.cos(y)*math.exp(-1*(x-math.pi)**2 - (y-math.pi)**2)
# print(f(3,4))

# funcion para calcular el fitness de toda una poblacion
def Fitness(array):
    fit = np.array([])
    for item in array:
        fit = np.append(fit, f(item[0], item[1]))
    return fit
fitness_arrays = Fitness(Initial_population)
# print(fitness_arrays)
# seleccion por torneo
# print ("MATING POOL")

def fwinner(p1, p2):
    #gana el que tenga menor aptitud (minimizar funcion)
    _p1 = f(p1[0],p1[1])
    _p2 = f(p2[0], p2[1])
    print("Aptitudes → ", _p1 , " «» ", _p2)
    filesaved.write("Aptitudes")
    filesaved.write(str(_p1))
    filesaved.write(str(_p2))

    if(_p1 < _p2):
        return p1
    else:
        return p2
    

# competicion por torneo
def mating_pool(population):
    #seleccion de 8 peleas y 16 competidores
    i = 0
    new_selected = np.array([])
    while(i<Number_individuals):
        r1 = random.randint(0,Number_individuals-1) #cuidado con sobrepasar la numero de invidiuos [0 a 7]
        r2 = random.randint(0,Number_individuals-1)
        if(r1 != r2):
            print("Enfrentamiento: ", i)
            print(r1, "\U0001F19A", r2)
            print(population[r1,:] , "\U0001F93C", population[r2,:])
            filesaved.write("Enfrentamiento: ")
            filesaved.write(str(i))
            filesaved.write(str(r1))
            filesaved.write(str(r2))
            filesaved.write(str(population[r1,:]))
            filesaved.write(str(population[r2,:]))
            winner = fwinner(population[r1,:], population[r2,:])
            print("Ganador → ", winner)
            filesaved.write("Ganador: ")
            filesaved.write(str(winner))
            new_selected = np.append(new_selected, winner, 0)
            # print(population[r1,:])
            # print(" VS ")
            # print(population[r2,:])
            # print("i", i)
            i += 1        
        else:
            continue
    
    # print(population[0,:])
    # print(population[8,:])


    # print(population[0,:])
    new_selected = np.reshape(new_selected, (Number_individuals, 2))
    print(new_selected)
    filesaved.write(str(new_selected))
    return new_selected

# mating_pool(Initial_population)
# news_candidates = mating_pool(Initial_population)

#cruzamiento blx de los padres
def cross_blx(parent1, parent2):
    beta = round(random.uniform(-alfa, 1+alfa), 2)
    print("CROSS-BLX")
    print("BETA: ", beta)
    filesaved.write("CROSS-BLX")
    filesaved.write("BETA: ")
    filesaved.write(str(beta))
    # Cx = []
    Cx = np.array([])
    i = 0

    # print(parent1[0])
    # print(parent2[1])
    # for i in range(2):
    # var = parent1
    while(i < 2):
        var = parent1[i] + beta * (parent2[i]-parent1[i])
        if( var <= maximun and var >= minimun):
            # if(var <= maximun and var >= minimun):
            print("C_", i,": ", var)
            filesaved.write("C_")
            filesaved.write(str(i))
            filesaved.write(str(var))

            Cx = np.append(Cx, var)
            i += 1
        else:
            beta = round(random.uniform(-alfa, 1+alfa), 2)
            print("HIJO NO FACTIBLE / CALCULANDO NUEBA BETA: ", beta)
            filesaved.write("HIJO NO FACTIBLE / CALCULANDO NUEBA BETA: ")
            filesaved.write(str(beta))

                    
    return Cx


# seleccion de padres
def mating_pool_2(candidates):
    i = 0
    parents = np.array([])
    childs = np.array([])
    while(i < Number_individuals):
        random1 = random.randint(0,Number_individuals-1)
        random2 = random.randint(0,Number_individuals-1)
        if(random1 != random2):
            if(candidates[random1,0] != candidates[random2,0]):
                print("PARENTS → ", random1, " <-> ", random2)
                print(candidates[random1,:], " <-> ", candidates[random2,:])
                filesaved.write("PARENTS")
                filesaved.write(str(random1))
                filesaved.write(str(random2))
                filesaved.write(str(candidates[random1,:]))
                filesaved.write(str(candidates[random2,:]))
                parents = np.append(parents, np.array([candidates[random1,:], candidates[random2,:]]))
                # whle()
                one_child = cross_blx(candidates[random1,:], candidates[random2,:])
                childs = np.append(childs, one_child)
                # chooseparents 
                # cross_blx
                i += 1
            else:
                continue
        else:
            continue
    print("CHILDS / Nueva poblacion")
    filesaved.write("CHILDS / Nueva poblacion")
    childs = np.reshape(childs, (Number_individuals, 2))
    # print(childs)
    return [parents, childs]
    

def choose_parents(candidates):
    a,b = mating_pool_2(candidates) 
    print("PADRES CANDIDATOS")
    filesaved.write("PADRES CANDIDATOS")
    # print(a,b)
    
# choose_parents(news_candidates)

# print("CROSSING")
# cross_blx(news_candidates)


def exec():
    #condicion de termino = 100 generaciones
    newP = Initial_population
    print("POBLACION INICIAL")
    print(newP)
    # fitt = Fitness(newP)
    for i in range(10):
        print("FITNESS")
        fitt = Fitness(newP)
        print(fitt)
        print("|······\t ＩＴＥＲＡＣＩＯＮ: ", ",,",i, '\'\'', "\t······|")
        filesaved.write("ITERACION:")
        filesaved.write(str(i))
        newC = mating_pool(newP)
        a,b = mating_pool_2(newC)
        print("PADRES CANDIDATOS:", a)
        print("NUEVA POBLACION: ", b)
        filesaved.write("PADRES CANDIDATOS:")
        filesaved.write(str(a))
        filesaved.write("NUEVA POBLACION: ")
        filesaved.write(str(b))
        newP = b
    print("PRIMERA GENERACION: ",Initial_population)
    filesaved.write("PRIMERA GENERACION: ")
    filesaved.write(str(Initial_population))
    filesaved.close()

exec()

        

    


# for i in range(30):
#     a = round(random.uniform(-10,10),5)
#     print(a)





