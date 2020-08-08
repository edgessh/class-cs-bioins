# Implemente el algoritmo de Selección Negativa para clasificar la Base de Datos Iris (test)
#
# Considere dos Clases
# Considere dos Atributos
# En combinación las Clases y Atributos no deben ser los mismos de los vistos en clase.
# Muestre los valores de los datos propios, detectores y tasa de clasificación en los archivos test.
# Muestre el gráfico con los valores propios, detectores y datos test.
# Los demás parámetros los puede definir Ud

from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
import  random
import math

def decor(fun):
    print('''
     -= Parámetros =-
    Base de Datos: Iris
    Dos Clases: Iris-versicolor (Propia o normal) e Iris-virginica (No-propia o anormal)
    Dos Atributos: Largo del Pétalo (PetalLength) y Ancho del Pétalo(PetalWidth)
    r: 0.05
    Cantidad de Detectores: 1000
    Mínimo Largo del Pétalo: 1.0
    Máximo Largo del Pétalo: 6.9
    Mínimo Ancho del Pétalo: 0.1
    Máximo Ancho del Pétalo: 2.5
    '''   )

    return fun


def read_data(filename):
    minPetalLength = 0
    maxPetalLength = 0
    minPetalWidth = 0
    maxPetalWidth = 0
    f = open(filename, 'r')
    buffer = [ ]
    for line in f:
        if line.startswith('@'):
            if line.startswith('@attribute PetalLength'):
                line = line.strip('\n')
                [ minPetalLength, maxPetalLength ] = list(map(float, line[ -9:-1 ].split(',')))
            elif line.startswith('@attribute PetalWidth'):
                line = line.strip('\n')
                [ minPetalWidth, maxPetalWidth ] = list(map(float, line[ -9:-1 ].split(',')))
            else:
                continue
        else:
            if 'Iris-versicolor' in line or 'Iris-virginica' in line:
                buffer.append(line[ 10:-1 ].split(','))
    # print(buffer)
    print(len(buffer))
    print(len(buffer[ 0 ]))
    return buffer, minPetalLength, maxPetalLength, minPetalWidth, maxPetalWidth

def normalize(trained, ml, ML, mw, MW):
    ntrain = []
    for row in trained:
        #normalizando
        length = (float(row[0]) - ml)/(ML - ml)
        width = (float(row[1]) - ml)/(MW - mw)
        clase = row[2]
        ntrain.append([length, width, clase])

    return ntrain

def get_plotting(data_train, data_det=None, data_test=None):
    if data_det is None and data_test is None:
        xx = data_train[ :, 0 ].astype(np.float)
        yy = data_train[ :, 1 ].astype(np.float)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.scatter(xx, yy, color='blue')
        # plt.plot(xx, yy) #esto crea lineas
        plt.ylim(0, 1)
        plt.xlim(0, 1)
        ax.set_aspect('equal')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Negative Selection Algorithm')
        plt.show()
    elif data_det is not None and data_test is None:
        xx = data_train[ :, 0 ].astype(np.float)
        yy = data_train[ :, 1 ].astype(np.float)
        xxx = data_det[:,0]
        yyy = data_det[:,1]
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.scatter(xx, yy, color='blue')
        plt.scatter(xxx,yyy,color='red')
        # plt.plot(xx, yy) #esto crea lineas
        plt.ylim(0, 1)
        plt.xlim(0, 1)
        ax.set_aspect('equal')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Negative Selection Algorithm')
        plt.show()
    elif data_det is not None and data_test is not None:
        xx = data_train[ :, 0 ].astype(np.float)
        yy = data_train[ :, 1 ].astype(np.float)
        xxx = data_det[ :, 0 ]
        yyy = data_det[ :, 1 ]
        xxxx = data_test[:,0].astype(np.float)
        yyyy = data_test[:,1].astype(np.float)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.scatter(xx, yy, color='blue')
        plt.scatter(xxx, yyy, color='red')
        plt.scatter(xxxx[0:5], yyyy[0:5], color='green')
        plt.scatter(xxxx[5:10], yyyy[5:10], color='yellow')

        # plt.plot(xx, yy) #esto crea lineas
        plt.ylim(0, 1)
        plt.xlim(0, 1)
        ax.set_aspect('equal')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Negative Selection Algorithm')
        plt.show()
    else:
        pass


def euclidean_distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def isvalid(x,y,data, r):
    flag = True
    for data_row in data:
        # print('prueba')
        # print(data_row[0])
        # print(data_row[1])
        if euclidean_distance(x,y,data_row[0].astype(np.float),data_row[1].astype(np.float)) < r:
            flag =  False
            break
        else:
            flag = True
        # if euclidean_distance(x,y,data_row[0].astype(np.float), data_row[1].astype(np.float)) > r:
        #     flag = flag and True
        # else:
        #     flag = flag and False
    return flag

def isvalidper(x, y, data, r):
    flag = True
    for data_row in data:
        if euclidean_distance(x, y, data_row[ 0 ].astype(np.float), data_row[ 1 ].astype(np.float)) < r:
            flag = True
            break
        else:
            flag = False

    return flag

@decor
def main():
    radio = 0.05
    train, minl, maxl, minw, maxw = read_data('iris-10-1tra.dat')
    test, tminl,tmaxl,tminw,tmaxw  = read_data('iris-10-1tst.dat')
    print(' -= Valores propios =-')
    # normalized_train = (x - min(x)) / (max(x) - min(x))
    normalized_train = normalize(train, minl, maxl,minw,maxw)
    normalized_test = normalize(test, tminl,tmaxl,tminw,tmaxw)
    data_numpy = np.array(normalized_train)
    test_numpy = np.array(normalized_test)
    print(tabulate(data_numpy))
    # get_plotting(data_numpy)

    # print(data_numpy[:,0].astype(np.float))
    # inicializar los detectores
    print(' -= DETECTORES =-')
    valid_detectores = 1000
    detectors = []
    i = 0
    while i < valid_detectores:
        xD = random.uniform(0,1)
        yD = random.uniform(0,1)
        # print('datos: %f  - %f',xD, yD)
        if isvalid(xD, yD, data_numpy, radio):
            # print('hubo validacion')
            detectors.append([xD, yD])
            i += 1
    print(tabulate(detectors))
    # get_plotting(data_numpy, np.array(detectors))
    print('size of test: ', np.size(test_numpy))
    print(tabulate(test_numpy))

    print(' -= POSITIVOS =-')
    print(tabulate(test_numpy[0:5]))
    # print(np.size(test_numpy))

    print(' -= NEGATIVOS =-')
    print(tabulate(test_numpy[5:10]))

    print(' -= Resultados =-')
    positives = 0
    negatives = 0
    j = 0
    for test_row in test_numpy:
        # print(test_row)
        if isvalidper(test_row[0].astype(np.float),test_row[1].astype(np.float), test_numpy, radio):
            positives += 1
        else:
            negatives += 1

    print('Positivos: ', positives)
    print('Negativos: ', negatives)
    print('Porcentajes Positivos: ', positives*0.1)
    print('Porcentajes Negativos: ', negatives*0.1)

    get_plotting(data_numpy, np.array(detectors), test_numpy)












main()


