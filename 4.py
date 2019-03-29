def primoh():
    a=int(input("Ingrese un numero: "))
    c=0
    c2=0
    if (a%6==0) or (a==6):
        print("El numero no es valido.")
    else:
        while c<=a+1:
            c = c + 1
            if (a+1) % c ==0:
                c2= c2 + 1
        if c2>2:
            print("El numero no es primo hermano.")
        else:
            print("El numero es primo hermano.")

primoh()