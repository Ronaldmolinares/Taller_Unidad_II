numeros = list(range(51))


def numero_primo(lista):
    """
    Generar una lista por comprensión de los números primos y que no sean múltiplos de 5. Esta lista
    debe ser entre 0 y el 50.
    """

    return [
        numero
        for numero in lista
        if numero > 1
        and all(numero % i != 0 for i in range(2, numero))
        and numero % 5 != 0
    ]


myList = ["a", "as", "bat", "car", "dove", "python"]


def diccionario_myList(lista):
    """
    Cree un diccionario por comprensión a partir de myList, que corresponda a cada elemento de la
    lista y su posición (K,V)
    """
    return {elemento: lista.index(elemento) for elemento in lista}


frase = "Tunja tiene mucha altitud"


def vocales(frase):
    """
    Crear una lista por comprensión, que se conforme de todas las vocales de la frase "TunjA tiene
    mucha altitud"
    """
    return [vocal for vocal in frase if vocal.lower() in "aeiou"]


def vocales_sin_repetir(frase):
    """
    Igual que el ejercicio anterior, pero teniendo en cuenta que la lista resultante no repita las vocales.
    """
    return list(dict.fromkeys(vocales(frase)))


"""
    Usando lambda para ordenar diccionarios. Ordene por edad la siguiente lista de amigos:
    Se puede utilizar la función sort en diccionarios donde (key=lambda..)
"""
my_friends = [
    {"name": "Pepito", "age": 35},
    {"name": "Juanito", "age": 20},
    {"name": "Julito", "age": 45},
    {"name": "Jaimito", "age": 22},
]
edades = sorted(my_friends, key=lambda x: x["age"])


"""
    Ejercicio 6: Investigar el uso de listas de funciones
"""


"""
    Ejercicio 7: Determinar si un número es par o impar utilizando una función lambda 
"""
numero = lambda x: f"El número {x} es PAR" if x % 2 == 0 else f"El número {x} es IMPAR"


"""
    Ej 8: Investigar el uso de función LAMBDA con parámetros, parámetros no definidos y DECORATORS
    Ej 9: con parámetros, (Immediately Invoked Function Expression- IIFE) por ejemplo: (lambda x, y: x + y)(param_1, param_2)
    Ej 10: También con múltiples parámetros y decorators, como por ejemplo: wraps(args) wrap(args, **kwargs)
"""

if __name__ == "__main__":
    print(numero_primo(numeros))
    print(diccionario_myList(myList))
    print(vocales(frase))
    print(vocales_sin_repetir(frase))
    print(edades)
    print(numero(234))
    print(numero(23))
