#funciones de los calculos 
def sumar(a,b):
    resultado = a + b
    return resultado



def restar(a,b):
    resta = a - b
    return resta



def multiplicar(a,b):
    producto = a * b
    return producto



def dividir(a,b):
    division = a / b

    if b != 0:
        return division
    else:
        return "Error: division por 0"



def sacar_factorial(x) -> int:
    
    factorial = 1

    for i in range(x):
       factorial = factorial * i + 1

    return x




