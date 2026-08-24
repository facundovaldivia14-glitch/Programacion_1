#craemos el saldo inicial
saldo=50000
#iniciamos un bucle while para que el usuario decida cuando cortar el programa, con menu de opciones
while True:
    print("Opcion 1: Consultar salto")
    print("Opcion 2: Ingresar dinero")
    print("Opcion 3: Retirar dinero")
    print("Opcion 4: Salir")
    #pedimos el dato como str para validar que haya ingresado una opcion correcta
    usuario=input("Seleccione una opcion: ")
    #en caso de no ingresar un numero o un numero fuera del rango de opciones volveremos a pedirlo
    while not usuario.isdigit() or 1 > int(usuario) or int(usuario) > 4:
        print("Por favor ingrese una opcion correcta entre 1 y 4")
        usuario=input("Seleccione una opcion nuevamente: ")
    #una vez se haya validado se convierte a entero
    usuario=int(usuario)
    match usuario:
        #mostramos su saldo actual
        case 1:
            print(f"Su saldo actual es {saldo}")
        case 2:
            #le pedimos el dato como str para validar el dinero a depositar
            ingresar=input("Ingrese el dinero a depositar: ")
            while not ingresar.isdigit():
                print("Por favor ingrese un numero entero sin puntos ni coma")
                ingresar=input("Ingrese el dinero a depositar nuevamente")
            ingresar=int(ingresar)
            #una vez validado el dinero a depositar lo convertimos a entero y lo sumamos a su saldo actual
            saldo+=ingresar
            print(f" dinero ingresado,su saldo actual es {saldo}")
        case 3:
            #le pedimos el dato como str para validar el dinero a retirar
            print(f"Su saldo actual para retirar es {saldo}")
            retirar=input("Ingrese el dinero a retirar: ")
            #el dinero debe ser un numero entero y ser mayor o igual, al saldo actual
            while not retirar.isdigit() or saldo < int(retirar):
                print("Por favor ingrese un monto dentro del rango")
                retirar=input("Ingrese el dinero a retirar nuevamente")
            #una vez validado se convierte a entero y se resta del saldo actual
            retirar=int(retirar)
            saldo-=retirar
            print(f"dinero retirado,saldo actual {saldo}")
        case 4:
            #cerramos sesion
            print("Cerrando sesion...")
            break