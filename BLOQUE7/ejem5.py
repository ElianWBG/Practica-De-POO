class Ejem5:
    @staticmethod
    def calcular_interes(*montos,tasa):
        for indice,tasita in enumerate(montos, 1):
            interes=tasa*tasita
            print(f"{indice}--Cantidad: {tasita} Interes:{interes}")
    
    @staticmethod
    def filtrar_transacciones(*montos):
        grandess=list(filter(lambda x:x>1000,montos))
        con_comi=list(map(lambda x:x*0.02,grandess))
        # grandes=list(map(lambda x:x*0.2,filter(lambda x:x>1000)))
        print(grandess)
        print(con_comi)
    @staticmethod
    def potencia_recursiva(base,exponente):
        if exponente==0:
            return 1
        return base*Ejem5.potencia_recursiva(base,exponente-1)

print(Ejem5.potencia_recursiva(2,8))
Ejem5.filtrar_transacciones(500, 1500, 200, 3000, 800, 2000)
# Grandes: [1500, 3000, 2000]
# Con comisión: [30.0, 60.0, 40.0]
Ejem5.calcular_interes(1000, 2000, 500, tasa=0.05)
# Monto: 1000 → Interés: 50.0
# Monto: 2000 → Interés: 100.0
# Monto: 500  → Interés: 25.0
