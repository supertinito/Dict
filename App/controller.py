
import config as cf
import model
import csv
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

def loadLetras(catalog):

    palabras = cf.data_dir + 'palabras.csv'
    
    input_file = csv.DictReader(open(palabras, encoding='utf-8'),delimiter=',')
    for palabra in input_file:
        palabra_real=palabra['palabra'].lower()
        primera_letra=palabra_real[0].lower().strip()
        model.addPalabra(catalog['Palabras'], palabra_real,primera_letra)


def PalabraSize(catalog):

    return model.PalabraSize(catalog)

def loadData(catalog):
    loadLetras(catalog)

def palabras_en_lista(catalog,lista):
    return model.palabras_en_lista(catalog,lista)
    
