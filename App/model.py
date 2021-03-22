


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
                                comparefunction=compareletra)

    return catalog


# Construccion de modelos
def addPalabra(catalog,palabra,letra):
    palabras=catalog['Palabras']
    print(palabra)
    palabra_separada=palabra.split(',')
    palabra_usar=palabra_separada[0]
    new_palabra=new_palabra(palabra_usar)
    existeletra= mp.contains(palabras, letra)
    if existeletra:
        entrada=mp.get(palabras, letra)
        letra_list=me.getValue(entrada)
        lt.addLast(letra, palabra)
    else:
        letra_list=new_letra(letra)
        mp.put(palabras, letra, letra_list)
        lt.addLast(letra, palabra)
# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos
def new_palabra(palabra):
    palabra={'p_original':None,'p_mod':None,'len':0}
    palabra['p_original'] = palabra
    palabra['p_mod'] = palabra
    palabra['len'] = len(palabra)
    return palabra 

def new_letra(letra):
# Funciones de consulta
    letra=lt.newList(datastructure='ARRAY_LIST')
    return letra

def PalabraSize(catalog):

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
