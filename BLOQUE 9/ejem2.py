class ejem2:
    @staticmethod
    def ejer1():
        #crear tupla con 4 elementos
        tupla:tuple=(10,30,20,50,100)
        a, b, *resto = (100, 200, 300, 400)
        # a=100, b=200, resto=[300, 400]
        print(tupla) 
        # tupla[0]=40 #me sale que este objeto no soporta el item asignado
        print(a) 
        print(b)
        print(*resto)


    
    @staticmethod
    def upita():
        coordenadas = [(1, 2), (3, 4), (5, 6), (7, 8)]
        for x,y in coordenadas:
            print(x,y)



print("="*40)
ejem2.ejer1()
print("="*40)
ejem2.upita()
