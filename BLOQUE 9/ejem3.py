class ejem3:
    @staticmethod
    def gestionar_ruta():
        ruta = ("Guayaquil", "Quito", "Cuenca", "Loja", "Manta")

        primera,*media,ultima=("Guayaquil", "Quito", "Cuenca", "Loja", "Manta")
        print(len(ruta))
        print(ruta[0])
        print(ruta[-1])
        print(ruta.count("Quito"))
        print(ruta.index("Cuenca"))
        print(f"Primera:{primera} media:{media} Ultima:{ultima}")

    
    @staticmethod
    def covertir_modificar():
        pasajeros = ("Ana", "Luis", "María", "Carlos")
        new_pasa=list(pasajeros)
        new_pasa.append("Pedro")
        new_pasa.remove("Luis")
        new_pasa.sort()
        new_pasa=tuple(new_pasa)
        print(new_pasa)
    
    @staticmethod
    def recorrer_vuelos():
        vuelos = [("GYE", "UIO", 45),
                ("UIO", "CUE", 60),
                ("CUE", "LOJ", 90)
            ]
        print("====DETALLE DE VUELOS====")
        for x,y,z in vuelos:
            print(f"{x}--{y}|Duracion:{z}")
        

           






ejem3.gestionar_ruta()
print("="*50)
ejem3.covertir_modificar()
print("="*50)
ejem3.recorrer_vuelos()
