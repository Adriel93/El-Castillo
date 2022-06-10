# ------------------------------------------------------------------
#
# El Castillo (v1.0)
#
# ╭━━━┳╮╱╭━━━╮╱╱╱╱╱╭╮╱╭╮╭╮
# ┃╭━━┫┃╱┃╭━╮┃╱╱╱╱╭╯╰╮┃┃┃┃
# ┃╰━━┫┃╱┃┃╱╰╋━━┳━┻╮╭╋┫┃┃┃╭━━╮
# ┃╭━━┫┃╱┃┃╱╭┫╭╮┃━━┫┃┣┫┃┃┃┃╭╮┃
# ┃╰━━┫╰╮┃╰━╯┃╭╮┣━━┃╰┫┃╰┫╰┫╰╯┃
# ╰━━━┻━╯╰━━━┻╯╰┻━━┻━┻┻━┻━┻━━╯
#Mi primer proyecto minimalista.
#Escrito en Python 
#
# Codigo avalible en: https://github.com/Adriel93/El-Castillo
#
# ------------------------------------------------------------------



from pickle import TRUE
from time import sleep
import random

global posionHP
posionHP = 0
global posionMP
posionMP = 0
global pluma 
pluma = 0
global libro
libro = 0
global llave
llave = 0
global collar
collar = 0
global estaca
estaca = 0
global armario
armario = 1
global abierto1
abierto1 = 1
global armarioSec
armarioSec = 1
global cajon1
cajon1 = 1
global cajon2
cajon2 = 1
global cajon3
cajon3 = 1
global armario2
armario2 = 1
global vampiro
vampiro =1


def inventario():
    global posionHP
    global posionMP
    global pluma 
    global libro
    global llave
    global collar
    global estaca

    print("----------")
    print("INVENTARIO")
    print("----------")
    print("Posion de vida---------------{}".format(posionHP))
    print("Posion de mana---------------{}".format(posionMP))
    print("Pluma------------------------{}".format(pluma))
    print("Libros-----------------------{}".format(libro))
    print("Llaves-----------------------{}".format(llave))
    print("Collar-----------------------{}".format(collar))
    print("Estaca-----------------------{}".format(estaca))




def cofre():
    global posionHP
    global posionMP
    global pluma 
    global libro
    global llave
    global collar
    global estaca
 
    cofreRandom = random.randrange(1,4)
    #print(cofreRandom)
    if cofreRandom == 1:
        objetosRandom = random.randrange(1,4)
        #print(objetosRandom)
        if objetosRandom == 1:
            posionHP +=1
            posionMP +=1
            print("Has encontrado una posion de mana y otra de vida")
        elif objetosRandom == 2:
            posionHP +=2
            posionMP +=1
            print("Has encontrado una posion de mana y dos de vida")
        elif objetosRandom == 3:
            posionMP +=1
            print("Has encontrado una posion de mana")

    elif cofreRandom == 2:
        objetosRandom = random.randrange(1,4)
        #print(objetosRandom)
        if objetosRandom == 1:
            posionHP +=1
            print("Has encontrado una posion de vida")
        elif objetosRandom == 2:
            libro +=1
            posionMP +=1
            print("Has encontrado un libro y una posion de mana")
        elif objetosRandom == 3:
            pluma +=1
            print("Has encontrado una pluma")

    elif cofreRandom == 3:
        objetosRandom = random.randrange(1,4)
        #print(objetosRandom)
        if objetosRandom == 1:
            llave +=1
            print("Has encontrado una llave")
        elif objetosRandom == 2:
            estaca +=1
            posionMP +=1
            print("Has encontrado un estaca y una posion de mana")
        elif objetosRandom == 3:
            collar +=1
            print("Has encontrado un collar")


