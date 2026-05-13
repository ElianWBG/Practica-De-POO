class EjerciciosB3:
    def mostar_opera(self):
        a=20
        b=4
        suma=a+b
        resta=a-b
        multiplicar=a*b
        dividir=a/b
        division_ente=a//b
        resto=a%b
        print("="*50)
        print(suma)
        print(resta)
        print(multiplicar)
        print(dividir)
        print(division_ente)
        print(resto)
        print("="*60)


li=[10,11,12,13]
li2=[10,11,12,13]
           
print(li==li2)
print(li is li2)

a=EjerciciosB3()
a.mostar_opera()     
