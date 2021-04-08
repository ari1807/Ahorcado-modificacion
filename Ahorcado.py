import random
import string

HANGMAN_PICS = ["""
  +---+          
      |
      |
      |
     ===""", """
  +---+
  O   |
      |
      |
     ===""", """
  +---+
  O   |
  |   |
      |
     ===""", """
  +---+
  O   |
 /|   |
      |
     ===""", """
  +---+
  O   |
 /|\  |
      |
     ===""", """
  +---+
  O   |
 /|\  |
 /    |
     ===""", """
  +---+
  O   |
 /|\  |
 / \  |
     ===""", """
  +---+
 [O   |
 /|\  |
 / \  |
     ===""", """
  +---+
 [O]  |
 /|\  |
 / \  |
     ==="""]
 

PALABRAS = {'Colores': 'rojo naranja amarillo verde azul indigo violeta blanco negro marron'.split(),
'Figuras geometricas': 'cuadrado triangulo rectangulo circulo elipse rombo trapezoide pentagono hexagono heptagono octagono'.split(),
'Frutas': 'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango frutilla tomate'.split(),
'Animales': 'murcielago oso castor gato perro cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela leon lagartija mono alce raton rata nutria buho panda serpiente conejo tiburon oveja zorrillo calamar tigre pavo tortuga weasel ballena zorro zebra'.split()}


def get_palabra_random(dict_palabras):
    """ Esta funcion devuelve un string aleatorio desde el diccionario de strings pasado como parametro, como tambien su clave."""
    
    # Primero, seleccionamos una clave aleatoria del diccionario:
    clave = random.choice(list(dict_palabras.keys()))

    # Despues, seleccionamos una palabra aleatoria de la lista contenida en la clave del diccionario:
    indice = random.randint(0, len(dict_palabras[clave])-1)

    return [dict_palabras[clave][indice], clave]

def mostrar_tabla(letras_incorrectas, letras_correctas, palabra_secreta):
    """ Esta funcion muestra en pantalla el dibujo, las letras incorrectas y los espacios con letras adivinadas de la palabra secreta."""

    print(dibujos[len(letras_incorrectas)])
    print()

    print('Intentos fallidos:', end=' ')
    for letra in letras_incorrectas:
        print(letra, end=' ')
    print()

    blanks = '_' * len(palabra_secreta)

    # Reemplaza los espacios en blanco con las letras adivinadas
    for i in range(len(palabra_secreta)):   
        if palabra_secreta[i] in letras_correctas:
            blanks = blanks[:i] + palabra_secreta[i] + blanks[i+1:]

    # Muestra la palabra secreta con espacios entre cada letra
    for letra in blanks:  
        print(letra, end=' ')
    print()

def get_intento(letras_intentadas):
    """ Esta funcion devuelve la letra que el jugador ingreso. Se asegura de que solo se haya ingresado una letra, y no algo mas. """
    
    while True:
        print('Ingresa una letra.')
        intento = input().lower()
        if len(intento) != 1:
            print('Por favor, ingrese solo una letra.')
        elif intento in letras_intentadas:
            print('Ya has ingresado esa letra. Elige otra vez.')
        elif intento not in string.ascii_lowercase:
            print('Por favor, ingresa una LETRA.')
        else:
            return intento

def jugar_otra_vez():
    """ Esta funcion devuelve True si el jugador quiere jugar otra vez, sino devuelve False. """
    
    print('Queres jugar otra vez? (si o no)')
    return input().lower().startswith('s')

def dar_pista (palabra_secreta, letras_correctas, pistas):
    """ Devuelve una letra de la palabra secreta que NO este en las letras adivinadas si el jugador pide la pista, sino devuelve ''. """
    
    letra_pista = ''
    print(f'Tenes {pistas} pistas.')
    if input('Queres una pista? (si/no): ').lower().startswith('s'):
        letra_pista = palabra_secreta[random.randint(0, len(palabra_secreta)-1)]
        while letra_pista in letras_correctas:
            letra_pista = palabra_secreta[random.randint(0, len(palabra_secreta)-1)]
    return letra_pista


print('A H O R C A D O')


while True: 
    dificultad = 'X'
    pistas = 3
    dibujos = HANGMAN_PICS[:]
    while dificultad not in 'FMD':
        print('Ingrese la dificultad: F - Facil, M - Medio, D - Dificil')
        dificultad = input().upper()
    if dificultad == 'M':
        del dibujos[7]
        del dibujos[5]
        pistas = pistas - 1
    if dificultad == 'D':
        del dibujos[7]
        del dibujos[5]
        del dibujos[3]
        del dibujos[1]
        pistas = pistas - 2

    letras_incorrectas = ''
    letras_correctas = ''
    palabra_secreta, conjunto_secreto = get_palabra_random(PALABRAS)
    juego_terminado = False

    while True:
        print('La palabra secreta esta en el grupo: ' + conjunto_secreto)
        mostrar_tabla(letras_incorrectas, letras_correctas, palabra_secreta)

        # Deja al jugador escribir una letra o elegir una pista.
        if pistas != 0:
            intento = dar_pista(palabra_secreta, letras_correctas, pistas)
            if (intento == ''):
                intento = get_intento(letras_incorrectas + letras_correctas)
            else:
                pistas = pistas - 1   
        else:
            intento = get_intento(letras_incorrectas + letras_correctas)
            
        if intento in palabra_secreta:
            letras_correctas = letras_correctas + intento
            # Chequear si el jugador gano
            encontro_todas_las_letras = True
            for i in palabra_secreta:
                if i not in letras_correctas:
                    encontro_todas_las_letras = False
                    break
            if encontro_todas_las_letras:
                print(f'Ganaste! La palabra secreta es {palabra_secreta}')
                juego_terminado = True
        else:
            letras_incorrectas = letras_incorrectas + intento
            
            # Chequear si el jugador intento demasiadas veces y perdio.
            if (len(letras_incorrectas) == len(dibujos)-1):
                mostrar_tabla(letras_incorrectas, letras_correctas, palabra_secreta)
                print(f'Te quedaste sin intentos!\nDespues de {len(letras_incorrectas)}  intentos fallidos y {len(letras_correctas)} letras adivinadas, la palabra era: {palabra_secreta}')
                juego_terminado = True
            

        # Termina la partida.
        if juego_terminado:
            break

    # Pregunta al jugador si quiere jugar de nuevo o salir del juego.    
    if jugar_otra_vez():
        continue
    else:
        break