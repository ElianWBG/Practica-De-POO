class ejem2:
    @staticmethod
    def funcion_doble(a):
        return print(a*2)
    
    @staticmethod
    def sumar_todo(*nume):
        return sum(nume)
    
    @staticmethod
    def factorial(n):
        if n == 0: return 1 # caso base
        return n * ejem2.factorial(n - 1) # llamada recursiva


    
    

ejem2.funcion_doble(5)
print(ejem2.sumar_todo(32,21,32,1,23,23))
print(ejem2.factorial(5))

    
    
