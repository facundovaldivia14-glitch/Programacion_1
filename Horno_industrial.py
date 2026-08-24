#Iniciamos un while para que el usuario ingrese las temperaturas que desee hasta que decida pararlo
while True:
    #pedimos la temperatura como str para hacer las validaciones
    print("Ingrese la palabra FIN para salir")
    temperatura=input("Ingrese la temperatura actual del horno: ").upper()
    #si el usuario ingresa "FIN" cortamos el programa directamente
    if temperatura == "FIN":
        break
    #creamos variables para validar, una valida que no se pase de puntos y la otra da la señal para transformar a float
    puntos=0
    validar=True
    #recorremos el str ingresado caracter por caracter atravez de un for y validamos cada caracter
    for i in temperatura:
        if i == "." :
            puntos+=1
            #en caso de que tenga mas de un punto, cambiamos la variable a False y cortamos el bucle for para que vuelva a ingresar la temperatura
            if puntos > 1:
                validar=False
                print("Error: Ha ingresado mas de un punto")
                break
        #en caso de que no sea un punto va a validar que sea un digito, si no es un digito la variable vuelve a cambiar a False cortando el bucle 
        elif not i.isdigit():
            validar=False
            print("Error: Ha ingresado un caracter no valido ")
            break
    #nos fijamos si el usuario a ingresado una cadena vacia o solamente un punto, anticipando los posibles errores y cambiamos la variable a False
    #para que no se convierta a float y se rompa el programa
    if temperatura == "" or temperatura == "." :
            validar=False
            print("Error: No ha ingresado un numero ")
    #por ultimo luego de pasar por toda la validacion se convierte a float y se verifica si esta dentro del rango de la temperatura 
    if validar == True :
        temperatura=float(temperatura)
        print(f"Temperatura cargada correctamente {temperatura}ºC")
        if   temperatura < 100 or temperatura > 500:
            print("ADVERTENCIA TEMPERATURA FUERA DE RANGO")