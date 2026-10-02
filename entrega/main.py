"""
Integrantes:
Camilo Andres Arias Tenjo
Ronald Samir Molinares Sanabria
"""

from functools import reduce

###############################
## Taller Unidad 2 _ Punto 1 ##
###############################

primeros_pedidos = [
    ["45", "Nacho Lee, Pedro Cardenas", 5, 32.50],
    ["87", "Urbanidad de Carreño, Juan Carreño", 4, 60.20],
    ["72", "Aprenda a jugar dados en dos días, Ana Parra", 4, 22.80],
    ["81", "En Vendedor de Sueños, Benito Hernandez", 4, 15.60],
]

salida = list(
    map(
        lambda x: (x[0], x[2] * x[3] + 15 if x[2] * x[3] < 80 else x[2] * x[3]),
        primeros_pedidos,
    )
)


###############################
## Taller Unidad 2 _ Punto 2 ##
###############################

pedidos = [
    [1, ("45", 3, 12.5), ("27", 15, 20.5), ("74", 10, 38.5)],
    [2, ("45", 10, 12.5), ("74", 11, 38.5)],
    [3, ("45", 2, 12.5), ("27", 1, 20.5)],
    [4, ("31", 6, 14.0), ("30", 9, 27.0), ("100", 15, 40.5)],
    [5, ("31", 5, 14.0), ("30", 12, 27.0), ("27", 4, 20.5)],
]

# factura = list(
#     map(
#         lambda pedido: [
#             pedido[0],
#             (sum(x[1] * x[2] for x in pedido[1:])) + 15
#             if sum(x[1] * x[2] for x in pedido[1:]) < 80
#             else sum(x[1] * x[2] for x in pedido[1:]),
#         ],
#         pedidos,
#     )
# )

valores = list(
    map(
        lambda x: [
            x[0],
            (lambda total: total + 15 if total < 80 else total)(
                reduce(lambda acc, pedido: acc + (pedido[1] * pedido[2]), x[1:], 0)
            ),
        ],
        pedidos,
    )
)


################################################################################
## Cuadernillo Unidad2_Taller_1_Listas por Comprensión y Funciones Especiales ##
################################################################################

numeros = list(range(51))


def numero_primo(lista):
    """
    Ejercicio 1: Generar una lista por comprensión de los números primos y que no sean múltiplos de 5. Esta lista
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
    Ejercicio 2: Cree un diccionario por comprensión a partir de myList, que corresponda a cada elemento de la
    lista y su posición (K,V)
    """
    return {elemento: lista.index(elemento) for elemento in lista}


frase = "Tunja tiene mucha altitud"


def vocales(frase):
    """
    Ejercicio 3: Crear una lista por comprensión, que se conforme de todas las vocales de la frase "TunjA tiene
    mucha altitud"
    """
    return [vocal for vocal in frase if vocal.lower() in "aeiou"]


def vocales_sin_repetir(frase):
    """
    Ejercicio 4: Igual que el ejercicio anterior, pero teniendo en cuenta que la lista resultante no repita las vocales.
    """
    return list(dict.fromkeys(vocales(frase)))


"""
    Ejercicio 5: Usando lambda para ordenar diccionarios. Ordene por edad la siguiente lista de amigos:
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
    Ejercicio 8: Investigar el uso de función LAMBDA con parámetros, parámetros no definidos y DECORATORS
    Ejercicio 9: con parámetros, (Immediately Invoked Function Expression- IIFE) por ejemplo: (lambda x, y: x + y)(param_1, param_2)
    Ejercicio 10: También con múltiples parámetros y decorators, como por ejemplo: wraps(args) wrap(args, **kwargs)
"""


#######################################################
## Cuadernillo Unidad2_Taller_2_Funciones Especiales ##
#######################################################

"""
    Ejercicio 1: A partir la lista de precios “precios”, utilice las funciones lambda y map para aplicarle un aumento
    del 25% a cada uno de los valeres, siempre y cuando no sobrepase los $270.000, en cuyo caso el
    valor queda como el original.
"""

precios = [
    275000,
    125990,
    76400,
    110900,
    68990,
    185900,
    56850,
    352950,
    456990,
    30990,
    69990,
    206350,
]

impuesto = list(map(lambda x: x * 1.25 if x * 1.25 <= 270000 else x, precios))
# imp = [x * 1.25 if x * 1.25 <= 270000 else x for x in precios]


"""
    Ejercicio 2: Respecto a la función filter, generar una Lista a partir del Objeto filter object con nombre
    even_numbers_iterator del taller, reemplazando la función check_even por una función lambda
    equivalente. 
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers_iterator = list(filter(lambda x: bool(x % 2 == 0), numbers))


"""
    Respecto a la función reduce realice el ejercicio número 3, contar_letra, utilizando funciones
    lambda y reduce en una sola línea. 
