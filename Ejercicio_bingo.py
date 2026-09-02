#Se debe:
#    ● Generar un cartón de 5x5 con números aleatorios del 1 al 50, sin números repetidos. 
#    ● Mostrar el cartón como una grilla. 
#    ● Simular el sorteo: en una estructura repetitiva, generar números aleatorios (sin repetir un número ya sorteado) y mostrarlos. 
#    ● Si el número sorteado está en el cartón, marcarlo (por ejemplo, reemplazándolo por 'X'). 
#    ● Después de cada marca, revisar si se completó una fila, una columna o alguna de las dos diagonales. Si es así, informar "¡BINGO!", 
#    indicar cuántos números se sortearon en total y finalizar el juego.

import random
#creamos la variable carton como una lista vacia
carton=[]
#generamos 25 numeros al azar entre 1 y 50(se guardaran en una lista)                    
numeros_carton=random.sample(range(1,51),25)
#generamos un contador para ir recorriendo cada numero de la lista generada con numeros aleatorios
contador=0
#hacemos doble for, uno para la cantidad de filas que va a tener nuestro carton (5)
for filas in range(5):
    #generamos una lista vacia en cada vuelta del for, con la que vamos a rellenar en el siguiente for
    filas=[]
    #en este for rellenamos cada columna y agregamos la fila completa a la lista carton
    for i in range(5):
        #el contador va a ir recorriendo uno por uno los valores de la lista que contiene los numeros aleatorios
        filas.append(numeros_carton[contador])
        contador+=1
    #una vez rellena la fila, la agregamos al carton, y la lista volvera a vaciarse ya que la creamos dentro del primer for como lista vacia
    carton.append(filas)
#generamos doble bluce for para mostrar la lista como una grilla
for filas in carton:
    for colum in filas:
        print(f"{colum:02d}",end="  ")
    print("")
