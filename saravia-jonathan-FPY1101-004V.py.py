import csv
import random

trabajadores = [
    {"nombre": "Juan Pérez"},
    {"nombre": "María García"},
    {"nombre": "Carlos López"},
    {"nombre": "Ana Martínez"},
    {"nombre": "Pedro Rodríguez"},
    {"nombre": "Laura Hernández"},
    {"nombre": "Miguel Sánchez"},
    {"nombre": "Isabel Gómez"},
    {"nombre": "Francisco Díaz"},
    {"nombre": "Elena Fernández"}
]

sueldo_minimo=300000
sueldo_maximo=2500000

valor1=800000
valor2=2000000


def asignar():
    for i in trabajadores:
        sueldo=random.randint(sueldo_minimo,sueldo_maximo)
        i["sueldos"]=sueldo
    print('Sueldos asignados aleatoriamente.')

def clasificar():
    global valor1
    global valor2
    monto1=0
    monto2=0
    monto3=0
    contador1=0
    #Sueldos menores a $800.000:
    for i in trabajadores:
        if i['sueldos'] <valor1:
            contador1+=1
    print(f'Sueldos menores a $800.000 Total: {contador1}')
    print('Nombre\t\t\tSueldo')
    for i in trabajadores:
        if i['sueldos']<valor1:
            print(f'{i['nombre']}\t\t${i['sueldos']}')
            monto1+=i['sueldos']
    #Sueldos entre $800.000 y $2.000.000:
    contador2=0
    for i in trabajadores:
        if i['sueldos'] > valor1 and i['sueldos']<valor2:
            contador2+=1
    print(f'\nSueldos entre $800.000 y $2.000.0000 Total: {contador2}')
    print('Nombre\t\t\tSueldo')
    print(f'{i['nombre']}\t\t${i['sueldos']}')
    for i in trabajadores:
        if i['sueldos'] > valor1 and i['sueldos']<valor2:
            print(f'{i['nombre']}\t\t${i['sueldos']}')
            monto2+=i['sueldos']
    #Sueldos mayores a $2.000.000:
    contador3=0
    for i in trabajadores:
        if i['sueldos'] > valor2:
            contador3+=1
    print(f'\nSueldos mayores a $2.000.000 Total: {contador3}')
    print('Nombre\t\t\tSueldo')
    print(f'{i['nombre']}\t\t${i['sueldos']}')
    for i in trabajadores:
        if i['sueldos' ] > valor2:
            print(f'{i['nombre']}\t\t${i['sueldos']}')
            monto3+=i['sueldos']
    total=monto1+monto2+monto3
    print(f'\nTotal sueldos:\t\t${total}')

def estadisticas():
    sueldos=[trabajador['sueldos'] for trabajador in trabajadores]
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
    print(f'La media geométrica es: ${media_geometrica}')

def reporte():
    descto_salud=0.7
    descto_afp=0.12
    for i in trabajadores:
        print('Nombre\t\t\Sueldo base\t\t\tDescuento Salud\t\tDescuento afp\t\tSueldo liquido')
        for i in trabajadores:
            sueldo=i['sueldos']
            descuento_en_salud=int(sueldo*descto_salud)
            i['descuentosalud']=descuento_en_salud
            descuento_en_afp=int(sueldo*descto_afp)
            i['descuentoafp']=descuento_en_afp
            sueldo_liquido=int(sueldo-descuento_en_salud-descuento_en_afp)
            i['sueldoliquido']=sueldo_liquido
            print(f'{i['nombre']}\t\t{i['sueldos']}\t\t${i['descuentosalud']}\t\t${i['descuentoafp']}\t\t\t${i['sueldoliquido']}')
        exportar()

def exportar():
    with open('bbdd.csv','w',newline='') as archivo:
        exportar_csv=csv.writer(archivo)
        exportar_csv.writerow(['Nombre empleado','Sueldo base','Descuento salud','Descuento AFP','Sueldo líquido'])
        for i in trabajadores:
            exportar_csv.writerow([i['nombre'],i['sueldos'],i['descuentosalud'],i['descuentoafp'],i['sueldoliquido']])
    print('Archivo generado exitosamente.')

def salir():
    print('Finalizando el programa...\nDesarrolado por Jonathan Saravia\nRut 18.534.141-0')

while True:
    print('\nMenú:')
    print('1) Asignar sueldos')
    print('2) Clasificar sueldos')
    print('3) Ver estadísticas ')
    print('4) Reporte de sueldos ')
    print('5) Salir del programa ')
    try:
        op=int(input('Indica lo que deseas realizar: '))
        if op==1:
            asignar()
        elif op==2:
            clasificar()
        elif op==3:
            estadisticas()
        elif op==4:
            reporte()
        elif op==5:
            salir()
            break
    except ValueError:
        print('Dato incorrecto. Intenta nuevamente.')