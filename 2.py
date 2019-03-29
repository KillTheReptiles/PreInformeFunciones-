def exponente():
    a1=int(input("Escriba un numero: "))
    b1=int(input("Escriba su exponente: "))
    operacion1=a1**b1
    print("El resultado es: ", operacion1)

    a2=int(input("Escriba un numero: "))
    b2=int(input("Escriba su exponente: "))
    operacion2=a2**b2
    print("El resultado es: ", operacion2)

    if operacion1>operacion2:
      print("El primer numero es mayor")
    else:
      print("El segundo es mayor")

exponente()