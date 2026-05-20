class ejem2:
    @staticmethod
    def desep():
        primera,*mitad,ultima=(10,20,30,40)
        print(f"Primera:{primera}")
        print(f"Mitad: {mitad}" )
        print(f"Ultima:{ultima}")
    
   
    
    @staticmethod
    def dic():
        dict1 = {"nombre": "Elian", "edad": 22}
        dict2 = {"ciudad": "Guayaquil", "carrera": "Sistemas"}
        superdict={**dict1,**dict2}
        print(superdict)
    
    @staticmethod
    def mutiplicar(a,b,c):
        return a*b*c
lista=[2,3,4]
print(ejem2.mutiplicar(*lista))
print("="*50)
ejem2.desep()
print("="*50)
print(ejem2.mutiplicar(*lista))  
print("="*50)
ejem2.dic()
