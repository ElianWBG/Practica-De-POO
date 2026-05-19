class ejem2:
    @staticmethod
    def Capturar_entero():
        try:
            num=int(input("Ingrese un numero"))
        except ValueError as e:
            print("dato no valido")
    
    @staticmethod
    def captura_index():
        lista=[1,3,4]
        try:
            lista[5]
        except IndexError as e:
            print("NO SE PUEDE MODIFICAR")

    @staticmethod
    def majedo_boble():

        try:
            resultado = 10 / 0
        except ZeroDivisionError:
            print("No se puede dividir por cero")
        except ValueError:
            print("Tipo de dato incorrecto")
      
        

ejem2.Capturar_entero()
ejem2.majedo_boble()
ejem2.Capturar_entero()