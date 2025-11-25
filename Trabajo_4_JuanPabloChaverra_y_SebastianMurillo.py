#trabajo modificado
#sebastian Murillo Gonzales 
#juan Pablo Chaverra Hoyos
import math
# funcion para sumar los numeros
def sumahastanumero(n):
    suma = 0
    for i in range(1, n + 1):
        suma += i
    return suma

# funcion para calcular el factorial
def calcularfactorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# PRIMERA PARTE
def opcion1():
    print("---- PRIMERA PARTE ----")

    # ciclo while
    Numerosingresados = []
    while len(Numerosingresados) < 2: 
            num = float(input("Ingrese un numero, 'No puedes ingresar letras': "))
            Numerosingresados.append(num)
    
    seno = math.sin(Numerosingresados[1])
    tangente = math.tan(Numerosingresados[0])
    if Numerosingresados[1] != 0:
        residuo = Numerosingresados[0] % Numerosingresados[1]
    else:
        residuo = "No se puede dividir por cero."
    
    print("\n RESULTADOS")
    print("Numeros ingresados:", Numerosingresados)
    print(f"Seno del segundo numero ({Numerosingresados[1]}): {seno}")
    print(f"Tangente del primer numero ({Numerosingresados[0]}): {tangente}")
    print(f"Residuo entre el primero y el segundo: {residuo}")  
    multiplos_3 = [n for n in Numerosingresados if n % 3 == 0]
    if multiplos_3:
        print("Numeros multiplos de 3:", multiplos_3)
    else:
        print("No hay multiplos de 3 entre los numeros ingresados.")

#MENU SEGUNDA PARTE
def opcion2():
    while True:
        print("\n--------- SEGUNDA PARTE  --------")
        print("* 1. Contar letras de un texto  *")
        print("* 2. Factorial de un numero     *")
        print("* 3. Sumar numeros hasta N      *")
        print("* 4. Volver al menu principal   *")
        print("*********************************")

        opcion = input("Seleccione una opcion: ")

        # letras contador
        if opcion == "1":
            texto = input("Ingrese un texto: ")
            print(f"El texto tiene {len(texto)} caracteres.")

        # factorial
        elif opcion == "2":
            print("=== CALCULO DE FACTORIAL ===")
            numero = int(input("Ingrese un numero entero positivo: ")) 
            if numero < 0:
                print("El factorial no esta definido para numeros negativos.")
            else:
                resultado = calcularfactorial(numero)
                print(f"El factorial de {numero} es: {resultado}")

        # suma de los numeros 
        elif opcion == "3":
            print("=== SUMA HASTA UN NUMERO ===")
            numero = int(input("Ingrese un numero entero positivo: "))
            if numero > 0:
                resultado = sumahastanumero(numero)
                print(f"La suma de los numeros desde 1 hasta {numero} es: {resultado}")
            else:
                print("Por favor ingrese un numero mayor que 0.")

        elif opcion == "4":
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

# MENU PRINCIPAL
while True:
    print("\n--------- MENU PRINCIPAL --------")
    print("* 1. Primer Parte del trabajo   *")
    print("* 2. Segunda Parte del trabajo  *")
    print("* 3. Terminar programa          *")
    print("*********************************")

    opcion = input("Seleccione una opcion: ")
    if opcion == "1":
        opcion1()
    elif opcion == "2":
       opcion2()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opcion no valida. Intente de nuevo.")
