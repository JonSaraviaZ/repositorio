#Desarrolla un programa en Python para un sistema de ventas de juegos de consolas en una tienda de videojuegos en DUOC UC. 
#El programa debe permitir a los usuarios realizar las siguientes acciones a través de un menú interactivo:

#1.	Registrar una venta.
#2.	Mostrar todas las ventas.
#3.	Buscar ventas por cliente.
#4.	Guardar las ventas en un archivo.
#5.	Cargar las ventas desde un archivo.
#6.	Generar factura.
#7.	Salir del programa.

#Requisitos:

#Menú Interactivo: El programa debe presentar un menú con las opciones mencionadas y permitir al usuario seleccionar una opción.
#Listas y Diccionarios: Utilizar listas y diccionarios para almacenar la información de las ventas.
#Archivos: Implementar la funcionalidad para guardar las ventas en un archivo y cargar las ventas desde un archivo.
#Funciones: Utilizar funciones para cada una de las funcionalidades del menú.
#Descuentos: Aplicar descuentos según el tipo de cliente:
#Estudiante: 15%
#Trabajador: 10%
#Socio: 20%

#Precios:
#Playstation - Acción - $10000
#Playstation - Aventura - $20000
#Playstation - Deportes - $30000
#Playstation - RPG - $40000
#Xbox - Acción - $11000
#Xbox - Aventura - $21000
#Xbox - Deportes - $31000
#Xbox - RPG - $41000
#Nintendo - Acción - $12000
#Nintendo - Aventura - $22000
#Nintendo - Deportes - $32000
#Nintendo - RPG - $42000

#El sistema debe también considerar el tipo de consola (PlayStation, Xbox, Nintendo) y el tipo de juego (Acción, Aventura, Deportes, RPG) al registrar una venta.

#Boleta o Factura : generar boleta o Factura con fecha y hora en el sistema de ventas de pizzas

import json
import os
from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME,"es_ES")

fecha_actual=datetime.now()

fecha=fecha_actual.strftime("%A, %d - %m - %Y")
hora=fecha_actual.strftime("%H:%M:%S")

juegos=[]

precios={
    #Numeros del 1 al 3 para las consolas
    #abreviaciones para el género del juego
    #Nombres reales de los juegos
    "1":{"av":{"juego1":27990,"juego2":31990,"juego3": 28990}},
    "2":{"ac":{"juego1":9990,"juego2":36990},"dep":{"juego1":26990,"juego2":22990,"juego3":32990}},
    "3":{"dis":{"juego1":42990,"juego2":32990}},
}

dsctoe=0.15
dsctot=0.1
dsctos=0.2

def agregarpersona(rut,consola,gen,cantidades,estatus,juego):
    global juegos
    global precios
    sub= None
    descuento= None
    monto= None
    for consola in precios.keys():
        if consola == consola and gen in precios[consola]:
            if estatus =="e":
                nombreproducto=juego
                precioproducto=precios[consola][gen][juego]
                sub=precioproducto*cantidades
                descuento=int(sub*dsctoe)
                monto=int(sub-descuento)
                break
            elif estatus =="t":
                nombreproducto=juego
                precioproducto=precios[consola][gen][juego]
                sub=precioproducto*cantidades
                descuento=int(sub*dsctot)
                monto=int(sub-descuento)
                break
            elif estatus =="s":
                nombreproducto=juego
                precioproducto=precios[consola][gen][juego]
                sub=precioproducto*cantidades
                descuento=int(sub*dsctos)
                monto=int(sub-descuento)
                break
    #Ingresando los datos a la lista
    if sub is not None and descuento is not None and monto is not None:
        nueva_venta={
            "rutcliente":rut,
            "consola":consola,
            "genero":gen,
            "estatus":estatus,
            "cantidad":cantidades,
            "nombreproducto":nombreproducto,
            "subtotal":sub,
            "descuento":descuento,
            "monto":monto,
        }
        juegos.append(nueva_venta)