#generamos los numeros del sorteo al azar y los guardamos en una variable
#se gardaran como una lista
sorteo=random.sample(range(1,51),50)
#con la variable contador,la vamos a usar para ir sacando de a uno los numeros generados en el sorteo
#ya que se generan aleatoriamente
contador=0
#la variable bingo, va a controlar el bucle while y las condiciones para verificar de que forma ha hecho bingo (vertical,horizontal,diagonal)
bingo=False
#la variable contador_de_x nos va a ayudar a saber si se ha completado una linea ya sea horizontal,vertical o diagonal
contador_de_x=0
#iniciamos un bucle while
while not bingo:
#iniciamos el bucle for que va a controlar las filas
    for fila in range(5):
        #en caso de que se haya hecho bingo,esta variable controla que no se vuelva a repetir todo el bucle
        if bingo == True:
            break
        #en caso de no hacer bingo,se iniciara el siguiente bucle for que va a controlar las columnas del carton en este caso
        elif bingo == False:
            for colum in range(5):
                #lo mismo que recien,si ha hecho bingo esta condicion controla que no se vuelva a repetir el bucle
                #hacemos esto porque en las condiciones dentro de este bucle for hay otros bucle for que van a estar verificando las distintas formas de hacer bingo
                #y al hacer break solo parara ese bucle, y cambiara la condicion de bingo a True, de esta manera logramos que se frenen todos los bucles for sino el juego no se detendria
                #hasta que terminara todo el bucle completo 
                if bingo == False:
                    #una vez pasada la condicion de bingo(todavia no hace bingo)
                    #esta condicion va a verificar que el primer numero sorteado sea igual a algun numero dentro del carton
                    #en caso de no cumplirse volvera a ininciarse el bucle pero esta vez con valores distintos de (fila,columa)
                    #de esta forma podremos fijarnos en todo el carton hasta encontrarlo,sino empezara otro bucle pero cambiara al segundo numero sorteado    
                    if carton[fila][colum] == sorteo[contador]:
                        #en caso de encontar el numero dentro del carton,verificaremos si se ha hecho bingo de todas las formas posibles
                        carton[fila][colum]="X"
                        #esta condicion con la funcion count() nos permite saber cuantos valores respecto al parametro pasado hay
                        #si llegase ha completar una fila entera se hara bingo, y cambiara la variable a True para que no se repita ningun bucle y termine
                        if carton[fila].count("X") == 5:
                            print("Bingo horizontal")
                            bingo=True
                            break
                        #en caso de que no se haya encontrado en ninguna fila,entrara a esta condicion donde verificaremos si ha hecho bingo de manera "vertical"
                        if bingo == False:
                            #iniciamos doble bucle for,donde la i va a controlar las filas y la j las columnas
                            for i in range(5):
                                for j in range(5):
                                    #verificamos de forma vertical, donde j va a controlar la columna y i las filas
                                    if carton[j][i] == "X":
                                        #en caso de encontrar sumara a la variable contadora de x 1
                                        contador_de_x+=1
                                        #en caso de llegar a 5,se imprimira bingo y se cambiara la variable bingo a "True" muy importarnte ya que esa variable controla todos los bucles
                                        if contador_de_x == 5:
                                            print("Bingo vertical")
                                            bingo=True
                                            break
                                    #en caso de no encontrar una "X" hacemos un break para que no siga buscando y se cambie la variable del bucle de arriba(i)
                                    #para asi buscar en otra columna el bingo
                                    else:
                                        break
                                #aca nuevamente verificamos que el bingo siga en False para volver a ejecutar el bucle for mayor (i)
                                #en caso contrario que sea True se frenara el bucle 
                                if bingo == True:
                                    break
                                #el contador de x siempre que termine el bucle chico (j) volvera a 0 para no generar problemas si en la columna anterior habia una x o mas
                                contador_de_x=0
                        #en caso de no haber encontrado todavia el bingo,esta condicion verificara si se ha hecho bingo de manera diagonal                    
                        if bingo == False:
                            #volvemos el contador de x a 0
                            contador_de_x=0
                            #iniciamos un bucle for
                            for i in range(5):
                                #y nos fijamos si en el carton hay una "X"
                                #carton[i][i], para el valor 0 tomara la primera fila y el primer valor
                                #cuando se reinicie el bucle tomara el valor 1 dando asi la segunda fila con el segundo valor
                                #de esa forma se producira una verificacion de manera vertical
                                if carton[i][i] == "X":
                                    #por cada "X" sumara a la variable contadora de x 
                                    contador_de_x+=1
                                    #en caso de llegar a 5 se imprimira bingo y se actualizara la variable bingo a "True" para detener todos los bucles 
                                    if contador_de_x == 5:
                                        print("Bingo diagonal")
                                        bingo=True
                                        break
                                #en caso de que no encuentre una "X" en alguna vuelta del bucle cortaremos inmediatamente el programa ya que no tiene sentido seguir
                                #porque no sera bingo
                                else:
                                    break
                        #y por ultimo esta condicion en caso de todavia no hacer bingo
                        #verificara la otra forma diagonal posible de hacer bingo
                        if bingo == False:
                            #iniciamos la variable contadora de x en 0
                            contador_de_x=0
                            #iniciamos un bucle for
                            for i in range(5):
                                #esta vez tenemos que hacer la diagonal contraria,empezaremos por la primer sublista y la ultima columna
                                #-1-i hace refencia ha que en la primer vuelta va a valer 0 la i para la fila y para la columna (0-1=-1)
                                #y asi cuando i valga 1 la columna va a valer -2 y asi logramos que se vaya haciendo la diagonal contraria a la de arriba
                                if carton[i][-1-i] == "X":
                                    #y aca repetimos el proceso de la condicion de la diagonal de arriba
                                    contador_de_x+=1
                                    if contador_de_x == 5:
                                        print("Bingo diagonal")
                                        bingo=True                           
                                        break
                                else:
                                    break
    #el contador para ir cambiando el numero sorteado lo dejamos alineado al terminar ambos bucles for iniciales que recorren todo el carton 
    #verificando si esta el numero sorteado
    contador+=1

                           
                            
                                
                        
                
                        
                    
            


     