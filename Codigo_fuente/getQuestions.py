"""
MIND QUARE - Juego interactivo de preguntas con tablero.
Algoritmo que extrae las preguntas desde la web y las escribe en archivos .txt.
Desarrollado por:
    -Camilo Andres Cuello
    -Juan Andres Orozco
    -Santiago Ospina
Universidad Nacional de Colombia - Facultad de Ingenieria.
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen
import os

def obt_preguntas(enunciados,opciones,a,b):
    '''
    Obtener las preguntas en base a los objetos de enunciados y opciones de la clase bs4.element usando el metodo.getText y organizandolas en un diccionario
    :param bs4.element enunciados: enunciados obtenidos con la libreria bs4
    :param bs4.element opciones: opciones obtenidas con la libreria bs4
    :param int a: inicio del rango desde donde se leeran los datos
    :param int b: final del rango hasta donde se leeran los datos
    :return: dict preguntas
    '''
    preguntas = {}

    for i in range(a,b):
        preguntas[i-a] = {
            'enunciado' : enunciados[i].getText(),
            'opcionA' : opciones[i*4].getText(),
            'opcionB' : opciones[i*4+1].getText(),
            'opcionC' : opciones[i*4+2].getText(),
            'opcionD' : opciones[i*4+3].getText(),
        }
    return preguntas

def crear_archivo(preguntas,nombre):
    '''
    Crear un archivo en base al diccionario de las preguntas de una categoria y un nombre
    :param dict preguntas: diccionario de preguntas de una categoria
    :param str nombre: nombre con el cual se guardara el archivo
    '''
    text = ''
    for i in range(0,20):
        text += '\n'.join([str(e) for e in preguntas[i].values()])
        if i < 19:
            text += '\n'
    
    ruta = os.path.join(os.getcwd() + '\\Resources\\Questions\\', nombre)
    archivo = open(ruta,'w',encoding='utf-8')
    archivo.write(text)
    archivo.close()

def obt_respuestas(respuestas,a,b):
    '''
    Obtener las respuestas en base al objeto de respuestas de la clase bs4.element usando el metodo.getText retornandolas como un string
    :param bs4.element respuestas: respuestas obtenidas con la libreria bs4
    :param int a: inicio del rango desde donde se leeran los datos
    :param int b: final del rango hasta donde se leeran los datos
    :return: str R
    '''
    R = ''
    for i in range(a,b):
        R += "'"+(respuestas[i].getText())
        if i<(b-1):
            R += "', "
        else:
            R += "'"
    return R  

def main():
    #leer la url y crear un objeto con la libreria bs4 que contendra el html del sitio web
    url = "https://camilo-neck.github.io/MindQuare-Web/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    #scrapear los enunciados, opciones y respuestas
    enunciados = soup.find_all("h3", class_="enunciado")
    opciones = soup.find_all("h6", class_="opcion")
    respuestas  = soup.find_all("h5", class_="respuesta")

    #extraer las preguntas por categoria
    preguntasMatematicas = obt_preguntas(enunciados,opciones,0,20)
    preguntasHistoria = obt_preguntas(enunciados,opciones,20,40)
    preguntasGeografia = obt_preguntas(enunciados,opciones,40,60)
    preguntasCiencia = obt_preguntas(enunciados,opciones,60,80)
    preguntasEntretenimiento = obt_preguntas(enunciados,opciones,80,100)

    #extraer las respuestas por categoria
    RM = obt_respuestas(respuestas,0,20)
    RH = obt_respuestas(respuestas,20,40)
    RG = obt_respuestas(respuestas,40,60)
    RC = obt_respuestas(respuestas,60,80)
    RE = obt_respuestas(respuestas,80,100)

    #crear un archivo con las preguntas por cada categoria
    crear_archivo(preguntasMatematicas,'preguntas_matematicas.txt')
    crear_archivo(preguntasHistoria,'preguntas_historia.txt')
    crear_archivo(preguntasGeografia,'preguntas_geografia.txt')
    crear_archivo(preguntasCiencia,'preguntas_ciencia.txt')
    crear_archivo(preguntasEntretenimiento,'preguntas_entretenimiento.txt')

    #crear un archivo con las respuestas
    ruta = os.path.join(os.getcwd() + '\\Resources\\Questions\\', 'Respuestas.txt')
    archivo = open(ruta,'w')
    archivo.write(RM+'\n')
    archivo.write(RH+'\n')
    archivo.write(RG+'\n')
    archivo.write(RC+'\n')
    archivo.write(RE+'\n')
    archivo.close()
    

if __name__=='__main__':
    main()
