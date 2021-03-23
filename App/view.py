

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp



def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Palabras que siguen patron de listas")

def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en el catalogo
    """
    controller.loadData(catalog)

def print_palabras(lista):
    for i in range(1,lt.size(lista_r)+1):
        palabra=lt.getElement(lista_r,i)
        print(palabra['p_original'])

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalog= initCatalog()
        loadData(catalog)
    elif int(inputs[0]) == 2:
        lista=list(input('Inserte la lista del patrón: ').split(","))
        print("Buscando palabras ....")
        respuesta=controller.palabras_en_lista(catalog,lista)
        print_palabras(respuesta)
    else:
        sys.exit(0)
sys.exit(0)
