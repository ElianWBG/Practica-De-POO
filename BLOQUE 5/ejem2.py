def validar_par():
    num=int(input("Ingrese un numero "))
    if num%2==0:
        print(f"{num} Es par ")
    else:
        print(f"{num} Es Impar ")
# validar_par()

def asignar():
    num=int(input("Ingrese su nota "))
    if  num>=90:
        print("Su Calificacion es A")
    elif num>=80:
        print("Su calificacion es B")
    elif num>=70:
        print("Su calificacion es C")
    else:
        print("Su calificacion es D")

# asignar()
def login():
    usuario="admin"
    password="123"
    usua=str(input(" Ingrese usuario "))
    contr=(input(" Ingrese contraseña "))
    if usua==usuario and contr==password:
        print(" Acceso concedido ")
    else:
        print(" Acceso Denegado ")     
login()   






    
    
    