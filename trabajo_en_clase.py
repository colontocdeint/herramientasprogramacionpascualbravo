import math

def opcion1():
    # 5.1.1 - Trabajar con ciclo while
    numeros = []

    while len(numeros) < 2:  # 5.1.3 - Debe haber mínimo 2 números
        try:
            num = float(input("Ingrese un número: "))
            numeros.append(num)
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")
    
    # 5.1.4 - 
    sen_segundo = math.sin(numeros[1])

    # 5.1.5 - Tangente del primer número
    tan_primero = math.tan(numeros[0])

    # 5.1.6 - Residuo entre el primero y el segundo número
    if numeros[1] != 0:
        residuo = numeros[0] % numeros[1]
    else:
        residuo = "No se puede dividir por cero."

    # 5.1.7 - Mostrar todos los números
    print("\n--- RESULTADOS OPCIÓN 1 ---")
    print("Números ingresados:", numeros)
    print(f"Seno del segundo número ({numeros[1]}): {sen_segundo}")
    print(f"Tangente del primer número ({numeros[0]}): {tan_primero}")
    print(f"Residuo entre el primero y el segundo: {residuo}")

    # 5.1.8 - Mostrar cuáles son múltiplos de 3
    multiplos_3 = [n for n in numeros if n % 3 == 0]
    if multiplos_3:
        print("Números múltiplos de 3:", multiplos_3)
    else:
        print("No hay múltiplos de 3 entre los números ingresados.")


def opcion2():
    # Menú secundario para el 40% de la nota
    while True:
        print("\n--- MENÚ OPCIÓN 2 ---")
        print("1. Contar caracteres de un texto")
        print("2. Calcular factorial de un número")
        print("3. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # 5.2.1 - Contar caracteres
            texto = input("Ingrese un texto: ")
            print(f"El texto tiene {len(texto)} caracteres.")

        elif opcion == "2":
            # 5.2.2 - Calcular factorial
            try:
                n = int(input("Ingrese un número entero para calcular su factorial: "))
                if n < 0:
                    print("El factorial no está definido para números negativos.")
                else:
                    factorial = 1
                    for i in range(1, n + 1):
                        factorial *= i
                    print(f"El factorial de {n} es: {factorial}")
            except ValueError:
                print("Debe ingresar un número entero válido.")

        elif opcion == "3":
            break
        else:
            print("Opción no válida, intente nuevamente.")


# Programa principal
while True:
    print("\n======= MENÚ PRINCIPAL =======")
    print("1. Opción 1 (60%)")
    print("2. Opción 2 (40%)")
    print("3. Salir")

    seleccion = input("Seleccione una opción: ")

    if seleccion == "1":
        opcion1()
    elif seleccion == "2":
        opcion2()
    elif seleccion == "3":
        print("¡Programa finalizado!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
