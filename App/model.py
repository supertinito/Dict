


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
def addPalabra(palabras,palabra,letra):
    palabra_usar=new_palabra(palabra)
    existeletra= mp.contains(palabras, letra)
    if existeletra:
        entrada=mp.get(palabras, letra)
        letra_list=me.getValue(entrada)
        lt.addLast(letra_list, palabra_usar)
    else:
        letra_list=new_letra(letra)
        lt.addLast(letra_list, palabra_usar)
        mp.put(palabras, letra, letra_list)
        
# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos
def new_palabra(palabra):
    nueva_palabra={'p_original':None,'p_mod':None,'len':0}
    nueva_palabra['p_original'] = palabra
    nueva_palabra['p_mod'] = palabra
    nueva_palabra['len'] = len(palabra)
    return nueva_palabra 

def new_letra(letra):
# Funciones de consulta
    letra=lt.newList(datastructure='ARRAY_LIST')
    return letra

def PalabraSize(catalog):

    return mp.size(catalog['Palabras'])

def letras_en_lista(catalog,lista):
    nuevo_mapa=mp.newMap(100,maptype='PROBING',loadfactor=0.5,comparefunction=compareletra)
    for letra in lista:
        pareja=mp.get(catalog['Palabras'],letra)
        llave=me.getKey(pareja)
        valor=me.getValue(pareja)
        for i in range(1,lt.size(valor)):
            elemento=lt.getElement(valor,i)
            if elemento['len']==len(lista):
                elemento['p_mod']=elemento['p_mod'][1:]
                if len(elemento['p_mod'])>0:
                    primera_letra=elemento['p_mod'][0]
                    addPalabra(nuevo_mapa,elemento,primera_letra)
                else:

    return nuevo_mapa

def palabras_en_lista(catalog,lista):
    map=catalog['Palabras']
    for i in range(0,len(lista)):
        letras=lista[i]
        map=letras_en_lista(map,letras)
    return mp.valueSet(map) 


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