#EN LAS AFUERAS DEL CASTILLO
def start():
    print("╭━━━┳╮╱╭━━━╮╱╱╱╱╱╭╮╱╭╮╭╮")
    sleep(1)
    print("┃╭━━┫┃╱┃╭━╮┃╱╱╱╱╭╯╰╮┃┃┃┃")
    sleep(1)
    print("┃╰━━┫┃╱┃┃╱╰╋━━┳━┻╮╭╋┫┃┃┃╭━━╮")
    sleep(1)
    print("┃╭━━┫┃╱┃┃╱╭┫╭╮┃━━┫┃┣┫┃┃┃┃╭╮┃")
    sleep(1)
    print("┃╰━━┫╰╮┃╰━╯┃╭╮┣━━┃╰┫┃╰┫╰┫╰╯┃")
    sleep(1)
    print("╰━━━┻━╯╰━━━┻╯╰┻━━┻━┻┻━┻━┻━━╯")
    sleep(1)
    print("Llegas a las afueras del castillo")
    sleep(1)
    print("Es casi de noche, y hace frio")
    sleep(1)
    print("Estas cansado, y quisieras reposar un poco")
    sleep(1)
    print('Delante de ti esta el imponente Castillo de "La Roca" ')
    sleep(1)
    outCastle()


def outCastle():
    while TRUE:
        print("-------------------")
        print("Que deseas hacer?")
        print("-------------------")
        print("1-Mirar")
        print("2-Ir a la puerta")
        print("3-Regresar")
        seleccion = int(input("Eleccion: "))
        if seleccion == 1:
            print("\nEL castillo se ve enorme, con una puerta que parece que dentro viviera un gigante")
            sleep(1)
            print("La puerta parece entre abierta,quiza pudiera refugiarme dentro")
            sleep(2)
            continue
        elif seleccion == 2:
            print("Te diriges a la enorme puerta principal y la empujas")
            sleep(2)
            entradaSP()

        elif seleccion == 3:
            print("Es demasiado tarde, imposible regresar ya")
            sleep(1)
            continue
 #Entrada en el salon principal
def entradaSP():
    print("Acabas de entar al castillo")
    print("PAAAAAAAMMMMMM")
    print("La puerta se cierra tras de ti")
    salonPrincipal()


#SALON_PRINCIPAL
def salonPrincipal():
    while TRUE:
        print("-------------------")
        print("Estas en el Salon principal")
        print("Que deseas hacer?")
        print("-------------------")
        print("1-Salon")
        print("2-Comedor")
        print("3-Escalera")
        seleccion = int(input("Eleccion: "))
        if seleccion == 1:
            print("A traves de un marco roto se ve la entrada a otro salon")
            print("Me movere hasta alli")

        elif seleccion == 2:
            print("El comedor es un lugar espacioso, se ve una mesa larga y platos alli servidos")
            print("cuando te acercas un poco te das cuenta que lleban bastante tiempo alli ")
            print("A lado derecho del comedor se ve una puerta, debe ser la coina")
            irCocina = input("Ir a la cocina? (y/n)")
            if irCocina == "y":
                cocina()
            elif irCocina == "n":
                print("No te interesa")
                continue
        elif seleccion == 3:
            print("La escalera parece tener algunos escalones rotos")
            print("Debo tener cuidado al subir")
            sleep(1)
            segundaPlanta()
#COCINA
def cocina():
    global armario
    while TRUE:
        print("-------------------")
        print("Estas en la cocina")
        print("Que deseas hacer?")
        print("-------------------")
        print("1-Mirar")
        print("2-Regresar a el Salon Principal")
        seleccion = int(input("Eleccion: "))
        if seleccion == 1:
            print("\nLa cocina se ve que es un desastre, las ratas acampan a sus anchas")
            sleep(1)
            print("Te detienes en un armario que hay al lado de el fregadero")
            abrir = input("Deseas abrirlo (y/n)")
            if abrir == "y":
                if armario == 1:
                    cofre()
                    armario -=1
                    continue
                else:
                    print("No hay nada dentro")
            elif abrir == "n":
                print("No te interesa")
                continue
        elif seleccion == 2:
            print("Te diriges nuevamente al salon principal")
            salonPrincipal()

