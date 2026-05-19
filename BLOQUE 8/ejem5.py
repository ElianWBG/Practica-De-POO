class ejem5:
    @staticmethod
    def gestion():
        productos = ["arroz", "leche", "pan", "huevos", "aceite"]
        productos.insert(2,"azucar")
        a=productos.pop()
        print(a)
        print(productos.index("pan"))
        print(len(productos))
        print(productos)
    
    @staticmethod
    def prcios_ord():
        precios = [5.50, 2.30, 8.90, 1.20, 6.75, 3.40]
        copia=precios.copy()
        precio=precios
        precio.append(9.48)#lo agrege para ver y probrar si se modifica bien 
        precios.sort()
        rango=max(precio)-min(precio)
        print(precios)
        print(copia)
        print(max(precios))
        print(min(precios))
        print(f"Rango:{rango}")
    
    @staticmethod
    def resumen():
        lunes    = [150, 200, 80, 320]
        martes   = [90, 175, 410, 60]
        miercoles= [200, 150, 300, 175]
        ventas_semanal=[]
        ventas_semanal.extend(lunes)
        ventas_semanal.extend(martes)
        ventas_semanal.extend(miercoles)
        print(sum(ventas_semanal))
        print(min(ventas_semanal))
        print(max(ventas_semanal))
        top=[x for x in(ventas_semanal)if x>200]
        print(top)
        promedio=sum(ventas_semanal)/len(ventas_semanal)
        pro=round(promedio,2)
        print(pro)
print("="*40)
ejem5.resumen()
print("="*40)
ejem5.prcios_ord()
print("="*40)
ejem5.gestion()
print("="*40)