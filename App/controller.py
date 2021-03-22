
import config as cf
import model
import csv
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

def loadLetras(catalog):

    a = cf.data_dir + 'a.csv'

    input_file = csv.DictReader(open(a, encoding='utf-8'),delimiter='\t')
    for palabra in input_file:
        model.addPalabra(catalog, palabra,'a')


def PalabraSize(catalog):

    return model.PalabraSize(catalog)

def loadData(catalog):

    loadLetras(catalog)
