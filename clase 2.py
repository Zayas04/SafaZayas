def apartado_a(num_1, num_2, num_3):

    # a) Metodo que recibe tres numeros y pinta por consola el mas grande
    if num_1 > num_2 and num_1 > num_3:
        print("El numero 1 es el mas grande")
    elif num_2 > num_3:
        print("El numero 2 es el mas grande")
    else:
        print("El numero 3 es el mas grande")

apartado_a(5, 8, 13)

def apartado_b(texto):

    # b) Metodo que recibe una cadena de texto y la pinta si no es " " y si tiene menos de 8 letras

    if texto != " " and len(texto) < 8:
        print(texto)

apartado_b("adsd")


def apartado_c(palabra_1, palabra_2, palabra_3, palabra_4):

    # c) Metodo que recibe cuatro palabras y pinta las palabras mas pequeñas y la mas grande

    if len(palabra_1) > len(palabra_2) and len(palabra_1) > len(palabra_3) and len(palabra_1) > len(palabra_4):
        print("Esta palabra es la mas grande -->", palabra_1)
    elif len(palabra_2) > len(palabra_3) and len(palabra_2) > len(palabra_4):
        print("Esta palabra es la mas grande -->", palabra_2)
    elif len(palabra_3) > len(palabra_4):
        print("Esta palabra es la mas grande -->", palabra_3)
    else:
        print("Esta palabra es la mas grande -->", palabra_4)
    if len(palabra_1) < len(palabra_2) and len(palabra_1) < len(palabra_3) and len(palabra_1) < len(palabra_4):
        print("Esta palabra es la mas pequeña -->", palabra_1)
    elif len(palabra_2) < len(palabra_3) and len(palabra_2) < len(palabra_4):
        print("Esta palabra es la mas pequeña -->", palabra_2)
    elif len(palabra_3) < len(palabra_4):
        print("Esta palabra es la mas pequeña -->", palabra_3)
    else:
        print("Esta palabra es la mas pequeña -->", palabra_4)
apartado_c("manolo", "ola", "maricarmen", "pepe")


def apartado_d(num1, num2, num3, num4, divisor):

    # d) Metodo que recibe 5 numeros y pinta todos los que se pueden dividir por el ultimo

    if num1 % divisor == 0:
        print(num1)
    if num2 % divisor == 0:
        print(num2)
    if num3 % divisor == 0:
        print(num3)
    if num4 % divisor == 0:
        print(num4)

apartado_d(7,4,8,16,4)


def apartado_e(palabra1, palabra2, palabra3):

    # e) Metodo que recibe 3 palabras y pinta todas las palabras que contengan al menos 3 vocales

    vocales_palabra1 = palabra1.count("a") + palabra1.count("e") + palabra1.count("i") + palabra1.count("o") + palabra1.count("u")
    vocales_palabra2 = palabra2.count("a") + palabra2.count("e") + palabra2.count("i") + palabra2.count("o") + palabra2.count("u")
    vocales_palabra3 = palabra3.count("a") + palabra3.count("e") + palabra3.count("i") + palabra3.count("o") + palabra2.count("u")

    if vocales_palabra1 >= 3:
        print(palabra1)
    if vocales_palabra2 >= 3:
        print(palabra2)
    if vocales_palabra3 >= 3:
        print(palabra3)



apartado_e("olaa", "ola", "oloo")


def apartado_6(palabra):

    # 6) Realiza un método que reciba una palabra y pinte por consola.
    vocalaes_palabra = palabra.count("a") + palabra.count("e") + palabra.count("i") + palabra.count("o") + palabra.count("u")
    tildes_palabra = palabra.count("á") + palabra.count("é") + palabra.count("í") + palabra.count("ó") + palabra.count("ú")
    if palabra != " ":
        print("Es distinta de " " ")
    else:
        print("La palabra es " " ")
    if len(palabra) < 5:
        print("La palabra no tiene mas de 5 letras")
    else:
        print("La palabra tiene mas de 5 letras")
    if vocalaes_palabra > 1:
        print("La palabra tiene vocales")
    else:
        print("La palabra no tiene vocales")
    if len(palabra) > vocalaes_palabra:
        print("La palabra tiene consonantes")
    else:
        print("La palabra no tiene consonante")
    if tildes_palabra > 1:
        print("La palabra tiene tilde")
    else:
        print("Las palabras no tiene tilde")
    print(len(palabra))


apartado_6("asdadadááá")