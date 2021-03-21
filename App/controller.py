
import config as cf
import model
import csv

def loadCategorias(catalog):

    a = cf.data_dir + 'a.txt'

    input_file = csv.DictReader(open(categoriafile, encoding='utf-8'),delimiter='\t')
    for categoria in input_file:
        model.addListaCategorias(catalog, categoria)

def loadVideos(catalog):
    videosfile = cf.data_dir + 'videos-small.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def PalabraSize(catalog):

    return model.PalabraSize(catalog)

def loadData(catalog):

    loadBooks(catalog)
    loadTags(catalog)
    loadBooksTags(catalog)