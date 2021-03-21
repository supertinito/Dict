


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'Palabras':None}

    """
    Este indice crea un map cuya llave es la etiqueta
    """
    catalog['Palabras'] = mp.newMap(100,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareletra

    return catalog


# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta
def PalabraSize(catalog):
    """
    Numero de tags en el catalogo
    """
    return mp.size(catalog['Palabras'])
# Funciones utilizadas para comparar elementos dentro de una lista
def compareletra(name, letra):
    letraentry = me.getKey(letra)
    if (name == letraentry):
        return 0
    elif (name > letraentry):
        return 1
    else:
        return -1
# Funciones de ordenamiento