"""


lista2 = [
    "Mexico",
    "Colombia",
    "Brasil",
    "Venezuela",
    "Bolivia",
    "Argentina",
    "Uruguay",
    "Peru",
    "Paraguay",
    "Chile",
    "a",
    "bdz",
    "aaaaFa",
]
contar_letra = reduce(lambda acc, texto: acc + texto.lower().count("a"), lista2, 0)


"""
A partir de un texto típico de la red X (antiguo twitter), correspondiente a una cadena de 50
palabras, hacer una transformación, en donde se genere una lista de listas en donde cada elemento
sea la palabra original, en mayúsculas, en minúsculas y su longitud.
Ejemplo, a partir del texto: 'Los soleados dias'.
Debe generar la lista: [['LOS', 'los', 3], ['DIAS', 'dias', 4], ['SOLEADOS', 'soleados', 8]].
Teniendo en cuenta que se organizan de menor a mayor por su longitud.
"""
texto = "Los soleados dias"


twitter_lambda = lambda texto: [
    [p.upper(), p.lower(), len(p)] for p in sorted(texto.split(), key=len)
]


"""
    Teniendo dos conjuntos de lecturas de temperaturas de una semana cada una, realizar operaciones
    que generen como resultado las temperaturas comunes de los dos grupos.
    temp1 = [22.4,30,28,22,30,29,20]
    temp2 = [18,20,22.3,19,31,30,17]
    Salida: [20, 30] 
"""
temp1 = [22.4, 30, 28, 22, 30, 29, 20]
temp2 = [18, 20, 22.3, 19, 31, 30, 17]

temperaturas = list(set(filter(lambda t: t in temp2, temp1)))


"""
    Calcular la frecuencia de un elemento en una lista de tuplas.
    Si se tiene listado = [('Pepito', 1, 10), ('Juanito', 2, 45), ('Pepito', 1, 38)] y se quiere verificar la
    frecuencia del elemento 'Pepito', será 2. 
"""
listado = [("Pepito", 1, 10), ("Juanito", 2, 45), ("Pepito", 1, 38)]
elemento = "Pepito"

frecuencias = reduce(
    lambda acc, tupla: acc + (1 if elemento in tupla else 0), listado, 0
)


"""
    A partir de una lista de números, convertirlos a número. Ejemplo lista=[8,5,8,1,2] debe quedar el
    número 85812. 
"""
lista = [8, 5, 8, 1, 2]

number = int("".join(map(str, lista)))


"""
    Integrar en un solo elemento la siguiente información:
    ciudades={'101':'Tunja', '200':'Moniquirá','340':'Puerto Boyacá'}
    coordenadas={'101':(160,45), '200':(168,39),'340':(168,39)}
    rango_temp={'101':'Frio','200':'Templado','340':'Caliente'}
    La salida debe ser:
    101 Tunja (160, 45) Frio
    200 Moniquirá (168, 39) Templado
    340 Puerto Boyacá (168, 39) Caliente 
"""
ciudades = {"101": "Tunja", "200": "Moniquirá", "340": "Puerto Boyacá"}
coordenadas = {"101": (160, 45), "200": (168, 39), "340": (168, 39)}
rango_temp = {"101": "Frio", "200": "Templado", "340": "Caliente"}

data = "\n".join(
    map(
        lambda x: f"{x[0]} {x[1]} {x[2]} {x[3]}",
        zip(
            ciudades.keys(),
            ciudades.values(),
            coordenadas.values(),
            rango_temp.values(),
        ),
    )
)


"""
    Si la información del ejercicio anterior se almacena en una lista de tuplas, plantee la operación
    contraria para desintegrar de nuevo en entidades independientes como se tenía inicialmente. 
"""
lista_tuplas = list(
    zip(
        ciudades.keys(),
        ciudades.values(),
        coordenadas.values(),
        rango_temp.values(),
    )
)

codigos, nombres, coordenadas, temperaturas = zip(*lista_tuplas)
ciudades_real = dict(zip(codigos, nombres))
coordenadas_real = dict(zip(codigos, coordenadas))
rango_temp_real = dict(zip(codigos, temperaturas))


if __name__ == "__main__":
    print("\n================= Primer Ejercicio ================")
    print(salida)

    print("\n================= Segundo Ejercicio ================")
    # print(factura)
    print(valores)

    print("\n================= EJERCICIOS CUADERNILLO 1 ================")
    print(f"Ejercicio 1: {numero_primo(numeros)}")
    print(f"Ejercicio 2: {diccionario_myList(myList)}")
    print(f"Ejercicio 3: {vocales(frase)}")
    print(f"Ejercicio 4: {vocales_sin_repetir(frase)}")
    print(f"Ejercicio 5: {edades}")
    print(f"Ejercicio 7: {numero(17)} y {numero(8)}")

    print("\n================= EJERCICIOS CUADERNILLO 2 ================")
    print(impuesto)
    # print(imp)
    print(even_numbers_iterator)
    print(f"La letra 'a' aparece {contar_letra} veces")
    print(f"Con función lambda: {twitter_lambda(texto)}")
    print(temperaturas)
    print(f"Frecuencia del elemento {elemento} es {frecuencias}")
    print(number)
    print(f"\n{data}")
    print(f"\n{lista_tuplas}\n{ciudades_real}")
    print(coordenadas_real)
    print(rango_temp_real)