#SEGUNDA PLANTA
def segundaPlanta():
    while TRUE:
        print("-------------------")
        print("Estas en la Segunda Planta")
        print("Que deseas hacer?")
        print("-------------------")
        print("1-Primer dormitorio")
        print("2-Segundo Dormitorio")
        print("3-Escalera")
        print("4-Inventario")

        seleccion = int(input("Eleccion: "))
        if seleccion == 1:
            dormitorio1()

        elif seleccion == 2:
            dormitorio2()

        elif seleccion == 3:
            print("La escalera parece tener algunos escalones rotos")
            print("Debo tener cuidado al subir")
            sleep(1)
            asotea()
        elif seleccion == 4:
            inventario()

#Dormitorio1
def dormitorio1():
    global abierto1
    global llave
    print("-------------------")
    print("Te paras enfrente de la puerta")
    if abierto1 == 1:
        if llave >=1:
            print("Utilizas un llave para intentar abrir la puerta")
            sleep(1)
            print("Abres la puerta lentamente.....")
            print("El dormitorio esta hecho un desastre, ")
            print("pareciera que desde que esta abandonado el lugar nadie pasa por el")
            abierto1 -=1
            llave -=1
            dentroDor1()
        else:
            print("Necesitas una llave para abrir esta puerta")
            sleep(1)
            segundaPlanta()
    elif abierto1 == 0:
        dentroDor1()

def dentroDor1():
    global armarioSec
    global cajon1
    global cajon2

    while TRUE:
        print("-------------------")
        print("Estas en el Primer Dormitorio")
        print("Que deseas hacer?")
        print("-------------------")
        print("1-Revizar Armario")
        print("2-Revizar cajon al lado de la cama")
        print("3-Revizar cajon al lado de la puerta")
        print("4-Salir del dormitorio")

        seleccion = int(input("Eleccion: "))
        #REVIZANDO ARMARIO
        if seleccion == 1:
            print("\nEl armario se ve que es un desastre, las ratas se han comido toda la ropa")
            sleep(1)
            if armarioSec == 1:
                print("Te detienes en una palanca que hay dentro de armario")
                print("detras de unas ropas viejas")
                abrir = input("Deseas tirar de la palanca? (y/n)")
                if abrir == "y":
                    cofre()
                    armarioSec -=1
                    continue
                elif abrir == "n":
                    print("No te interesa")
                    continue
            else:
                print("Detras el compartimento secreto, que ya no tiene nada")
       #REVIZANDO CAJON AL LADO DE LA CAMA         
        elif seleccion == 2:
            if cajon1 == 1:
                print("Mueves la cama un poco y levantas la tapa del cajon")
                cofre()
                cajon1 -=1
                continue
            else:
                print("El cajon no tiene nada dentro")
        #REVIZANDO CAJON AL LADO DE LA PUERTA
        elif seleccion == 3:
            if cajon2 == 1:
                print("Levantas la tapa del cajon")
                cofre()
                cajon2 -=1
                continue
            else:
                print("El cajon no tiene nada dentro")
        elif seleccion == 4:
            print("Sales del dormitorio")
            segundaPlanta()

def dormitorio2():
    global armario2
    global cajon3
    while TRUE:
        print("-------------------")
        print("Estas en el Segundo Dormitorio")
        print("Que deseas hacer?")
        print("-------------------")
        print("1-Revizar Armario")
        print("2-Revizar cajon al lado de la cama")
        print("3-Salir del dormitorio")

        seleccion = int(input("Eleccion: "))
        #REVIZANDO ARMARIO
        if seleccion == 1:
            print("\nEl armario se ve que es un desastre, las ratas se han comido toda la ropa")
            sleep(1)
            if armario2 == 1:
                print("Revizas dentro de las ropas y cajones del armario")
                cofre()          
                continue
            elif armario2 == 0:
                print("Parece que ya revisastes aqui, no hay nada dentro")
        #REVIZANDO CAJON AL LADO DE LA CAMA         
        elif seleccion == 2:
            if cajon3 == 1:
                print("Mueves la cama un poco y levantas la tapa del cajon")
                cofre()
                cajon3 -=1
                continue
            else:
                print("El cajon no tiene nada dentro")
       
        elif seleccion == 3:
            print("Sales del dormitorio")
            segundaPlanta()

