def primos():
    n=int(input("Ingrese un numero: "))
    c = 0
    for i in range(1,n+1):
        if (n% i)==0:
            c=c + 1
    if c==2:
        print ("El número ingresado es primo.")
    else:
        print ("El número ingesado no es primo.")
primos()        