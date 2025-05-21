def obtener_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("entrada no valida, introduce un numero porfavor")

def obtener_operacion():
    while True:
        operacion = input("ingresar operacion (+, -, *, /): ")
        if operacion in ['+', '-', '*', '/']:
            return operacion
        else:
            print("operacion no valida, porfavor ingrese una de las siguientes: +, -, *, /")

def calcular(num1, num2, operacion):
    try:
        if operacion == '+':
            return num1 + num2
        elif operacion == '-':
            return num1 - num2
        elif operacion == '*':
            return num1 * num2
        elif operacion == '/':
            if num2 == 0:
                raise ValueError("No puedes divir entre cero")
            return num1 / num2
    except ValueError as e:
        print (e)
        return None
    

def main():
    print("hola, esta es una calculadora")
    while True:
        num1 = obtener_numero("Ingresa un numero:  ")
        operacion = obtener_operacion()
        num2 = obtener_numero("Ingresa otro numero:  ")

        resultado = calcular(num1, num2, operacion)
        if resultado is not None:
            print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")

        continuar = input("¿Quieres hacer otra operación? (s/n): ")
        if continuar.lower() != 's':
            print("Gracias por usar la calculadora. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()