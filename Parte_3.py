import random
from Parte_2 import cargar_datos_para_rosco

#Funcion que retorna 10 letras aleatorias que 
# estan ordenadas alfabeticamente 
def cargar_letras():
    """
    Funcion que retorna 10 letras aleatorias que
    """
    letras = ['a', 'b', 'c', 'd', 'e', 'f', \
            'g', 'h', 'i', 'j', 'k', 'l', 'm',\
            'n', 'ñ', 'o', 'p', 'q', 'r', 's', \
            't', 'u', 'v', 'w', 'x', 'y', 'z']
    lista_letras = random.sample(letras, k=10)
    return sorted(lista_letras, key=lambda x: x.replace("ñ", "n~"))

# Funcion que retorna dos listas ordenadas alfabeticamente
def cargar_palabras(dicc_rosco, lista_letras):
    """
    Esta funcion retorna dos listas ordenadas alfabeticamente
    """
    palabras = []
    definiciones = []

    for letra in lista_letras:
        if(letra in dicc_rosco):
            palabra_definicion = random.choice(dicc_rosco[letra])
            palabras.append(palabra_definicion[0])
            definiciones.append(palabra_definicion[1])

    return palabras, definiciones

"""
def probar_funcion(dicc_rosco):
    lista_letras = cargar_letras()
    for i in range(100):
        print(cargar_palabras(dicc_rosco, lista_letras))
"""

#Bloque Principal
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

#datos_rosco(cargar_datos_para_rosco, cargar_letras, cargar_palabras)