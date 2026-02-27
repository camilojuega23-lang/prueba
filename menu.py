import os
from saludo import saludo
from despedida import despedida

def limpiarPantalla():
    os.system("cls")

def menu():
    while True:
        print('1.saludar')
        print('2.despedirse')
        print('3.salir')

        opcion = int(input("ingrese la opcion"))

        match opcion:
            case 1:
                limpiarPantalla()
                saludo()
                print('a')
            case 2:
                limpiarPantalla()
                despedida()
                print('a')
            case 3:
                limpiarPantalla()
                print('salida')
                break
            case _:
                limpiarPantalla()
                print('accion no valida')

if __name__ == "__main__":
    menu()
