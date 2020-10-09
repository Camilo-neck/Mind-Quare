import msvcrt #kbhit->esperar tecla , getch->leer tecla
import time #sleep->simular temporizador haciendo que el programa espere 1 segundo entre cada bucle
import os #system('cls')->limpiar la consola , getcwd-> obtener la ruta actual
import random #generar numeros aleatorios

def imprimir_pregunta(num_p): #funcion para imprimir las preguntas, esta lee un archivo que las incluye
    archivo = open((os.getcwd() + "\preguntas.txt"), 'r') #se obtiene la ruta del archivo y este se abre
    # se crea una lista en base a el indice de la pregunta
    with archivo as f:
        data = f.readlines()[((num_p*5)):(num_p*5)+5]
    # se imprime la pregunta linea a linea basado en la lista data
    print((data[0]))
    print((data[1]).strip()) #se pone strip porque por defecto guarda el caracter de salto de lineacls
    print((data[2]).strip())
    print((data[3]).strip())
    print((data[4]).strip())
    archivo.close() #se cierra el archivo
def revisar_respuesta(num_p,rta, respuestas): #funcion para revisar la validez de la respuesta intruducida
    if rta==respuestas[num_p]:
        print("\nCORRECTO")
    else:
        print("\nINCORRECTO")

def catch_count(temp, num_p, respuestas):
    while temp+1>0:
        time.sleep(1)
        os.system('cls')
        imprimir_pregunta(num_p)
        if msvcrt.kbhit():
            rta=(chr(ord(msvcrt.getch()))).upper() #conversion de la entrada a ascii -> chr -> mayuscula (esto porque getch agrega un 'b' a cualquier entrada)
            print("\nEscogio la opcion:",rta)
            time.sleep(2.5)
            revisar_respuesta(num_p,rta,respuestas)
            break
        else:
            print("\n",temp)
        temp-=1
    if temp<0:
        print("\nTiempo agotado")
    time.sleep(2)

#funcion principal
def main():
    temp=20
    cant_preguntas=5
    num_p=random.randint(0,cant_preguntas-1) #generar numero aleatorio para la pregunta
    respuestas=['B','A','C','A','D'] #ingresar aqui las respuestas deseadas
    catch_count(temp,num_p,respuestas)

if __name__ == '__main__':
    main()
