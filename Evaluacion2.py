import os
opcion=""
VentasTotal=0

Cestrellam=500
CantCest=0
TotalCes=0
totalCesDes=0

Champ=4000
CantChamp=0
TotalChamp=0
totalChampDes=0

Meganium=2500
CantMeg=0
TotalMeg=0
totalMegDes=0

Donkie=2000
CantDon=0
TotalDon=0
totalDonkDes=0

while opcion!="5":
    os.system ("cls")
    print("Heladeria Fan's Levis Live:")
    print("1.-Cestrellan")
    print("2.-Champs")
    print("3.-Meganium")
    print("4.-Donkie")
    print("5.-Salir")
    opcion=input("Seleccione una opción: ")

    if opcion not in ("1", "2", "3", "4", "5"):
        print("Opción no es válida")
    #Cestrellam
    elif opcion=="1":
        Cantidad=int(input("El valor del Cestrellam es de $500, ingrese cantidad: "))
        edad=int(input("Si es mayor de edad o de la tercera edad puede tener un descuento del 10%, ingrese su edad: "))
        if edad<18 or edad >= 60:
            descuento=500*90/100
            totalCesDes=Cantidad*descuento
            print("Descuento realizado con exito, el monto a pagar es de: $", totalCesDes )
            totalCesDes += 0
            CantCest += Cantidad
        else:
             TotalCes=Cantidad*Cestrellam
             print("Descuento no realizado, el valor a pagar seria de: $", TotalCes)
             TotalCes += 0
             CantCest += Cantidad        
    #Champs    
    elif opcion=="2":
        Cantidad=int(input("El valor del Champs es de $4.000, ingrese cantidad: "))
        edad=int(input("Si es mayor de edad o de la tercera edad puede tener un descuento del 10%, ingrese su edad: "))
        if edad<18 or edad >= 60:
            descuento=4000*90/100
            totalChampDes=Cantidad*descuento
            print("Descuento realizado con exito, el monto a pagar es de: $", totalChampDes )
            totalChampDes += 0
            CantChamp += Cantidad
        else:
             TotalChamp=Cantidad*Champ
             print("Descuento no realizado, el valor a pagar seria de: $", TotalChamp)
             TotalChamp += 0
             CantChamp += Cantidad 
    #Meganium    
    elif opcion=="3":
        Cantidad=int(input("El valor del Meganium es de $2.500, ingrese cantidad: "))
        edad=int(input("Si es mayor de edad o de la tercera edad puede tener un descuento del 10%, ingrese su edad: "))
        if edad<18 or edad >= 60:
            descuento=descuento=2500*90/100
            totalMegDes=Cantidad*descuento
            print("Descuento realizado con exito, el monto a pagar es de: $", totalMegDes )
            totalMegDes += 0
            CantMeg += Cantidad
        else:
             TotalMeg=Cantidad*Meganium
             print("Descuento no realizado, el valor a pagar seria de: $", TotalMeg)
             TotalMeg += 0
             CantMeg += Cantidad 
    #Donkie
    elif opcion=="4":
        Cantidad=int(input("El valor del Meganium es de $2.000, ingrese cantidad: "))
        edad=int(input("Si es mayor de edad o de la tercera edad puede tener un descuento del 10%, ingrese su edad: "))
        if edad<18 or edad >= 60:
            descuento=descuento=2000*90/100
            totalDonkDes=Cantidad*descuento
            print("Descuento realizado con exito, el monto a pagar es de: $", totalDonkDes)
            totalDonkDes += 0
            CantDon += Cantidad
        else:
             TotalDon=Cantidad*Donkie
             print("Descuento no realizado, el valor a pagar seria de: $", TotalDon)
             TotalDon += 0
             CantDon += Cantidad 

    #Total
    elif opcion=="5":
        VentasTotal=TotalCes+TotalChamp+TotalMeg+TotalDon+totalCesDes+totalChampDes+totalMegDes+totalDonkDes
        print("*******************************")
        print("Heladeria Fan's Levis Live:")
        print("Reporte de productos vendidos")
        print("Cestrellan     : ", CantCest )
        print("Champ          : ", CantChamp )
        print("Meganium       : ", CantMeg )
        print("Donkie         : ", CantDon )
        print("total de ventas: $", VentasTotal )
        print("*******************************")

    input("Presione enter para continuar")