def agregarempresa(rutempresa,consola,gen,cantidades,estatus,juego):
    global juegos
    global precios
    sub= None
    descuento= None
    monto= None
    iva= None
    for consola in precios.keys():
        if consola == consola and gen in precios[consola]:
            if estatus =="e":
                nombreproducto=juego
                precioproducto=precios[consola][gen][juego]
                iva=int(precioproducto*0.19)
                sub=precioproducto*cantidades
                descuento=int(sub*dsctoe)
                monto=int(sub-descuento)
                break
            elif estatus =="t":
                nombreproducto=juego
                precioproducto=precios[consola][gen][juego]
                iva=int(precioproducto*0.19)
                sub=precioproducto*cantidades
                descuento=int(sub*dsctot)
                monto=int(sub-descuento)
                break
            elif estatus =="s":
                nombreproducto=juego
                precioproducto=precios[consola][gen][juego]
                iva=int(precioproducto*0.19)
                sub=precioproducto*cantidades
                descuento=int(sub*dsctos)
                monto=int(sub-descuento)
                break
    #Ingresando los datos a la lista
    if sub is not None and descuento is not None and monto is not None and iva is not None:
        nueva_venta={
            "rutcliente":rutempresa,
            "consola":consola,
            "genero":gen,
            "estatus":estatus,
            "cantidad":cantidades,
            "nombreproducto":nombreproducto,
            "subtotal":sub,
            "descuento":descuento,
            "iva":iva,
            "monto":monto,
        }
        juegos.append(nueva_venta)

#Busca los datos de la empresa por el tipo de cliente y rut
def buscar(rut):
    global juegos
    v1=int(input("Indica\n1 si es cliente persona o\n2 si es cliente empresa: "))
    if v1==1:  
        for busqueda in juegos:
            if rut in busqueda["rutcliente"]:
                print(f"\nRut cliente:{busqueda['rutcliente']}\nConsola:{busqueda['consola']}\nGénero:{busqueda['genero']}\nEstatus:{busqueda['estatus']}\nCantidad:{busqueda['cantidad']}\nNombre del juego:{busqueda['nombreproducto']}\nSubtotal: ${busqueda['subtotal']}\nDescuento:${busqueda['descuento']}\nMonto: ${busqueda['monto']}\n")
                break
            else:
                print("Rut del cliente no se encuentra.")
    elif v1==2:
        for busqueda in juegos:
            if rut in busqueda["rutcliente"]:
                print(f"\nRut cliente:{busqueda['rutcliente']}\nConsola:{busqueda['consola']}\nGénero:{busqueda['genero']}\nEstatus:{busqueda['estatus']}\nCantidad:{busqueda['cantidad']}\nNombre del juego:{busqueda['nombreproducto']}\nSubtotal: ${busqueda['subtotal']}\nDescuento:${busqueda['descuento']}\nIva:${busqueda['iva']}\nMonto: ${busqueda['monto']}\n")
                break
            else:
                print("Rut del cliente no se encuentra.")

def boletafactura(rut):
    global juegos
    cant=None
    subto=None
    descto=None
    monto=None
    for diccionario in juegos:
        if rut == diccionario['rutcliente']:
            doc=int(input("Indica\n1 si es cliente persona o\n2 si es cliente empresa: "))
            if doc==1:
                juego=diccionario['nombreproducto']
                cant=diccionario['cantidad']
                subto=diccionario['subtotal']
                descto=diccionario['descuento']
                monto=diccionario['monto']
                print("\nFecha y hora: ",fecha,hora)
                print("Boleta")
                print("-------------")
                print(f"Cantidad:{cant}\t{juego}")
                print("-------------")
                print(f"Subtotal\t${subto}")
                print(f"Descuento\t${descto}")
                print("-------------")
                print(f"Monto\t\t${monto}")
                break
            elif doc==2:
                rutempresa=diccionario['rutcliente']
                juego=diccionario['nombreproducto']
                cant=diccionario['cantidad']
                subto=diccionario['subtotal']
                iva=diccionario['iva']
                descto=diccionario['descuento']
                monto=diccionario['monto']
                print("\nFecha y hora: ",fecha,hora)
                print("Factura")
                print("-------------")
                print(f"Rut empresa:\t{rutempresa}")
                print(f"Cantidad:{cant}\t{juego}")
                print("-------------")
                print(f"Subtotal\t${subto}")
                print(f"Iva\t\t${iva}")
                print(f"Descuento\t${descto}")
                print("-------------")
                print(f"Monto\t\t${monto}")
                break


