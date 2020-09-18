### importando librerias
import os
import pyfiglet
import random
import numpy as np
import palabras

### personitas a mostrar en el menú
ahorcado = ['''
      +---+
          |
          |
          |
          |
          |
    =========''','''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''','''
      +---+
          |
          |
    \ O / |
      |   |
     / \  |
    =========''']

def establecerPalabraAleatoria(listaPalabras):
  ### Escogiendo una palabra aleatoria de una lista
  palabraAleatoria = random.randint(0, len(listaPalabras) -1)
  return (listaPalabras[palabraAleatoria]).upper()

def elegirLetra(letrasSeleccionadas):
  ### Escogiendo y validando la letra
  letra = (input("Introduce una letra:\n")).upper()
  while True:
    if(len(letra)) != 1:
      print('Debes introducir una sola letra')
      return elegirLetra(letrasSeleccionadas)
    elif(letra not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
      print('Debes introducir una letra válida')
      return elegirLetra(letrasSeleccionadas)
    elif(letra in letrasSeleccionadas):
      print('Introduce una letra que aún no hayas usado')
      return elegirLetra(letrasSeleccionadas)
    else:
      letrasSeleccionadas.append(letra);
      return letra

def imprimirPantalla(palabraOfuscada,intentos, textoRandom, palabra):
  ### Imprimir los mensajes
  os.system('cls')
  print(ahorcado[intentos])
  print(palabraOfuscada)
  # descomentar esta linea para mostrar la palabra en cuestion
  # print(palabra)
  print(textoRandom + ", te quedan " + str(7 - intentos) + " intentos")

def victoria(palabra):
  # mensaje en caso de victoria
  os.system('cls')
  print("HAS GANADO!!!")
  print(ahorcado[8])
  print("la palabra era "+ palabra)
  input("Presiona Enter para volver al menú principal")
  return main()

def derrota(palabra):
  # mensaje en caso de derrota
  os.system('cls')
  print("DERROTA :(")
  print(ahorcado[7])
  print("la palabra era "+ palabra)
  input("Presiona Enter para volver al menú principal")
  return main()

def jugar(palabras):
  # Iniciando el juego
  letrasSeleccionadas = []
  print("jugando")
  palabraSecreta = establecerPalabraAleatoria(palabras.lista)
  palabraOfuscada = np.full(len(palabraSecreta),"_")
  intentos = 0
  mensaje = 'Jugemos'
  while intentos < 7:
    imprimirPantalla(''.join(palabraOfuscada), intentos, mensaje, palabraSecreta)
    letra = elegirLetra(letrasSeleccionadas)
    if letra not in palabraSecreta:
      intentos += 1
      mensaje = 'Intenta otra ves'
    else:
      for _ in range(len(palabraSecreta)):
        if palabraSecreta[_] == letra:
          palabraOfuscada[_] = letra
      if ''.join(palabraOfuscada) == palabraSecreta:
        return victoria(palabraSecreta)
      mensaje = 'Bien, esa letra te ayudará'
  return derrota(palabraSecreta)

def main():
  # método principal
  os.system('cls')
  print(pyfiglet.figlet_format("Ahorcado!!"))
  opcion1 = "1. Jugar\n"
  opcion2 = "2. Salir\n"

  option = int(input("selecciona una opción: \n"+ opcion1 + opcion2 + "***selecciona un número*** :"))
  if(option == 1):
      return jugar(palabras)
  if(option == 2):
    os.system('cls')
    return
  else:
    (input("presiona una opción válida (Enter)"))
    return main()
main()
