import os
import time as t
import msvcrt as ms
import random as r

persona=[]
personas=[]

#Menú
def menu():
    print("--MENU--\n")
    print("1. Registrar\n2. Buscar por RUT\n3. Reporte renta\n4. Salir ")
    print("\n---------------")

#Registro
def reg():
    w1=1
    os.system("Cls")
    print("--REGISTRO DE CLIENTES--\n")
    while w1==1:
        rutcliente= input("Ingrese el RUT del cliente (Si el RUT contiene una 'K' reemplacela por un '0').\n> ")
        if len(rutcliente)==8 or len(rutcliente)==9 and rutcliente.isdigit():
            w1=0
            for persona in personas:
                if persona[0]==rutcliente:
                    os.system("Cls")
                    print("--REGISTRO DE CLIENTES--\n")
                    print("El RUT ingresado ya existe, ingrese otro.")
                    w1=1
        else:
            os.system("Cls")
            print("--REGISTRO DE CLIENTES--\n\nIngrese un RUT válido.\n")
    namec= input("Ingrese el nombre del cliente\n> ")
    namec=namec.capitalize()
    apell= input("Ingrese el apellido del cliente\n> ")
    apell=apell.capitalize()
    op1= (input("\nIngrese el proyecto\n-Vive Santiago = VS\n-Vive La Florida = VF\n-Vive Ñuñoa = VN\n> "))
    if op1=="VS" or op1=="vs":
        proyecto= "Vive Santiago"
    elif op1=="VF" or op1=="vf":
        proyecto= "Vive La Florida"
    elif op1=="VN" or op1=="vn":
        proyecto= "Vive Ñuñoa"
    rmensual= int(input("Ingrese la renta mensual: \n> "))
    persona=[rutcliente,namec,apell,proyecto,rmensual]
    personas.append(persona)
    print("El cliente fue registrado con éxito, presione una tecla para volver al menu.")
    ms.getch()

#Buscador
def buscar(rutcliente):
    os.system("Cls")
    print("--BUSCAR CLIENTE--\n")
    i=1
    for persona in personas:
        if persona[0]==rutcliente:
            print(f"RUT: {persona[0]}")
            print(f"Nombre: {persona[1]} {persona[2]}")
            print(f"Proyecto: {persona[3]}")
            print(f"Renta mensual: ${persona[4]}")
            print("\nPresione una tecla para ingresar otro RUT.")
            ms.getch()
            i=0
    if i==1:
            os.system("Cls")
            print("--BUSCAR CLIENTE--\n")
            print("El RUT que ingresó no existe, presione una tecla para intentar de nuevo.\n")
            ms.getch()

#Listado completo
#def listar():
 #   os.system("Cls")
  #  print("--LISTADO DE MASCOTAS--\n")
   # for mascota in mascotas:
    #    print(f"ID: {mascota[0]}")
     #   print(f"Nombre: {mascota[1]}")
      #  print(f"Dueño: {mascota[2]}")
       # print(f"Tipo: {mascota[3]}\n")
    #print("Presione una tecla para volver al menu. ")
    #ms.getch()

#Reporte segun renta
def reportes():
    os.system("Cls")
    print("--REPORTES SEGUN RENTA--\n")
    numrep=0
    for persona in personas:
        if persona[4]>=900000:
            numr= r.randint(2500,3700)
            print(f"Reporte IMMO Ltda.:\nSr/a {persona[1]} {persona[2]}\nRUT: {persona[0]}\n")
            print(f"Con su renta mensual de: ${persona[4]}\nEn el proyecto: {persona[3]}")
            print(f"Puede acceder a un departamento de UF{numr}\n-----------\n")
            numrep=numrep+1
    print(f"Se generó {numrep} reporte/s.\nPresione una tecla para volver al menu. ")
    ms.getch()


