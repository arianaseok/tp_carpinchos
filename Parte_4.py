import Parte_3
from Parte_2 import palabra_sin_acento

ACIERTO = "a"
ERROR = "e"

def generar_diccionario():
    """
    La funcion importa las funciones de Parte_2 y Parte_3
    y devuelve un diccionario con clave palabra y valor definicion,
    y tambien devuelve una lista_letras
    """
    lista_letras, palabras, definiciones = Parte_3.datos_rosco()
    datos_rosco = {}
    for i in range(len(lista_letras)):
        datos_rosco[palabras[i]] = definiciones[i]
    return datos_rosco, lista_letras

def mostrar_tablero(lista_letras, resultados, aciertos, errores, posicion, letra, long_palabra, definicion):
    """
    Esta funcion recibe 4 parametros (2 listas y 2 variables (int)) y
    Muestra por pantalla el estado del juego.
    """
    print(f"""
    {''.join(f'[{letra}]' for letra in lista_letras)}
    {''.join(f'[{resultado}]' for resultado in resultados)}
    {' ' * (posicion * 3 + 1)}^
    Aciertos: {aciertos}
    Errores: {errores}
    Turno letra: {letra} Longitud palabra: {long_palabra} \nDefinicion: {definicion}
    """)

def cargar_palabra():
    """
    Esta funcion se encargar de cargar valores para 
    la variable palabra.
    """
    palabra = input("Ingrese la palabra: ").lower()
    return palabra_sin_acento(palabra)

def palabra_valida():
    """
    La funcion recibe como parametro una variable, y retorna
    la variable de tipo string 
    """
    palabra = cargar_palabra()
    while not palabra.isalpha():
        print("Ingrese solo LETRAS!")
        palabra = palabra_sin_acento(cargar_palabra())
    return palabra

def analizar_palabra_ingresada(palabra_ingresada, clave_palabra):
    """
    La funcion analiza el dato que haya en "palabra_ingresada",
    y en caso de que sea igual a "clave_palabra" retorna una "a"
    de ACIERTO y en caso contrario retorna una "e" de ERROR
    >>> analizar_palabra("pato", "pato")
    'a'
    >>> analizar_palabra("hecho", "hacha")
    'e'
    >>> analizar_palabra("caballo", "corbata")
    'e'
    """
    return ACIERTO if (palabra_ingresada == clave_palabra) else ERROR

def contar_puntos(resultado, aciertos, errores):
    """
    La funcion recibe un parametro que es una
    variable de tipo str
    La funcion devuelve 3 variables inicializadas
    de tipo int
    """
    if (resultado == ACIERTO):
        aciertos += 1
        puntos = 10
    else:
        errores += 1
        puntos = -3
    return aciertos, errores, puntos

def jugar_turno(aciertos, errores, posicion,
                lista_letras, resultados, palabra, definicion):
    """
    La funcion recibe 7 parametros los cuales deben ser;
    3 variables de tipo int, 2 listas que sus componentes 
    sean de tipo str y dos variables que sean de tipo str
    totas inicializadas.
    La funcion devuelve 4 variables las cuales son 3 de tipo
    int y una str
    """
    letra = palabra[0]
    long_palabra = len(palabra)
    mostrar_tablero(lista_letras, resultados, aciertos, errores,
                    posicion, letra, long_palabra, definicion)
    palabra_ingresada = palabra_valida()
    resultado = analizar_palabra_ingresada(palabra_ingresada, palabra)
    resultados[posicion] = resultado
    aciertos, errores, puntos = contar_puntos(resultado, aciertos, errores)

    return aciertos, errores, puntos, palabra_ingresada


def mostrar_resultado (resultado, letra, long_palabra, palabra_jugador, palabra_correcta):
    """
    La funcion recibe 5 parametros; dos listas y 3 variables.
    La funcion muestra por pantalla; si los datos ingresados son
    correctos muestra un respetivo mensaje sino muestra otro mensaje.
    """
    if (resultado == ERROR):
        print(f"Turno de la letra: {letra} - Palabra de {long_palabra} letras - {palabra_jugador} - La palabra correcta es: {palabra_correcta}")
    else:
        print(f"Turno de la letra: {letra} - Palabra de {long_palabra} letras - {palabra_jugador}")
    

def mostrar_resumen_de_juego(diccionario_rosco, 
                                palabras_ingresadas, resultado):
    """
    La funcion recibe tres parametros; un diccionario y dos lista
    ya inicializadas.
    La funcion muestra por pantalla el resumen de la partida
    """
    print("\n-------- Resumen de la partida -----------")
    print("-" * 90)
    for posicion, palabra in enumerate(diccionario_rosco.keys()):
        letra = palabra[0]
        long_palabra = len(palabra)
        palabra_correcta = palabra
        palabra_jugador = palabras_ingresadas[posicion]
        resultado = analizar_palabra_ingresada(palabra_jugador, palabra_correcta)
        mostrar_resultado(resultado, letra, long_palabra, palabra_jugador, palabra_correcta)
    print("-" * 90)


def juego_inicializado(diccionario_rosco, lista_letras, resultados):
    aciertos = 0
    errores = 0
    puntos_totales = 0
    palabras_ingresadas = []

    for indice, palabra in enumerate(diccionario_rosco.keys()):
        print(palabra)
        letra = palabra[0]
        long_palabra = len(palabra)
        posicion = indice
        definicion = diccionario_rosco[palabra]
        aciertos, errores, puntos, palabra_ingresada = jugar_turno(
            aciertos, errores, posicion, lista_letras, resultados, palabra, definicion)
        puntos_totales += puntos
        palabras_ingresadas.append(palabra_ingresada)
    
    mostrar_tablero(lista_letras, resultados, aciertos, errores, posicion, letra, long_palabra, definicion)
    mostrar_resumen_de_juego(diccionario_rosco, palabras_ingresadas, resultados)
    return puntos_totales

def cargar_respuesta():
    """
    La funcion carga valores a la variable "respuesta"
    y la retorna
    """
    respuesta = input("¿Camarada deseas seguir jugando? (si/no): ").lower()
    return palabra_sin_acento(respuesta)

def respuesta_valida():
    """
    La funcion llama a la funcion cargar_respuesta y guarda su valor en
    "respuesta" con la cual trabajara para verificar que lo hay dentro de
    esa variable sea un "si" o un "no".
    La funcion retorna la variable con una cadena de caracteres que
    puede ser "si" o "no"
    """
    respuesta = cargar_respuesta()
    while (respuesta != "si") and (respuesta != "no"):
        print("Por favor, ingrese 'si' o 'no'")
        respuesta = palabra_sin_acento(cargar_respuesta())
    return respuesta


def jugar_rosco():
    resultado = [" " for i in range(10)]
    continuar_jugando = True
    puntaje_total = 0

    while continuar_jugando:
        diccionario_rosco, lista_letras = generar_diccionario()
        puntaje_partida = juego_inicializado(diccionario_rosco, lista_letras, resultado)
        puntaje_total += puntaje_partida
        print(f"\nEl puntaje de la partida es: {puntaje_partida}")
        respuesta = respuesta_valida()
        if (respuesta == "no"):
            continuar_jugando = False
        else:
            resultado = [" " for i in range(10)]
    
    print(f"\nPuntaje total: {puntaje_total}")

jugar_rosco()