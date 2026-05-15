def evaluar_estudiantes():
    nom=input("Ingrese su nombre ")
    not1=float(input("Ingrese primera nota "))
    not2=float(input("Ingrese segunda nota "))
    not3=float(input("Ingrese examen final "))
    asistencia=float(input("Ingrese porcentaje de asistencia " ))

    notas=[not1,not2,not3]
    promedio=sum(notas)/len(notas)

    pro="Aprobado" if promedio>=70 else "Reprobado"
    asis="Asistencia suficiente" if asistencia>=75 else "Asistecia insuficiente"
    estado="PROMOVIDO" if promedio>=70 and asistencia>=75 else "NO PROMOVIDO"
    print("=====REPORTE ESTUDIANTIL======")
    print(f"Nombre: {nom} ")
    print(f"Promedio: {promedio}--{pro} ")
    print(f"Asistencia {asistencia}%--{asis}")
    print(f"Estado: {estado}")
evaluar_estudiantes()