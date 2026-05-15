def clasificar_vehiculo():
    tipo=input("Ingrese tipo")
    velo=int(input("Velocidad actual"))
    años=int(input("Año de antiguedad"))

    
    match tipo:
        case"auto" :categoria="vehiculo Liviano"
        case"moto":categoria="Vehiculo dos ruedad"
        case"camion": categoria="Vehiculo pesado"
        case"bus":categoria="trasporte publico"
        case _: categoria="Vehiculo desconocido"
        
    
   
    if velo<60:
        velocidad="Velocidad baja"
    elif velo>=60 and velo<120: 
        velocidad="Velocidad Normal"
    else:
        velocidad="Exceso de velocidad"
    
    estado="vehiculo riesgoso" if años>10 and velo>100  else "Vehiculo en condiciones"
    
    
    



    print("======REPORTE VEHICULAR=======")
    print(f"Tipo: {tipo}--{categoria}")
    print(f"velocidad: {velo}-- Km/h{velocidad}")
    print(f"Años: {años}--{estado}")
clasificar_vehiculo()