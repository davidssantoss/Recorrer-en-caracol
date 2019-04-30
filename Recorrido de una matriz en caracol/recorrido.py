from io import StringIO
import numpy as np

"""
@author: David s
"""

def leerMatriz():
    return np.genfromtxt(StringIO((open('matriz.txt', 'r')).read()), delimiter = ' ')
def rotarMatriz(matriz):
    return np.rot90(matriz, k = 1, axes = (0,1))
def avanzar(matriz):
    if matriz.shape[0] == 1:
        return matriz[0, 0:1]
    else:
         return matriz[(matriz.shape[0]-1), 1: matriz.shape[1]]

def recortar(matriz):
    return matriz[1:matriz.shape[0]-1, 1: matriz.shape[1]-1]

def recorrer(matriz, l):
    if matriz.shape[0] == 1:
        print(avanzar(matriz))
        return "Terminado"
    if matriz.shape[0] > 0:
        if l > 0:
            print(np.fliplr([avanzar(matriz)])[0])
            recorrer(rotarMatriz(matriz), l - 1)
            print("algo que recorre por aqui")
        else:
            recorrer(recortar(matriz), 4)
print("Ruta de la Matriz: ")
print(leerMatriz())
print("Recorriendo en caracol: ")
print(recorrer(leerMatriz(), 4))
