import funciones as fu

while True:
    fu.limpiarpantalla()
    fu.printv("📗📗📘📘Sistema VentaBooks📗📗📘📘")
    fu.printv("******************************************")
    fu.printv("1) Guardar")
    fu.printv("2) Buscar")
    fu.printv("3) Certificados")
    fu.printv("0) Salir")
    opcion=int(input("Selecccione : "))

    #Validamos opcion

    if opcion==0:
        fu.printr("Adios :D")
        break
    elif opcion==1:
        fu.printv("Guardar")
    elif opcion==2:
        fu.printv("Buscar")
    elif opcion==3:
        fu.printv("Certificados")
    else:
        fu.printr("OPCION INVALIDA")

    