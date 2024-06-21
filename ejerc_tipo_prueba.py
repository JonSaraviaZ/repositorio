#Sistema de ventas de pizzas

#Contexto. 

#Debe permitir:

#1.	Registrar una venta.
#2.	Mostrar todas las ventas.
#3.	Buscar ventas por cliente.
#4.	Guardar las ventas en un archivo.
#5.	Cargar las ventas desde un archivo.
#6.	Generar Boleta
#7.	Salir del programa.

#Requisitos:

#•	Menú Interactivo: El programa debe presentar un menú con las opciones mencionadas y permitir al usuario seleccionar una opción.
#•	Listas y Diccionarios: Utilizar listas y diccionarios para almacenar la información de las ventas.
#•	Archivos: Implementar la funcionalidad para guardar las ventas en un archivo y cargar las ventas desde un archivo.
#•	Funciones: Utilizar funciones para cada una de las funcionalidades del menú.
#•	Descuentos: Aplicar descuentos según el tipo de usuario:
#Estudiante diurno: 15%
#Estudiante vespertino: 20%
#Administrativo: 10%

#El sistema debe también considerar el tipo de pizza (Peperoni, Mediterránea, Vegetariana) y el tamaño (Pequeña, Mediana, Familiar) al registrar una venta.

#Boleta: generar una boleta con fecha y hora en el sistema de ventas de pizzas

#Guardar proyecto en github y enviar link por ava.

#Lista de precios

#Pizza	        Tamaño	    Precio
#Peperoni	    Pequeña	    5.000
#Peperoni	    Mediana	    8.000
#Peperoni	    Familia	    10.000

#Mediterranea	Pequeña	    6.000
#Mediterranea	Mediana	    9.000
#Mediterranea	Familia	    12.000

#Vegetariana	Pequeña	    5.500
#Vegetariana	Mediana	    8.500
#Vegetariana	Familia	    11.000

#Escribí los códigos base para trabajar con json, guardar mi archivo e iniciar el formato de la fecha y hora
import json
import os
from datetime import datetime
#Con import locale establecí que quería los datos en español.
import locale
locale.setlocale(locale.LC_TIME,"es_ES")

fecha_actual=datetime.now()

#Acá dele entregué el formato a la fecha y hora. Además sumé el día con %A.
fecha=fecha_actual.strftime("%A, %d - %m - %Y")

hora=fecha_actual.strftime("%H:%M:%S")

#Declaré la lista llamada "Pizza"
pizzas=[]

#Establecí un diccionario anidado para los distintos tipos de pizzas y precios
precios={
    "pep":{"p":5000,"m":8000,"f":10000},
    "medi":{"p":6000,"m":9000,"f":12000},
    "vege":{"p":5500,"m":8500,"f":11000}
}

#Descuentos por tipo de jornada
dsctod=0.15
dsctov=0.20
dsctoa=0.1

#Generé una función agregar para realizar
def agregar(rut,tipos,tamaños,cantidades,jorn):
    global pizza
    global precios
    #Calculando el producto, descuento y monto final
    sub= None
    descuento= None
    monto= None
    for tipo in precios.keys():
        if tipos == tipo and tamaños in precios[tipo]:
            if jorn =="d":
                precioproducto=precios[tipo][tamaños]
                sub=precioproducto*cantidades
                descuento=int(sub*dsctod)
                monto=int(sub-descuento)
                break
            elif jorn =="v":
                precioproducto=precios[tipo][tamaños]
                sub=precioproducto*cantidades
                descuento=int(sub*dsctod)
                monto=int(sub-descuento)
                break
            elif jorn =="a":
                precioproducto=precios[tipo][tamaños]
                sub=precioproducto*cantidades
                descuento=int(sub*dsctod)
                monto=int(sub-descuento)
                break
    #Ingresando los datos a la lista
    if sub is not None and descuento is not None and monto is not None:
        nueva_venta={
            "rutcliente":rut,
            "tipo":tipos,
            "tamaño":tamaños,
            "jornada":jorn,
            "cantidad":cantidades,
            "subtotal":sub,
            "descuento":descuento,
            "monto":monto,
        }
        pizzas.append(nueva_venta)

