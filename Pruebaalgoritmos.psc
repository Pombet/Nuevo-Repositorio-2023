Algoritmo sin_titulo
	Definir totale, totali, total Como Entero
	Definir nombre Como Caracter
	Definir option Como Entero
	Definir interior, exterior Como Entero
	Definir suma Como Entero
	Definir cantidadi, cantidade Como Entero
	Definir porcentaje Como Entero
	Definir totalcant Como Entero
	Definir contador Como Entero
	
	exterior= 5000
	interior= 8000
	suma= exterior+interior
	
	Escribir "************************"
	Escribir "----Lavado de autos----"
	Escribir "************************"
	
	Mientras option <> 6 Hacer
	
		Escribir "[1] Nombre del cliente"
		Escribir "[2] Lavado interior"
		Escribir "[3] Lavado exterior"
		Escribir "[4] boleta del cliente"
		Escribir "[5] Ver total de ventas"
		Escribir "[6] Salir"
		Leer option 
		Si option = 1 Entonces
			Escribir "Ingrese su nombre"
			Leer nombre
			escribir "Nombre del cliente ",nombre 
		FinSi
		
		Si option = 2 Entonces
			Escribir "cantidad de autos: "
			Leer cantidadi
			totali=cantidadi*interior
			Mostrar totali
			Escribir "Presione enter para continuar"
			Esperar Tecla
		FinSi
		
		si option = 3 Entonces
			Escribir "cantidad de autos: "
			Leer cantidade
			totale=cantidade*exterior
			Mostrar totale
			Escribir "Presione enter para continuar"
			
			Esperar Tecla
		FinSi
		
		si option = 4 Entonces
			Escribir "*******************************************************"
			Escribir "Gracias ", nombre, " por preferir nuestros servicios."
			total=totale+totali
			Escribir "Lavado Exterior :" totale
			Escribir "Lavado Interior :" totali
			Escribir "Monto a pagar :" total
			Escribir "Ingrese un porcentaje de descuento, entre 10% y 30%"
			Leer porcentaje
			si porcentaje >= 10 y porcentaje <= 30 Entonces
				total = total - (porcentaje * total / 100)
				Escribir "Gracias ", nombre, " por preferir nuestros servicios."
				Escribir "Lavado Exterior :" totale
				Escribir "Lavado Interior :" totali
				Escribir "Monto final con descuento a pagar: $" total
				Escribir "Presione enter para continuar"
				Escribir "-----------------------------------------"
				contador= contador + 1 
			SiNo
				Escribir "Descuento invalido, monto a pagar $", total
				Escribir "-----------------------------------------"
				contador= contador + 1
			FinSi
			Esperar Tecla
		
		
			
			total=0
			porcentaje=0
			totali=0
			totale=0
		FinSi
		
		Si option = 5 Entonces
			Escribir "El total de boletas: ", contador
		FinSi
	
		
	FinMientras
FinAlgoritmo
