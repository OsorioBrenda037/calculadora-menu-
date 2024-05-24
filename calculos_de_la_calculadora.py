#funciones de los calculos 
def sumar(a,b):
    """Funcion para sumar dos valores.

    Args:
        a (entero): primer operando.
        b (entero): segundo operando.

    Returns:
        entero: resultado de la suma.
    """
    resultado = a + b
    return resultado



def restar(a,b):
    """Funcion para restar dos numeros.

    Args:
        a (entero): primer operando.
        b (entero): segundo operando.

    Returns:
        entero: resultado de la resta.
    """
    resta = a - b
    return resta



def multiplicar(a,b):
    """Funcion para multiplicar un numero por otro.

    Args:
        a (entero): numero distinto de 0.
        b (entero): numero distinto de 0.

    Returns:
        entero: resultado de la multiplicacion.
    """
    producto = a * b
    return producto



def dividir(a,b):
    """Funcion para divdir un numero por otro.

    Args:
        a (entero): numero distinto de cero.
        b (entero): numero distinto de cero.

    Returns:
        entero: resultado de la division.
    """
    division = a / b

    if b != 0:
        return division
    else:
        return "Error: division por 0"



def sacar_factorial(x) -> int:
    """Funcion para calcular el factorial de un numero.

    Args:
        x (entero): numero distinto de cero y positivo.

    Returns:
        entero: Retorna el factorial del numero ingresado.
    """

    factorial = 1

    for i in range(x):
       factorial = factorial * i + 1
       print(factorial)
    
    print(factorial)
    return factorial



#     factorial = 1
#     for numero in range(x):
#         factorial *= numero+1

#     return factorial