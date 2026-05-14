def clasificar_personas():
    nombre=str(input("Ingrese Nombre "))
    edad=int(input("Ingrese edad "))
    salario=int(input("Ingrese salario "))
    
    if edad <=18:
        print("Menor de edad")
    elif edad<25:
        print("Joven")
    elif edad<64:
        print("Aduelto")
    else:
        print("Adulto Mayor")
    
    if salario<500:
        print("Salario Bajo")
    elif salario<1499:
        print("Salario medio")
    else:
        print("Salario Alto")
    
    
    estado = "Persona Independiente" if edad > 18 and salario > 1000 else "Necesito ayuda"
        

    print("=======Perfil======")
    print(f"Nombre:{nombre}")
    print(f"Edad:{edad}")
    print(f"Salario: {salario}")
    print(f"Estado: {estado}")
    print("="*20)
clasificar_personas()




    