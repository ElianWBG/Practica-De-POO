class ejem4():
    @staticmethod
    def gestionar_notas():
        notas = [85, 42, 90, 61, 78, 95, 33, 70]
        notas.append(88)
        notas.append(45)
        notas.remove(42)
        print(notas.count(70))
        notas.sort(reverse=True)
        print(notas)


    @staticmethod
    def comprarar_listas():
        grupo_a = [10, 20, 30]
        grupo_b = [10, 20, 30]
        grupo_c=grupo_a
        print(grupo_a==grupo_b)#Es true porq comparados tienen los mismos valores
        print(grupo_a is grupo_b)#esta es false porq ocupan diferentes espacio en memoria son dos elementos independientes
        print(grupo_a is grupo_c)#esta es true porq apunta al mismo espacio en memoria 
    
    @staticmethod
    def combinar_grupos():
        matematica = [85, 90, 78]
        ciencias   = [92, 88, 70]
        notas=[]
        notas.extend(matematica)
        notas.extend(ciencias)
        promedio=sum(notas)/len(notas)
        mayores=[i for i in (notas) if i>85]
        print(len(notas))
        print(promedio)
        print(mayores)



ejem4.gestionar_notas()
print("="*40)
ejem4.comprarar_listas()
print("="*40)
ejem4.combinar_grupos()
