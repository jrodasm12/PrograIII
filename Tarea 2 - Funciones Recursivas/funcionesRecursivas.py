"Funcion para convertir decimales a binarios"
def convertir_a_binario(decimal):
    if decimal == 0:
        return ""
    else:
        return convertir_a_binario(decimal//2)+str(decimal%2)

"Funcion para contar digitos"
def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

"Funcion para raiz cuadrada"
def calcular_raiz_cuadrada(numero, candidato, tolerancia=0.01):
    aproximacion = (candidato + numero / candidato) / 2
    if abs(candidato - aproximacion) < tolerancia:
        return int(aproximacion)
    else:
        return calcular_raiz_cuadrada(numero, aproximacion, tolerancia)

def raiz_cuadrada_entera(numero):
    if numero < 0:
        raise ValueError("La raiz cuadrada entera no esta definida para numeros negativos.")
    else:
        return calcular_raiz_cuadrada(numero, 1)

"Funcion para convertir numeros romanos a decimales"
def convertir_a_decimal(numero_romano):
    romano_a_decimal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if numero_romano == "":
        return 0

    if len(numero_romano) == 1 or romano_a_decimal[numero_romano[0]] >= romano_a_decimal[numero_romano[1]]:
        return romano_a_decimal[numero_romano[0]] + convertir_a_decimal(numero_romano[1:])
    else:
        return romano_a_decimal[numero_romano[1]] - romano_a_decimal[numero_romano[0]] + convertir_a_decimal(numero_romano[2:])

"Funcion para suma de numeros enteros"
def suma_numeros_enteros(numero):
    if numero == 0:
        return 0
    else:
        return numero + suma_numeros_enteros(numero - 1)

"Menu interactivo"
while True:
    print("\nMenu Interactivo:")
    print("1. convertir decimales a binarios")
    print("2. contar digitos")
    print("3. raiz cuadrada entera")
    print("4. convertir romano a decimal")
    print("5. suma de numeros enteros")
    print("6. Salir")

    opcion = input("Ingrese el numero de la opcion: ")
    if opcion == '1':
        numero = int(input("Ingrese un numero entero para convertir a binario: "))
        print("Resultado:", convertir_a_binario(numero))
    elif opcion == '2':
        numero = int(input("Ingrese un numero entero para contar los digitos: "))
        print("Resultado:", contar_digitos(numero))
    elif opcion == '3':
        numero = int(input("Ingrese un numero entero para calcular la raiz cuadrada entera: "))
        print("Resultado:", raiz_cuadrada_entera(numero))
    elif opcion == '4':
        numero_romano = input("Ingrese un numero romano para convertir a decimal: ")
        print("Resultado:", convertir_a_decimal(numero_romano))
    elif opcion == '5':
        numero_entero = int(input("Ingrese un numero entero para calcular la suma hasta ese valor: "))
        print("Resultado:", suma_numeros_enteros(numero_entero))
    elif opcion == '6':
        print("Salir")
        break
    else:
        print("Opcion no valida. Solo ingrese un numero del 1 al 6.")