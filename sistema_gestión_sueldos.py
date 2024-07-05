import csv
import random

trabajadores = [
    {"nombre": "Juan Pérez", "cargo": "Consultor TI"},
    {"nombre": "María García", "cargo": "Analista"},
    {"nombre": "Carlos López", "cargo": "Programador"},
    {"nombre": "Ana Martínez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Pedro Rodríguez", "cargo": "Consultor TI"},
    {"nombre": "Laura Hernández", "cargo": "Analista"},
    {"nombre": "Miguel Sánchez", "cargo": "Programador"},
    {"nombre": "Isabel Gómez", "cargo": "Jefe de Proyecto"},
    {"nombre": "Francisco Díaz", "cargo": "Consultor TI"},
    {"nombre": "Elena Fernández", "cargo": "Analista"}
]

sueldos=[]

sueldo_min=300000
sueldo_max=2500000

def asignar():
    for trabajador in trabajadores:
        sueldo=int(random.randint(sueldo_min,sueldo_max))
        trabajador["sueldo"]=sueldo
    print('Sueldos asignados aleatoriamente.')

def clasificar():
    #Sueldos menores a $800.000:
    monto1=0
    monto2=0
    monto3=0
    contador1=1
    for trabajador in trabajadores:
        if trabajador['sueldo'] <800000:
            contador1+=1
    print(f'Sueldos menores a $800.000 Total: {contador1}')
    print('Nombre\t\t\tCargo\t\t\tSueldo')
    print(f'{trabajador['nombre']}\t\t{trabajador['cargo']}\t\t{trabajador['sueldo']}')
    for trabajador in trabajadores:
        if trabajador['sueldo']<800000:
            print(f'{trabajador['nombre']}\t\t{trabajador['cargo']}\t\t{trabajador['sueldo']}')
            monto1=trabajador['sueldo']
    #Sueldos entre $800.000 y $2.000.000:
    contador2=1
    for trabajador in trabajadores:
        if trabajador['sueldo'] > 800000 and trabajador['sueldo']<2000000:
            contador2+=1
    print(f'\nSueldos menores a $800.000 Total: {contador2}')
    print('Nombre\t\t\tCargo\t\t\tSueldo')
    print(f'{trabajador['nombre']}\t\t{trabajador['cargo']}\t\t{trabajador['sueldo']}')
    for trabajador in trabajadores:
        if trabajador['sueldo' ] > 800000 and trabajador['sueldo']<2000000:
            print(f'{trabajador['nombre']}\t\t{trabajador['cargo']}\t\t${trabajador['sueldo']}')
            monto2=trabajador['sueldo']
    #Sueldos mayores a $2.000.000:
    contador3=1
    for trabajador in trabajadores:
        if trabajador['sueldo'] >= 2000000:
            contador3+=1
    print(f'\nSueldos mayores a $2.000.000 Total: {contador3}')
    print('Nombre\t\t\tCargo\t\t\tSueldo')
    print(f'{trabajador['nombre']}\t\t{trabajador['cargo']}\t\t{trabajador['sueldo']}')
    for trabajador in trabajadores:
        if trabajador['sueldo' ] >= 2000000:
            print(f'{trabajador['nombre']}\t\t{trabajador['cargo']}\t\t${trabajador['sueldo']}')
            monto3=trabajador['sueldo']
    total=monto1+monto2+monto3
    print(f'Total sueldos: ${total}')

def estadisticas():
        #Acá se crea una comprensión de listas. Es una forma concisa de crear listas en Python.
        #Trabaja de esta formar: [nueva_lista_elemento for elemento in iterable]
        #Acá se creó la lista trabajado['sueldo'] y se asignó a la variable sueldos 
        #Para cada trabajador en la lista inicial "trabajadores", se extrae el valor asociado con la clave 'sueldo'.
        #[trabajador['sueldo'] for trabajador in trabajadores]: Esta comprensión de listas crea una nueva 
        #La lista que contiene solo los valores de los sueldos de cada trabajador.
        sueldos=[trabajador['sueldo'] for trabajador in trabajadores]
        sueldo_maximo=max(sueldos)
        sueldo_minimo=min(sueldos)
        total_sueldos=sum(sueldos)
        cant_sueldos=len(sueldos)
        promedio=int(total_sueldos/cant_sueldos)
        producto_sueldos=1
        for sueldo in sueldos:
            producto_sueldos*=sueldo
        media_geometrica=int(producto_sueldos**(1/cant_sueldos))
        print(f'El sueldo máximo es: ${sueldo_maximo}')
        print(f'El sueldo mínimo es: ${sueldo_minimo}')
        print(f'EL sueldo promedio es: ${promedio}')
        #print(f'La media geométrica es: ${media_geometrica:.2f}')
        #El :.2f es un especificador de formato que se utiliza para dar formato a números de punto flotante (decimales) 
        #cuando se utilizan dentro de una cadena formateada (f-string).
        # : introduce el especificador de formato.
        # .2 indica que se deben mostrar dos cifras decimales.
        # f indica que el número debe formatearse como un número de punto flotante (decimal).
        #Por ejemplo, si media_geometrica es 123.456789, se imprimirá como 123.46.
        print(f'La media geométrica es: ${media_geometrica}')

def exportar():
    with open ('bbdd.csv','w',newline='') as archivo_csv:
        escritor_csv=csv.writer(archivo_csv)
        escritor_csv.writerow(['Nombre','Cargo','Sueldo base','Descuento Salud','Descuento AFP','Sueldo líquido'])
        for trabajador in trabajadores:
            escritor_csv.writerow([trabajador['nombre'],trabajador['cargo'],trabajador['sueldo'],trabajador['descuentosalud'],trabajador['descuentoafp'],trabajador['sueldoliquido']])
    print('Archivo exportado exitosamente')


def calculo():
    salud=0.07
    afp=0.12
    print('Nombre\t\t\tCargo\t\t\tSueldo base\t\tdescuento salud\t\tdescuento afp\t\tsueldo liquido')
    for trabajador in trabajadores:
        sueldo=trabajador['sueldo']
        descuento_en_salud=int(sueldo*salud)
        trabajador['descuentosalud']=descuento_en_salud
        descuento_en_afp=int(sueldo*afp)
        trabajador['descuentoafp']=descuento_en_afp
        sueldo_liquido=int(sueldo-descuento_en_salud-descuento_en_afp)
        trabajador['sueldoliquido']=sueldo_liquido
        print(f'{trabajador['nombre']}\t\t{trabajador['cargo']}\t\t${trabajador['sueldo']}\t\t${trabajador['descuentosalud']}\t\t\t${trabajador['descuentoafp']}\t\t\t${trabajador['sueldoliquido']}')
    exportar()

def salida():
    print('Saliendo de programa')
    print(f'Desarrollado por Jonathan Saravia Zurita')
    print(f'Rut 18.534.141-0')

while True:
    print("\nMenú: ")
    print('1)Asignar sueldos: ')
    print('2)Clasificar sueldos: ')
    print('3)Ver estadísticas: ')
    print('4)Generar reportes: ')
    print('5)Salir del programa: ')
    op=int(input('Indica lo que deseas realizar: \n'))
    if op==1:
        asignar()
    elif op==2:
        clasificar()
    elif op==3:
        estadisticas()
    elif op==4:
        calculo()
    elif op==5:
        salida()
        break