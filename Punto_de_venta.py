cuenta=0
while True:
    print("Opcion 1: Agregar Hamburguesa($4500)")
    print("Opcion 2: Agregar Papas Fritas($2000)")
    print("Opcion 3 Agregar Bebida($1500)")
    print("Opcion 4: Pagar el pedido(Cierra el ticket")
    print("Opcion 5: Cancelar pedido y salir")
    #pedimos el dato como str para validar la opcion y que se encuentre dentro del rango
    pedido=input("Seleccione una opcion: ")
    while not pedido.isdigit() or 1 > int(pedido) > 5:
        print("Por favor seleccione una opcion valida entre 1 y 5")
        pedido=input("Seleccione una opcion nuevamente")
    #convertimos a entero e iniciamos un match case
    pedido=int(pedido)
    
    match pedido:
        case 1:
            #damos un mensaje de exito y mostramos el total de su cuenta a pagar, con cada opcion que vaya a agregar
            cuenta+=int(4500)
            print("Hamburguesa agregada")
            print(f"Total actual ${cuenta}")
        case 2:
            cuenta+=int(2000)
            print("Papas Fritas agregadas")
            print(f"Total actual ${cuenta}")
        case 3:
            cuenta+=int(1500)
            print("Bebida agregada")
            print(f"Total actual ${cuenta}")
        case 4:
            #le mostramos el total a pagar y verificamos que el monto ingresado sea un numero entero, mayor o igual a la suma a pagar
            print(f"El total a pagar es ${cuenta}")
            efectivo_cliente=input("Ingrese el monto, debe ser mayor al total a pagar: ")
            while not efectivo_cliente.isdigit() or int(efectivo_cliente) < cuenta :
                print("El monto debe ser mayor o igual al total a pagar")
                efectivo_cliente=input("Ingrese nuevamente el dinero del cliente: ")
            #una vez hecha la validacion convertimos a entero y le restamos el dinero del cliente a la cuenta a pagar
            #para asi saber cuanto es su vuelto si le corresponde
            efectivo_cliente=int(efectivo_cliente)
            
            efectivo_cliente-=cuenta
            
            print(f"El vuelto del cliente es ${efectivo_cliente}")
            
            cuenta=0
        case 5 :
            #cerramos el programa 
            print("Cancelando pedido y cerrando programa...")
            break