#Realicé la función buscar(rut) para encontrar el rut que consulta el usuario
def buscar(rut):
    global pizzas
    for busqueda in pizzas:
        if rut in busqueda["rutcliente"]:
            print(f"\nRut cliente:{busqueda['rutcliente']}\nTipo:{busqueda['tipo']}\nTamaño:{busqueda['tamaño']}\nJornada:{busqueda['jornada']}\nCantidad:{busqueda['cantidad']}\nSubtotal: ${busqueda['subtotal']}\nDescuento:${busqueda['descuento']}\nMonto: ${busqueda['monto']}\n")
        else:
            print("Rut del cliente no se encuentra.")

#Realicé la función boleta(rut) para encontrar el rut que consulta el usuario e imprimir los datos por pantalla
def boleta(rut):
    global pizzas
    cant=None
    subto=None
    descto=None
    monto=None
    for diccionario in pizzas:
        if rut == diccionario['rutcliente']:
            cant=diccionario['cantidad']
            subto=diccionario['subtotal']
            descto=diccionario['descuento']
            monto=diccionario['monto']
            print("Fecha y hora: ",fecha,hora)
            print("\nBoleta")
            print("-------------")
            print(f"{cant} pizza")
            print("-------------")
            print(f"Subtotal\t${subto}")
            print(f"Descuento\t${descto}")
            print("-------------")
            print(f"Monto\t\t${monto}")
            break

#Realicé la función guardar() para grabar los datos en un archivo json
def guardar():
    with open('bbdd.json','w') as archivo:
        #con ensure_ascii=False,indent=4 le di un formato al orden interno de los archivos
        json.dump(pizzas,archivo,ensure_ascii=False,indent=4)
        print("Archivo guardado")

#Inicié el programa con un ciclo While True desplegando las opciones por pantalla
while True:
    print('\nMenú:')
    print('1) Registrar una venta.')
    print('2) Mostrar todas las ventas')
    print('3) Buscar ventas por cliente ')
    print('4) Guardar las ventas en un archivo')
    print('5) Cargar las ventas desde un archivo')
    print('6) Generar boleta')
    print('7) Salir del programa')
    #Usé un try y except para manejar errores imprevistos
    try:
        op=int(input("Indica lo que deaseas realizar: "))
        if op==1:
            #El programa comienza a pedir los datos para registrar las ventas
            rut=input("Indica el Rut del cliente: ").lower()
            tipos=input("Indica pep (pepperoni), medi(Mediterranea) o vege(vegetariana): ").lower()
            tamaños=input("Indica P(pequeña), M(mediana) o F(Familiar): ").lower()
            cantidades=int(input("Indica la cantidad de pizzas: "))
            jorn=input('Indica D(diurno), V(vespertino) o A(administrativo): ').lower()
            #Llama la funcionar agregar()
            agregar(rut,tipos,tamaños,cantidades,jorn)
            print("Venta registrada exitosamente.")
            continue
        elif op==2:
            #Solo imprime los datos en la lista pizzas
            print(pizzas)
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
                pizzas=json.load(archivo)
                print('Archivo cargado exitosamente.')
        elif op==6:
            #Se piden los datos y se llama la funcion boleta(rut)
            rut=input("Indica el Rut del cliente: ").lower()
            boleta(rut)
        elif op==7:
            #Se sale del programa
            print("Saliendo")
            break
        else:
            #Se entrega un mensaje de error en caso de que no se indiquen los datos requeridos.
            print("Número incorrecto.\nIntenta nuevamente")
    except ValueError:
        print("Información ingresada es incorrecta.\nIntenta nuevamente")