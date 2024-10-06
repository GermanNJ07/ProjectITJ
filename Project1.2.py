import requests
import re
from collections import Counter
import time
import string


inicio = "*** START OF THIS PROJECT GUTENBERG EBOOK" #linea que delimita donde comienza la lectura
final = "*** END OF THIS PROJECT GUTENBERG EBOOK" #linea que delimita donde termina la lectura
url_de = "https://raw.githubusercontent.com/angelgarcan/course-python/refs/heads/main/books/gutenberg/de-10223-8_UTF8.txt"
url_en = "https://raw.githubusercontent.com/angelgarcan/course-python/refs/heads/main/books/gutenberg/en-10002-8_UTF8.txt"
url_es = "https://raw.githubusercontent.com/angelgarcan/course-python/refs/heads/main/books/gutenberg/es-11529-8_UTF8.txt"
url_fr = "https://raw.githubusercontent.com/angelgarcan/course-python/refs/heads/main/books/gutenberg/fr-10682-8_UTF8.txt"

def get_file(url): 
    #Funcion para obtener el archivo desde la URL
    response = requests.get(url, verify=False)
    doc = open("file2.txt",'wb').write(response._content) #El archivo se guarda como file2.txt

def set_file_boundaries(inicio,final):
    #Funcion para obtener en que lugar del archivo se encuentran las lineas que delimitan las fronteras del fragmento que se quiere leer
    archivo = open("file2.txt",'r') #se abre el archivo en modo lectura
    abc = archivo.read()
    indice_inicio = abc.index(inicio) #se busca el indice donde esta el inicio del fragmento
    indice_final = abc.index(final) #se busca el indice donde esta el final del fragmento
    archivo.seek(indice_inicio)
    abc = archivo.read(indice_final-indice_inicio)
    with open(r'file3.txt', 'w') as outfile:
        outfile.write(abc) #se crea un nuevo archivo llamado file3.txt que solo contiene el texto delimitado por los boundaries deseados en Inicio y Final
    archivo = open("file3.txt",'r')
    return archivo, indice_inicio,indice_final


def remove_newline(archivo,character): 
    #funcion para eliminar el salto de linea
    file = archivo.read()
    file = file.replace(character,"")
    #print(file)
    with open(r'file3.txt', 'w') as outfile:
        outfile.write(file) #se sobreescribe el archivo file3.txt con el nuevo texto que ya no tiene saltos de linea


def remove_punctuation_marks():
    #funcion para eliminar los signos de puntuacion
    file = open("file3.txt",'r')
    archivo = file.read()
    translator = str.maketrans('', '', string.punctuation)
    no_punct = archivo.translate(translator)
    with open(r'file3.txt', 'w') as outfile:
        outfile.write(no_punct)#se sobreescribe el archivo file3.txt con el nuevo texto que ya no tiene signos de puntuacion


def convert_lowercase():
    #funcion para mandar todo a minusculas
    file = open("file3.txt",'r')
    archivo = file.read()
    archivo = archivo.lower()
    with open(r'file3.txt', 'w') as outfile:
        outfile.write(archivo) #se sobreescribe el archivo file3.txt con el nuevo texto en minusculas


def count_occurrences():
    #funcion para contar y ordenar las ocurrencias de cada caracter dentro del archivo
    file = open("file3.txt",'r') #se abre el archivo en modo lectura
    cuenta = Counter(file.read()) #se usa Counter
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
remove_newline(file,'\n')
remove_punctuation_marks()
convert_lowercase()
contador = count_occurrences()
print(contador)
top_ten(contador)
end_time = get_time()
print(f"Tiempo de ejecucion en aleman: {end_time-start_time} segundos\n")

##### Para lenguaje ingles#####
start_time = get_time()
get_file(url_en)
file,indice_inicio,indice_final = set_file_boundaries(inicio,final)
remove_newline(file,'\n')
remove_punctuation_marks()
convert_lowercase()
contador = count_occurrences()
print(contador)
top_ten(contador)
end_time = get_time()
print(f"Tiempo de ejecucion en ingles: {end_time-start_time} segundos\n")

##### Para lenguaje espaniol#####
start_time = get_time()
get_file(url_es)
file,indice_inicio,indice_final = set_file_boundaries(inicio,final)
remove_newline(file,'\n')
remove_punctuation_marks()
convert_lowercase()
contador = count_occurrences()
print(contador)
top_ten(contador)
end_time = get_time()
print(f"Tiempo de ejecucion en espaniol: {end_time-start_time} segundos\n")

##### Para lenguaje frances#####
start_time = get_time()
get_file(url_fr)
file,indice_inicio,indice_final = set_file_boundaries(inicio,final)
remove_newline(file,'\n')
remove_punctuation_marks()
convert_lowercase()
contador = count_occurrences()
print(contador)
top_ten(contador)
end_time = get_time()
print(f"Tiempo de ejecucion en frances: {end_time-start_time} segundos\n")









