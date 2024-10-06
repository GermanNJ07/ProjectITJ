import requests
import re
from collections import Counter
import time


inicio = "*** START OF THIS PROJECT GUTENBERG EBOOK" #linea que delimita donde comienza la lectura
final = "*** END OF THIS PROJECT GUTENBERG EBOOK" #linea que delimita donde termina la lectura
url_de = "https://raw.githubusercontent.com/angelgarcan/course-python/refs/heads/main/books/gutenberg/de-10223-8_UTF8.txt"
url_en = "https://raw.githubusercontent.com/angelgarcan/course-python/refs/heads/main/books/gutenberg/en-10002-8_UTF8.txt"
url_es = "https://raw.githubusercontent.com/angelgarcan/course-python/refs/heads/main/books/gutenberg/es-11529-8_UTF8.txt"
url_fr = "https://raw.githubusercontent.com/angelgarcan/course-python/refs/heads/main/books/gutenberg/fr-10682-8_UTF8.txt"

def get_file(url): 
    #Funcion para obtener el archivo desde la URL
    response = requests.get(url, verify=False)
    open("file.txt",'wb').write(response._content) #El archivo se guarda como file.txt

def set_file_boundaries(inicio,final):
    #Funcion para obtener en que lugar del archivo se encuentran las lineas que delimitan las fronteras del fragmento que se quiere leer
    archivo = open("file.txt",'r') #se abre el archivo en modo lectura
    abc = archivo.read()
    indice_inicio = abc.index(inicio) #se busca el indice donde esta el inicio del fragmento
    indice_final = abc.index(final) #se busca el indice donde esta el final del fragmento
    return archivo, indice_inicio,indice_final


def count_occurrences(archivo,indice_inicio,indice_final):
    #funcion para contar y ordenar las ocurrencias de cada caracter dentro del archivo
    archivo.seek(indice_inicio) 
    cuenta = Counter(archivo.read(indice_final-indice_inicio)) #se usa Counter
    cuenta.most_common() #se usa el metodo most_common para ordenar de mayor a menor numero de ocurrencias
    return cuenta


def top_ten(contador):
    #funcion para obtener el top ten de caracteres mas frecuentes 
    cuenta = contador.most_common()
    print("\nTop ten characters")
    for i in range (10):
        print (cuenta[i])


def get_time():
    #funcion para obtener el tiempo
    timer = time.time()
    return timer


##### Para lenguaje aleman#####
start_time = get_time() 
get_file(url_de) 
file,indice_inicio,indice_final = set_file_boundaries(inicio,final)
contador = count_occurrences(file,indice_inicio,indice_final)
print(contador)
top_ten(contador)
end_time = get_time()
print(f"Tiempo de ejecucion en aleman: {end_time-start_time} segundos\n")

##### Para lenguaje ingles#####
start_time = get_time()
get_file(url_en)
file,indice_inicio,indice_final = set_file_boundaries(inicio,final)
contador = count_occurrences(file,indice_inicio,indice_final)
print(contador)
top_ten(contador)
end_time = get_time()
print(f"Tiempo de ejecucion en ingles: {end_time-start_time} segundos\n")

##### Para lenguaje espaniol#####
start_time = get_time()
get_file(url_es)
file,indice_inicio,indice_final = set_file_boundaries(inicio,final)
contador = count_occurrences(file,indice_inicio,indice_final)
print(contador)
top_ten(contador)
end_time = get_time()
print(f"Tiempo de ejecucion en espaniol: {end_time-start_time} segundos\n")

##### Para lenguaje frances#####
start_time = get_time()
get_file(url_fr)
file,indice_inicio,indice_final = set_file_boundaries(inicio,final)
contador = count_occurrences(file,indice_inicio,indice_final)
print(contador)
top_ten(contador)
end_time = get_time()
print(f"Tiempo de ejecucion en frances: {end_time-start_time} segundos\n")




