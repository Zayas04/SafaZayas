# def apartado_a(texto):
#
#     # a) Devuelve el texto en minusculas
#
#     texto = texto.lower()
#
#     return texto
#
# print(apartado_a("Viva España, Viva Marruecos, Viva Francia, Viva Alemania"))
#
# def apartado_b(texto):
#
#
#    # b) Devuelve las frases el texto, se considera texto ",", "."
#
#    texto = texto.replace(";", ".")
#    texto = texto.split(".")
#
#    return texto
#
#
# print(apartado_b("Viva España. Viva Marruecos. Viva Francia. Viva Alemania"))
#
#
# def apartado_c(texto):
#
#     # c) Devuelve el numero de vocales del texto
#     texto = texto.lower()
#     a = texto.count("a")
#     e = texto.count("e")
#     i = texto.count("i")
#     o = texto.count("o")
#     u = texto.count("u")
#
#     return a + e + i + o + u
#
#
# print(apartado_c("Viva España. Viva Marruecos. Viva Francia. Viva Alemania"))
#
#
# def apartado_d(texto):
#
#
#     # d) El numero de palabas del texto
#
#     texto = texto.replace(".", " ").split(" ")
#     cuenta = len(texto)
#
#     return cuenta
#
# print(apartado_d("Viva España.Viva Marruecos.Viva Francia.Viva Alemania"))
#
# def apartado_e(texto, num_letras):
#
#     # e) Pinta las palabra de mas de 5 letras
#
#     texto = texto.split(" ")
#     for palabra in texto:
#         if len(palabra) >= num_letras:
#             print(palabra)
#
#
#
#
# apartado_e("Viva España Viva Marruecos Viva Francia Viva Alemania", 6)

# def apartado_f(texto):
#
#     # f) Pinta una letras en minuscula y otra en mayuscula y sustituyendo las vocales por x
#
#
#     texto = texto.split(" ")
#     lista = []
#
#     for palabra in texto:
#         if texto.index(palabra) % 2 ==0:   # Index --> me da el indice de la lista (0, 1, 2) segun la posicion
#             minusculas = palabra.lower().replace("a", "x").replace("e", "x"). replace("i", "x").replace("o", "x").replace("u", "x")
#             lista.append(minusculas)
#         else:
#             mayusculas = palabra.upper().replace("A", "X").replace("E", "X"). replace("I", "X").replace("O", "X").replace("U", "X")
#             lista.append(mayusculas)
#
#     return " ".join(lista)  # Join --> Convertir una lista en un texto
#
# print(apartado_f("Viva España Viva Marruecos Viva Francia Viva Alemania"))


def apartado_g(texto):

    # g) Pinta por consola el numero de mayusculas y minisculas que no sean vocales

    lista_upper = []
    lista_lower = []
    for letra in texto:
        if letra.isupper() and letra not in ("a", "e", "i", "o", "u"):     # not in --> lo mismo que != pero sirve para poner mas valores
            lista_upper.append(letra)
        elif letra.islower() and letra not in ("a", "e", "i", "o", "u"):
            lista_lower.append(letra)

    upper = len(lista_upper)
    lower = len(lista_lower)

    print("Letras en mayusculas --> " + str(upper))
    print("Letras en minusculas --> " + str(lower))

apartado_g("Viva España Viva Marruecos Viva Francia Viva Alemania")

