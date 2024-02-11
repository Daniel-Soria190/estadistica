### Archivo de funciones de python para estadistica aplicada.

# Importando librerias
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# import scipy as scp
import seaborn as sns

# Funcion para cargar datos

# Funcion de ordenamiento por casillas

# Funcion de promedio
def promedio(lista):
    """
    Calcula el promedio de una lista o arreglo de numpy

    Parametros
    ----------
    lista: Recibe una lista de datos [x1, x2,...,xn].
    
    Returns
    -------
    `float`, `numpy.ndarray`

    Notas
    -----
    
    """
    if isinstance(lista, (list)):
        n = len(lista)
        sum = 0
        for x in lista:
            sum += x
        aux = sum/n
    elif isinstance(lista, tuple):
        a,b = lista
        aux = (a+b)/len(a)
    else:
        aux = lista.sum()/lista.size
    return(aux)


# Fucnion de ordenamiento burbuja

def burbuja(lista):
    """
    Función de ordenamiento basado en el algoritmo bubble sort.

    
    
    """
    if isinstance(lista, (list,tuple)):
        n=len(lista)
    else:
        n = lista.size

    ordenado = lista.copy()
    for i in range(n-1):
        for j in range(0,n-i-1):
            if ordenado[j] > ordenado[j+1]:
                ordenado[j], ordenado[j+1] = ordenado[j+1], ordenado[j]

    return(ordenado)

# Funcion de mediana

def mediana(lista):
    """Calcula la mediana de una lista de datos
    
    """
    aux = burbuja(lista)
    if isinstance(aux, (list,tuple)):
        n=len(aux)
    else:
        n = aux.size
    
    if n%2 == 0:
        i, j = int(n/2), int(n/2)+1
        mediana = (aux[i]+aux[j])/2
    else:
        i = int(n/2)+1
        mediana = aux[i]

    return(mediana)

# Función de moda

# Funcion de tablas de frecuencia
def tabla(arreglo,nClases=None):
    """
    Funcion que genera la tabla de frecuencias dado un arreglo de datos.

    Parametros
    ----------
    arreglo: Recibe una lista de datos [x1, x2,...,xn].

    nClases: Ajusta manualmente la cantidad de clases en que se divide el
    arreglo
    
    Returns
    -------
    `pandas.DataFrame()`

    Notas
    -----

    Se espera la definicion de una clase Tabla que embeba la misma funcion
    y distintas propiedades de la tabla.

    
    """
    
    aux = burbuja(arreglo.copy())
    n=len(aux)
    a, b = int(aux[0]), int(aux[n-1]+1)
    rango = b-a
    if isinstance(nClases,(int,float)):
        clases = int(nClases)
        inter = rango/clases
    else:               # Modo automatico
        clases = int(np.sqrt(n))
        inter = rango/clases

    marcas = np.arange(a,b+1,inter)
    frec = np.zeros(clases)
    
    for x in aux:
        for j in range(0,clases):
            if marcas[j] <= x < marcas[j+1]:
                frec[j] += 1

    acumulada = []
    sum = 0
    for x in frec:
        sum += x
        acumulada.append(sum)

    linf = np.array(marcas[0:clases])
    lsup = np.array(marcas[1:])

    marcaClase = (linf + lsup)/2    
    
    dic = {'Linf':marcas[0:clases], 'Lsup':marcas[1:], 'MarcaDeClase':marcaClase, 'FrecuenciaAbsoluta':frec}
    tabla = pd.DataFrame(dic)

    tabla['FrecuenciaAcumulada'] = acumulada
    tabla['FrecuenciaRelativa'] = tabla['FrecuenciaAbsoluta']/n
    tabla['FRA'] = tabla['FrecuenciaAcumulada']/n

    return(tabla)

def stem():
    pass