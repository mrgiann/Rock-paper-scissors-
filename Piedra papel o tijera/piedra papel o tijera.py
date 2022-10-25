import os
clear = lambda: os.system("cls")
clear()
import random
archivo = open("score.txt","a")
numpartidas= int(input("Cuantas partidas quieres jugar?\033[36m "))
nombre = input("\033[37mnombre:\033[36m ").lower().capitalize()

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
pjugador = 0
pbot= 0
empate= 0

def partida():
    global pjugador
    global pbot
    global empate
    opciones = ["piedra","papel","tijera"]
    bot = random.choice(opciones)
    jugador=input("\033[37mElije: piedra - papel - tijera :\033[36m  ").lower()
    print("\033[37mBot elijio:\033[31m ",bot,"\033[37m")
    print("-"*50,"\033[33m")

    if jugador=="piedra" and bot=="piedra":
        print("Empate, punto nulo")
        empate+=1
    elif jugador=="piedra" and bot=="papel":
       print("Gana papel, punto para bot")
       pbot+=1
    elif jugador=="piedra" and bot=="tijera":
        print("Gana piedra, punto para jugador")
        pjugador+=1
       
    elif jugador=="papel" and bot=="papel":
        print("Empate, punto nulo")
        empate+=1
    elif jugador=="papel" and bot=="tijera":
        print("Gana tijera, punto para bot")
        pbot+=1
    elif jugador=="papel" and bot=="piedra":
        print("Gana papel, punto para jugador")
        pjugador+=1

    elif jugador=="tijera" and bot=="tijera":
        print("Empate, punto nulo")
        empate+=1
    elif jugador=="tijera" and bot=="piedra":
        print("Gana piedra, punto para bot")
        pbot+=1
    elif jugador=="tijera" and bot=="papel":
        print("Gana tijera, punto para jugador")
        pjugador+=1
    print("\033[37m-"*50)
    print("")

i=0
while i<numpartidas:
    print("")
    partida()
    i+=1
    
archivo.write('Nombre: ' + nombre + '\n')
archivo.write('Puntaje del jugador: ' + "%d" %  pjugador + '\n')
archivo.write('Puntaje del bot: ' + "%d" %   pbot + '\n')
archivo.write('Empates: ' + "%d" %   empate + '\n')
archivo.write('----------------'+ '\n')


archivo.close()

















































































































































































































































































































































