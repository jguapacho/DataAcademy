def area_triangulo():
    base = int(input("¿Cúal es la base? "))
    altura =int(input("¿Cúal es la altura?"))
    area = (base*altura)/2
    print("El area del triangulo es: "+ str(area))
def pie_pap_tij():
    cont_jugador_1 = 0
    cont_jugador_2 = 0
    for i in range(3):
        jugador_1=input("Jugador 1: Escoja entre piedra, papel o tijera: ")
        jugador_2=input("Jugador 2: Escoja entre piedra, papel o tijera: ")
        if  jugador_1== "tijera" and jugador_2 == "papel":
            print("Ganador jugador 1")
            cont_jugador_1 += 1
        elif jugador_1== "piedra" and jugador_2 == "tijera":
            print("Ganador jugador 1")
            cont_jugador_1 += 1
        elif jugador_1== "papel" and jugador_2 == "piedra":
            print("Ganador jugador 1")
            cont_jugador_1 += 1
        elif  jugador_2== "tijera" and jugador_1 == "papel":
            print("Ganador jugador 2")
            cont_jugador_2 += 1
        elif jugador_2== "piedra" and jugador_1 == "tijera":
            print("Ganador jugador 2")
            cont_jugador_2 += 1
        elif jugador_2== "papel" and jugador_1 == "piedra":
            print("Ganador jugador 2")
            cont_jugador_2 += 1
        elif jugador_2 == jugador_1:
            print("Empate")
        else:
            print('La opción no es valida')
    if cont_jugador_1 > cont_jugador_2:
        print('El ganador es el jugador 1')
    else:
        print('El ganador es el jugador 2')
def conv_millas_km():
    millas = int(input('ingrese la millas: '))
    print('Las millas ingresadas equivalen a: '+ str(millas*1.609344) + ' km')
def cal_vol():
    pass
def ran_camb():
    pass

def run():
    pass
    print("Reto 1 - Área de un triángulo")
    print("Reto 2 - Piedra, papel o tijera")
    print("Reto 3 - Conversor de millas a kilómetros")
    print("Reto 4 - Calculadora de volúmenes")
    print("Reto 5 - Rangos cambiantes")

    eleccion = input('Elija el reto: ')
    if eleccion == "1":
        area_triangulo()
    elif eleccion == "2":
        pie_pap_tij()
    elif eleccion == "3":  
        conv_millas_km()
    elif eleccion == "4":
        cal_vol()
    elif eleccion == "5":
        ran_camb()
    else:
        print('La opción no es valida')

if __name__ == '__main__':
    run()
