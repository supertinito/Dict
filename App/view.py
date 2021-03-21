

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf



def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- ")

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

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        answer = controller.loadData(cont)
        print('Palabras cargadas: ' + str(controller.PalabrasSize(cont))))

    else:
        sys.exit(0)
sys.exit(0)
