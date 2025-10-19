# debug_test.py
# Ejemplo para probar Run y Debug en VSC

def saludar(nombre):
    print(f"Hola, {nombre}!")

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: No es posible dividir por cero")
        return None

if __name__ == "__main__":
    nombre = "Roberto"
    saludar(nombre)
    try:
        resultado = dividir(10, 5)
        if resultado is not None:
            print("Resultado:", resultado)
    except Exception as e:
        print(f"Ocurrió un error inesperado, revisar: {str(e)}")
        
