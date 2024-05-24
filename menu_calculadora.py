#crear una calculadora que sume, reste, divida, multiplique y calcule el factorial de un numero


from os import system
from calculos_de_la_calculadora import *


def pausar():
    """Funcion que pause el programa 
    hasta que el usuario presione alguna tecla.
    """
    system("pause")

#menu principal


#funcion de opcion A y opcion B
def pedir_numero():
    """Funcion para pedir los operandos por consola.

    Returns:
        entero: devuelve el numero ingresado. 
    """

    x = input("ingrese un numero: ")
    x = int(x)
    return x


def menu_calculadora(x,y):
    """Funcion que muestra el menu principal de la calculadora.

    Args:
        x (string): Opcion para ingresar el primer operando.
        y (string): Opcion para ingresar el segundo operando.
        z (string): Opcion que nos lleva a otro menu para elegir el calculo.
        r (string): Opcion para mostrar el resultado del calculo hecho entre x e y.
        t (string): Opcion para salir del programa.
    Returns:
        string: devuelve la opcion elegida.
    """

    print(f"A) primer operando {"A = x" if x == None else f"A = {x}"}") 
    print(f"B) segundo operando {"B = y" if y == None else f"B = {y}"}") 
    print("C) elija el calculo a realizar") 
    print("D) mostrar el resultado") 
    print("E) fin del programa")

    elijir_opcion = input("Elija una opción: ")
    print(system("cls"))
    return elijir_opcion



def menu_de_calculos():
    """Funcion que muestra el menu principal de la calculadora.

    Args:
        x (string): Opcion que nos ejecuta la funcion de suma.
        y (string): Opcion que nos ejecuta la funcion de resta.
        z (string): Opcion que nos ejecuta la funcion de multiplicar.
        r (string): Opcion que nos ejecuta la funcion de dividir.
        t (string): Opcion que nos ejecuta la funcion de factorial.
    Returns:
        entero: Devuelve el resulado del calculo.
    """
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) Factorial")

    eleccion = input("Elija el calculo que desea realizar: ")

    if eleccion == "1":
        resultado = sumar(x,y)
    
    elif eleccion == "2":
        resultado = restar(x,y)
    
    elif eleccion == "3":
        resultado = multiplicar(x,y)
    
    elif eleccion == "4":
        resultado = dividir(x,y)
    
    elif eleccion == "5":
        resultado_x = sacar_factorial(x) #es lo unico que no funciona
        resultado_y = sacar_factorial(y) #es lo unico que no funciona

        resultado = f"El factorial de {x} es {resultado_x} y el factorial de {y} es {resultado_y}"

    return resultado


#funcion para mostrar el resultado
def mostrar_resultado(resultado):
    """Funcion para mostrar el resultado del calculo realizado
       en la funcion menu_de_calculos()

    Args:
        entero: printea el resultado 
    """

    print(resultado)


puerta_primer_operando = False
puerta_segundo_operando = False
puerta_opciones_de_calculo = False
desea_seguir = "s"
x = None
y = None

"""Por ultimo entramos al while principal, que hace que las tareas de la calculadora sigan un orden especifico.
Esto se logra mediante el uso de banderas (que yo llamo puertas).
"""

while desea_seguir == "s":
    opcion = menu_calculadora(x,y)
   
    match(opcion):
        case "A":
            x = pedir_numero()
            puerta_primer_operando = True
        case "B":
            if puerta_primer_operando:
                y = pedir_numero()
                puerta_segundo_operando = True          
            else:
                print("Se debe ingresar el primer operando antes que el segundo")
        case "C":
            if puerta_primer_operando == False:
                print("se debe ingresar el primer operando, por favor vuelva a empezar")
            elif puerta_segundo_operando == False:
                print("Se debe ingresar el segundo operando, por favor vuelva a empezar")
            else:
                resultado = menu_de_calculos()
                puerta_opciones_de_calculo = True
        case "D": 
            if puerta_primer_operando == False:
                print("se debe ingresar el primer operando, por favor vuelva a empezar")
            elif puerta_segundo_operando == False:
                print("Se debe ingresar el segundo operando, por favor vuelva a empezar")
            elif puerta_opciones_de_calculo == False:
                print("No se puede realizar ninguna cuenta si no se elije que calculo realizar")
            else:
                mostrar_resultado(resultado)
        case "E":
            desea_seguir = input("presione s para continuar, de lo contrario presione n: ")

            if desea_seguir == "n":
                break
    pausar()