def asotea():
    vidaVamp = 350
    vidaheroe = 150
    global llave
    global estaca
    global collar
    global posionHP
    global posionMP

    if vampiro == 1:
        while TRUE:
            print("-----------------")
            print("Atacar al vampiro")
            print("-----------------")
            print("1.Atacar con la mano")
            print("2.Atacar con la llave")
            print("3.Atacar con collar")
            print("4.Atacar con la estaca")
            print("5.Usar posion de vida")
            print("6.Usar posion de mana")
            print("7.Inventario")
            print("8.Huir")
            #print(vidaVamp)
            #print(vidaheroe)
            if vidaVamp > 0 and vidaheroe > 0 :
                ataque = int(input("Escoja la opcion: "))
                if ataque == 1:
                    Ataque = random.randint(6,12)
                    vidaVamp = vidaVamp - Ataque
                    print("Has ocacionado {} puntos de daño".format(Ataque))   
                    AtaqueVamp = random.randint(25,50)
                    vidaheroe = vidaheroe - AtaqueVamp
                    print("El vampiro te devuelve un golpe de {} puntos de daño".format(vidaheroe))
                    continue
                if ataque == 2:
                    if llave >0:
                        Ataque = random.randint(8,12)
                        vidaVamp = vidaVamp - Ataque
                        llave -=1
                        print("Has ocacionado {} puntos de daño".format(Ataque))
                        AtaqueVamp = random.randint(25,50)
                        vidaheroe = vidaheroe - AtaqueVamp
                        print("El vampiro te devuelve un golpe de {} puntos de daño")                        
                        continue
                    else:
                        print("No tienes ninguna llave para atacar")
                        continue
                if ataque == 3:
                    if collar > 0:
                        print("Sacas un collar del bolsillo, este empieza a brillar")
                        Ataque = random.randint(20,70)
                        vidaVamp = vidaVamp - Ataque
                        collar -=1
                        print("Has ocacionado {} puntos de daño".format(Ataque))
                        AtaqueVamp = random.randint(25,50)
                        vidaheroe = vidaheroe - AtaqueVamp
                        print("El vampiro te devuelve un golpe de {} puntos de daño")                        
                        continue
                    else:
                        print("No tienes ningun collar para atacar")
                        continue
                if ataque == 4:
                    if estaca > 0:
                        print("Empuñas la estaca en tu mano y sales corriendo hacia el")
                        Ataque = random.randint(50,100)
                        vidaVamp = vidaVamp - Ataque
                        estaca -=1
                        print("Has ocacionado {} puntos de daño".format(Ataque))
                        AtaqueVamp = random.randint(25,50)
                        vidaheroe = vidaheroe - AtaqueVamp
                        print("El vampiro te devuelve un golpe de {} puntos de daño".format(AtaqueVamp))
                        continue
                    else:
                        print("No tienes ninguna estaca para atacar")
                        continue
                if ataque == 5:
                    if posionHP > 0:
                        print("Bebes de un sorbo la posion")
                        vidaheroe +=20
                        continue
                    else:
                        print("No tienes ninguna posion de vida")
                        continue
                if ataque == 6:
                    if posionMP > 0:
                        print("Bebes de un sorbo la posion")
                        vidaheroe +=20
                        continue
                    else:
                        print("No tienes ninguna posion de mana")
                        continue
                if ataque == 7:
                    inventario()
                    continue
                if ataque == 8:
                    print("Sales corriendo en busca de la escalera por donde subiste")
                    print("Te caes por la escalera, ya que estaba rota")
                    print("HAS MUERTO")
                    seleccion = input("Deseas comenzar de nuevo? (y/n)")
                    if seleccion == "y":
                        start()
                        break
                    elif seleccion == "n":
                        exit()
            elif vidaheroe <= 0:
                print("HAS MUERTO")
                seleccion = input("Deseas comenzar de nuevo? (y/n)")
                if seleccion == "y":
                    start()
                    break
                elif seleccion == "n":
                    exit()
            else:
                print("HAS GANADO")
                seleccion = input("Deseas comenzar de nuevo? (y/n)")
                if seleccion == "y":
                    start()
                    break
                elif seleccion == "n":
                    exit()
start()

