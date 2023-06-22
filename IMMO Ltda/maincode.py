
import os
import time as t
import msvcrt as ms
import random as r
from funciones import *

#MAIN CODE
w4=1
while True:
    w3=1
    try:
        os.system("Cls")
        menu()
        op= int(input("Ingrese una opción\n> "))
        if op==1:
            reg()
        elif op==2:
            w2=1
            while w2==1:
                os.system("Cls")
                print("--BUSCAR CLIENTE--\n")
                rutcliente= input("Ingrese el RUT del cliente o 'X' para volver al menu (si el RUT contiene 'K' reemplacela por un '0').\n> ")
                if len(rutcliente)==8 or len(rutcliente)==9 and rutcliente.isdigit():
                    buscar(rutcliente)
                elif rutcliente=="X" or rutcliente=="x":
                    os.system("Cls")
                    print("--BUSCAR CLIENTE--\n")
                    print("Volverá al menu...")
                    t.sleep(1)
                    w2=0
                else:
                    os.system("Cls")
                    print("--BUSCAR CLIENTE--\n")
                    print("Ingresó un RUT no válido, presione una tecla para volver a intentar.")
                    ms.getch()
        elif op==3:
            os.system("Cls")
            print("--REPORTES SEGUN RENTA--\n")
            reportes()
        elif op==4:
            os.system("Cls")
            print("Hasta luego ;)\n")
            t.sleep(0.5)
            break
    except:
        print("Ha ocurrido un error, presione una tecla para intentar de nuevo.")
        ms.getch()