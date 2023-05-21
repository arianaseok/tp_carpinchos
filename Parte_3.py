import random
from Parte_2 import cargar_datos_para_rosco


def cargar_letras():
    """
    La funcion retorna una lista de 10 letras aleatorias 
    que estan ordenadas alfabeticamente sin repetirse entre
    ellas mismas
    """
    letras = ['a', 'b', 'c', 'd', 'e', 'f', \
            'g', 'h', 'i', 'j', 'k', 'l', 'm',\
            'n', 'ñ', 'o', 'p', 'q', 'r', 's', \
            't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_letras = random.sample(letras, k=10)
    return sorted(lista_letras, key=lambda x: x.replace("ñ", "n~"))

# Funcion que retorna dos listas ordenadas alfabeticamente
def cargar_palabras(diccionario_rosco, lista_letras):
    """
    La funcion recibe dos parametros; 1 diccionario el cual
    tiene como clave letra y valores una lista de listas de tipo
    [palabra(str), definicion(str)],  y 1 lista que contiene 10
    letras ordenadas alfabeticamente
    La funcion retorna dos listas ordenadas alfabeticamente
    """
    palabras = []
    definiciones = []
    for letra in lista_letras:
        if(letra in diccionario_rosco):
            palabra_definicion = random.choice(diccionario_rosco[letra])
            palabras.append(palabra_definicion[0])
            definiciones.append(palabra_definicion[1])
    return palabras, definiciones

"""
def probar_funcion(dicc_rosco):
    lista_letras = cargar_letras()
    for i in range(100):
        print(cargar_palabras(dicc_rosco, lista_letras))
"""

def datos_rosco():
    """
    Esta funcion es el bloque principal del programa
    """
    diccionario_rosco = cargar_datos_para_rosco()
    lista_letras = cargar_letras()
    palabras, definiciones = cargar_palabras(diccionario_rosco, lista_letras)
    return lista_letras, palabras, definiciones

    #print(lista_letras)
    #print(palabra)
    #print(definicion)