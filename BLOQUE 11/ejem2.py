class Ejem2:
    @staticmethod
    def presentar1():
        
        A={1,2,3,4,5}
        B={4,5,6,7}
        print("===CONJUNTOS")
        print(f"UNION{A|B}")
        print(f"Diferencia{A-B}")
        print(f"Intersepcion{A&B}")
    @staticmethod
    def eliminar_dupli():
        conjunto={1,2,2,3,3,3,4}
        sin_copia=list(set(conjunto))
        print("=== USAR SET====")
        print(sin_copia)
    @staticmethod
    def calculo():
        A={1,2,3,4,6}
        B={6,7,8,9,10}
        asd=A|B
        dsa=A&B
        sad=(A|B)-(A&B)
        print("==EXPLICACION DE | y & en conjuntos==")
        print(f"{asd} Une todos los elementos ")
        print(f"{dsa} Muestra la interseccion de los conjuntos ")
        print(f"{sad} muestras todo menos los que se comparten")
        
        
        

print("="*40)
Ejem2.presentar1()
print("="*40)
Ejem2.eliminar_dupli()
print("="*40)
Ejem2.calculo()




