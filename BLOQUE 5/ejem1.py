# if condicion:
#     # se ejecuta si es True
# elif otra_condicion:
#     # se ejecuta si la anterior era False y esta es True
# else:
#     # se ejecuta si ninguna fue True
# # par o impar
# numero = 15
# if numero % 2 == 0:
#     print("Par")
# else:
#     print("Impar")

# # calificación
# nota = 85
# if nota >= 90:   print("A")
# elif nota >= 80: print("B")
# elif nota >= 70: print("C")
# else:            print("D")
# # forma normal
# if edad >= 18:
#     mensaje = "Mayor de edad"
# else:
#     mensaje = "Menor de edad"

# # forma ternaria — exactamente igual pero en una línea
# mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
# print(mensaje)
# dia = "lunes"
# match dia:
#     case "lunes":   print("Inicio de semana")
#     case "viernes": print("Fin laboral")
#     case "sabado" | "domingo": print("Fin de semana")  # varios casos juntos
#     case _:         print("Otro día")  # _ es el caso por defecto