def guardar():
    with open('bbdd.json','w') as archivo:
        json.dump(juegos,archivo,ensure_ascii=False,indent=4)
        print("Archivo guardado")

while True:
    print("\nMenú:")
    print("1) Registrar una venta:")
    print("2) Mostrar todas las ventas:")
    print("3) Buscar ventas por cliente:")
    print("4) Guardar las ventas en un archivo:")
    print("5) Cargar las ventas desde un archivo:")
    print("6) Generar boleta o factura:")
    print("7) Salir del programa:")
    try:
        op=int(input("Indica lo que deseas realizar: "))
        if op==1:
            v1=int(input("Indica\n1 si es cliente persona o \n2 si es cliente empresa: "))
            if v1==1:
                rut=input("Indica el Rut del cliente: ").lower()
                consola=input("Indica\n1 para Nintendo,\n2 para PS5,\n3 para PS4: ").lower()
                if consola=="1":
                    gen=input("Indica\nav para aventura: ").lower()
                    juego=input("Indica el nombre del juego: ").lower()
                    cantidades=int(input("Indica la cantidad de juegos: "))
                    estatus=input('Indica E(estudiante), T(trabajador) o S(socio): ').lower()
                elif consola=="2":
                    gen=input("Indica\nac para acción\ndep para deporte: ").lower()
                    juego=input("Indica el nombre del juego: ").lower()
                    cantidades=int(input("Indica la cantidad de juegos: "))
                    estatus=input('Indica E(estudiante), T(trabajador) o S(socio): ').lower()
                elif consola=="3":
                    gen=input("Indica\ndis para disparos: ").lower()
                    juego=input("Indica el nombre del juego: ").lower()
                    cantidades=int(input("Indica la cantidad de juegos: "))
                    estatus=input('Indica E(estudiante), T(trabajador) o S(socio): ').lower()
                #Llama la funcionar agregarpersona()
                agregarpersona(rut,consola,gen,cantidades,estatus,juego)
                print("Venta registrada exitosamente.")
                continue
            elif v1==2:
                rutempresa=input("Indica el Rut del cliente: ").lower()
                consola=input("Indica\n1 para Nintendo,\n2 para PS5,\n3 para PS4: ").lower()
                if consola=="1":
                    gen=input("Indica\nav para aventura: ").lower()
                    juego=input("Indica el nombre del juego: ").lower()
                    cantidades=int(input("Indica la cantidad de juegos: "))
                    estatus=input('Indica E(estudiante), T(trabajador) o S(socio): ').lower()
                elif consola=="2":
                    gen=input("Indica\nac para acción\ndep para deporte: ").lower()
                    juego=input("Indica el nombre del juego: ").lower()
                    cantidades=int(input("Indica la cantidad de juegos: "))
                    estatus=input('Indica E(estudiante), T(trabajador) o S(socio): ').lower()
                elif consola=="3":
                    gen=input("Indica\ndis para disparos: ").lower()
                    juego=input("Indica el nombre del juego: ").lower()
                    cantidades=int(input("Indica la cantidad de juegos: "))
                    estatus=input('Indica E(estudiante), T(trabajador) o S(socio): ').lower()
                #Llama la funcionar agregarpersona()
                agregarempresa(rutempresa,consola,gen,cantidades,estatus,juego)
                print("Venta registrada exitosamente.")
                continue
        elif op==2:
            #Solo imprime los datos en la lista pizzas
            print(juegos)
        elif op==3:
            #Se piden los datos y se llama la funcion buscar(rut)
            rut=input("Indica el Rut del cliente: ").lower()
            buscar(rut)
        elif op==4:
            #Se llama la función guardar()
            guardar()
        elif op==5:
            #Se genera la carga del archivo en el programa
            with open('bbdd.json','r') as archivo:
                juegos=json.load(archivo)
                print('Archivo cargado exitosamente.')
        elif op==6:
            #Se piden los datos y se llama la funcion boleta(rut)
            rut=input("Indica el Rut del cliente: ").lower()
            boletafactura(rut)
        elif op==7:
            #Se sale del programa
            print("Saliendo")
            break
        else:
            #Se entrega un mensaje de error en caso de que no se indiquen los datos requeridos.
            print("Número incorrecto.\nIntenta nuevamente")
    except ValueError:
        print("Información ingresada es incorrecta.\nIntenta nuevamente")