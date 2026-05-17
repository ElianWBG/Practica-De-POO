class ejem2:
    @staticmethod
    def agregacion():
        asd=[]
        asd.append(3)
        asd.append(1)
        asd.append(2)
        asd.sort()
        print(asd)
        
        
    

    @staticmethod
    def listita():
        dsa=[5,2,8,1,9,3]
        x=sum(dsa)
        a=max(dsa)
        e=min(dsa)
        print(x,e,a)
       




    @staticmethod
    def asd():           
        lista = [1, 2, 3]

        copia_ref  = lista
        copia_real = lista.copy()
        copia_ref.append(5)
        print(lista)
        print(copia_real)
        print(copia_ref)
        print(lista is copia_ref)    # ¿True o False? ¿por qué?
        print(lista is copia_real)   # ¿True o False? ¿por qué?
         
# agrega un elemento a copia_ref
# imprime las tres y explica qué pasó 
ejem2.asd()
print("="*40)    
ejem2.listita()
print("="*40)   
ejem2.agregacion()
            
