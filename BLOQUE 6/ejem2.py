count=0
while count<=10:
    print(f"{count}")
    count+=1

for e in range(0,20,2):
    print(e)

frutas=["Perita","Manzana","Guineo"]
for indice,fruta in enumerate(frutas):
    print(f"{indice}-{fruta}")

carros=["SUPRA","AVEO","GIXER","SUZUKI"]
for indice,carro in enumerate(carros):
    print(f"{indice}--{carro}")

cuadrados = [x**2 for x in range(10)]
print(cuadrados)
pares = [x for x in range(10) if x % 2 == 0]
print(pares)
cuadrado_pares = [n**2 for n in range(1,11) if n % 2 == 0]
print(cuadrado_pares)
for e in range(0,20,2):
    print(e)


contador=0
while contador<=50:
    
    print(f"{contador}")
    contador+=1

zapatos=["ADIDAS","NIKE","SCHECKER"]
for indice,nombre in enumerate(zapatos):
    print(f"{indice}--{nombre}")

cuadrado=[x*2 for x in range(10) if x%2==0]
print(cuadrado)


