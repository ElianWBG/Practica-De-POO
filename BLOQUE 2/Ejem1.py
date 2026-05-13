def presentar_variables():
    entero:int=40
    decimal:float=19.5
    texto:str="hola"
    booleano:bool=True
    nulo=None
    print(f"Entero: {entero}")
    print(f"Decimal: {decimal}")
    print(f"Texto: {texto}")
    print(f"Booleano: {booleano}")
    print(f"Nulo: {nulo}")
    
    
lista: list=[1,2,3,"Elian"]
tupla:tuple=(1,"Hola",3.14)
diccionario:dict={"nombre": "Belfor","edad":25}
conjunto:set={1,2,5}
def presentar_tipos():
    lista: list=[1,2,3,"Elian"]
    tupla:tuple=(1,"Hola",3.14)
    diccionario:dict={"nombre": "Belfor","edad":25}
    conjunto:set={1,2,5}   
    print(f"Lista: {lista}")
    print(f"tupla: {tupla}")
    print(f"diccionario: {diccionario}")
    print(f"Conjunto: {conjunto}")

class EjercicioTipos:
    def mostrar_datos(self):
        texto="Python"
        lista=[10,20,30,40]
        diccionario= {"nombre": "elian", "edad":20}
        print(texto[0])
        print(lista[3])
        print(diccionario["nombre"])
lista=[10,20,30,40,50]



presentar_variables()
print("="*40)
presentar_tipos()
print("="*40)
print(lista[0])
print(lista[-1])
print(lista[1:4])
print("="*40)
obj = EjercicioTipos()
obj.mostrar_datos()

