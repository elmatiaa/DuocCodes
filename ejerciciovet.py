import os
import time as t
import msvcrt as ms
import random as r

mascota=[]
mascotas=[]

#Menú
def menu():
    print("--MENU--\n")
    print("1. Registrar mascota\n2. Listar todos los registros\n3. Buscar mascota\n4. Imprimir reportes\n5. Salir ")
    print("\n---------------")

#Registro
def regm():
    w1=1
    os.system("Cls")
    print("--REGISTRO DE MASCOTAS--\n")
    while w1==1:
        idmascota= input("Ingrese el ID de la mascota\n> ")
        if len(idmascota)==5 and idmascota.isdigit():
            w1=0
            for mascota in mascotas:
                if mascota[0]==idmascota:
                    os.system("Cls")
                    print("--REGISTRO DE MASCOTAS--\n")
                    print("La ID ya existe, ingrese otra.")
                    w1=1
        else:
            os.system("Cls")
            print("--REGISTRO DE MASCOTAS--\n\nIngrese un codigo válido.\n")
    namem= input("Ingrese el nombre de la mascota\n> ")
    namem=namem.capitalize()
    named= input("Ingrese el nombre del dueño\n> ")
    named=named.capitalize()
    op1= (input("La mascota es (P)erro o (G)ato?\n> "))
    if op1=="P" or op1=="p":
        tipom= "Perro"
    elif op1=="G" or op1=="g":
        tipom= "Gato"
    mascota=[idmascota,namem,named,tipom]
    mascotas.append(mascota)
    print("La mascota fue registrada con éxito, presione una tecla para volver al menu.")
    ms.getch()

#Buscador
def buscar(idmascota):
    os.system("Cls")
    print("--BUSCAR MASCOTA--\n")
    i=1
    for mascota in mascotas:
        if mascota[0]==idmascota:
            print(f"ID: {mascota[0]}")
            print(f"Nombre: {mascota[1]}")
            print(f"Dueño: {mascota[2]}")
            print(f"Tipo: {mascota[3]}")
            print("\nPresione una tecla para ingresar otra.")
            ms.getch()
            i=0
    if i==1:
            os.system("Cls")
            print("--BUSCAR MASCOTA--\n")
            print("La ID que escribió no existe, presione una tecla para ingresar otra.\n")
            ms.getch()

#Listado completo
def listar():
    os.system("Cls")
    print("--LISTADO DE MASCOTAS--\n")
    for mascota in mascotas:
        print(f"ID: {mascota[0]}")
        print(f"Nombre: {mascota[1]}")
        print(f"Dueño: {mascota[2]}")
        print(f"Tipo: {mascota[3]}\n")
    print("Presione una tecla para volver al menu. ")
    ms.getch()

#Reporte de perros
def reportesp():
    os.system("Cls")
    print("--REPORTES--\n")
    nump=0
    for mascota in mascotas:
        if mascota[3]=="Perro":
            numr= r.randint(1,10)
            print(f"ID: {mascota[0]}")
            print(f"Nombre: {mascota[1]}")
            print(f"Tipo: {mascota[3]}")
            print(f"\nSr/a {mascota[2]}:\nLe informamos que a su mascota le fantan {numr} vacuna/s.\n-----------\n")
            nump=nump+1
    print(f"El numero de perros registrados es: {nump}\nPresione una tecla para volver al menu. ")
    ms.getch()
        
#Reporte de gatos
def reportesg():
    os.system("Cls")
    print("--REPORTES--\n")
    numg=0
    for mascota in mascotas:
        if mascota[3]=="Gato":
            numr= r.randint(1,10)
            print(f"ID: {mascota[0]}")
            print(f"Nombre: {mascota[1]}")
            print(f"Tipo: {mascota[3]}")
            print(f"\nSr/a {mascota[2]}:\nLe informamos que a su mascota le fantan {numr} vacuna/s.\n-----------\n")
            numg=numg+1
    print(f"El numero de gatos registrados es: {numg}\nPresione una tecla para volver al menu. ")
    ms.getch()

#MAIN CODE
w2=1
w4=1
while w2==1:
    w3=1
    try:
        os.system("Cls")
        menu()
        op= int(input("Ingrese una opción\n> "))
        if op==1:
            regm()
        elif op==2:
            listar()
        elif op==3:
            while w3==1:
                os.system("Cls")
                print("--BUSCAR MASCOTA--\n")
                idmascota= input("Ingrese el ID de la mascota o 'X' para volver al menu.\n> ")
                if len(idmascota)==5:
                    buscar(idmascota)
                elif idmascota=="X" or idmascota=="x":
                    os.system("Cls")
                    print("--BUSCAR MASCOTA--\n")
                    print("Volverá al menu...")
                    t.sleep(2)
                    w3=0
                else:
                    os.system("Cls")
                    print("--BUSCAR MASCOTA--\n")
                    print("Ingresó una ID no válida, presione una tecla para volver a intentar.")
                    ms.getch()
        elif op==4:
            os.system("Cls")
            print("--REPORTES--\n")
            op2= int(input("¿Para que mascotas desea los reportes?\n1. Perros\n2. Gatos\n> "))
            if op2==1:
                reportesp()
            elif op2==2:
                reportesg()
        elif op==5:
            w2=0
            os.system("Cls")
            print("Hasta luego ;)\n")
            t.sleep(0.5)
    except:
        print("Ha ocurrido un error, presione una tecla para intentar de nuevo.")
        ms.getch()