import random
import os
import numpy as np
opcion=""

matriz = [] # matriz principal

listaDeOpcionesValidas = ["0","1","2","3","4","5"] #opciones del menú principal

contratos = []  #matriz para guardar los autos vendidos



#Primera opcion
def guardar_auto(matriz):
    patente = input("Ingrese la patente (6 caracteres): ")
    marca = input("Ingrese la marca (3 caracteres): ")
    modelo = input("Ingrese el modelo (3 caracteres): ")
    ano = int(input("Ingrese el año (sobre 2000): "))
    valor = int(input("Ingrese el valor (mínimo $500.000):$ "))

    if len(patente) == 6 and len(marca) == 3 and len(modelo) == 3 and ano > 2000 and valor >= 500000:
        matriz.append([patente, marca, modelo, ano, valor])
        input("Vehículo guardado exitosamente.")
        input("Enter para continuar")
    else:
        print("Error al guardar el vehículo. Revise los datos ingresados.")
        input("Presione Enter para volver a intentarlo")

#Segunda opción, buscar
def buscar_vehiculo(matriz):
    patente = input("Ingrese la patente del vehículo que desea buscar: ")
    encontrado = False

    for vehiculo in matriz:
        if vehiculo[0] == patente:
            estado = "Vendido" if vehiculo in contratos else "Disponible"
            encontrado = True
            ano_actual = 2023
            ano_fabricacion = ano_actual - vehiculo[3]
            print("*******************************")
            print("Información del vehículo:")
            print("Patente:", vehiculo[0])
            print("Marca:", vehiculo[1])
            print("Modelo:", vehiculo[2])
            print("Año del vehículo:", vehiculo[3])
            print("Valor:$", vehiculo[4])
            print("Años de antiguedad:", ano_fabricacion, "años")
            print("Estado:", estado)
            print("*******************************")
            input("presione enter para continuar")
    if not encontrado:
        print("Vehículo no encontrado.")
        input("presione enter para continuar")
        
#Tercera opción, mostrar
def listar_vehiculos(matriz):
    print("*******************************")
    print("Listado de vehículos:")
    if len(matriz) == 0:
        print("No hay vehiculos ingresados en el sistema.")
        print("*******************************")
        input("presione enter para continuar")
        return
    
    for vehiculo in matriz:
        estado = "Vendido" if vehiculo in contratos else "Disponible"
        print("Patente:", vehiculo[0])
        print("Marca:", vehiculo[1])
        print("Modelo:", vehiculo[2])
        print("Año del vehículo:", vehiculo[3])
        print("Valor: $", vehiculo[4])
        print("Estado:", estado)
        print("*******************************")

        print()
        input("presione enter para mostrar siguiente vehiculo o salir")
        print()

#Cuarta opción, contrato
def imprimir_contrato(matriz):
    patente = input("Ingrese la patente del vehículo a vender: ")
    encontrado = False

    for vehiculo in matriz:
        if vehiculo[0] == patente:
            encontrado = True
            if vehiculo not in contratos:
                contrato_numero = random.randint(1000, 50000)
                contratos.append(vehiculo)
                print("*******************************")
                print("***Contrato de Compraventa***")
                print("Número de Contrato:", contrato_numero)
                print("Datos del vehículo:")
                print("Patente:", vehiculo[0])
                print("Marca:", vehiculo[1])
                print("Modelo:", vehiculo[2])
                print("Año del vehículo:", vehiculo[3])
                print("Valor:$", vehiculo[4])
                print("*******************************")
                input("presione enter para continuar")
            else:
                print("El vehículo ya ha sido vendido.")
                input("presione enter para continuar")


    if not encontrado:
        print("Vehículo no encontrado.")
        input("presione enter para continuar")

#Menú principal
while opcion != "5":
    os.system("cls")
    print("----- Automotora -----")
    print("1. Guardar vehículo")
    print("2. Buscar vehículo")
    print("3. Listar vehículos")
    print("4. Imprimir contrato")
    print("5. Salir")

    opcion = (input("Seleccione una opción: "))

    if opcion not in listaDeOpcionesValidas:
        print("La opción ingresada no es válida")
        input("Presione enter para continuar...")
    elif opcion == "1":
        guardar_auto(matriz)
    elif opcion=="2":
        buscar_vehiculo(matriz)
    elif opcion== "3":
        listar_vehiculos(matriz)
    elif opcion=="4":
        imprimir_contrato(matriz)

    