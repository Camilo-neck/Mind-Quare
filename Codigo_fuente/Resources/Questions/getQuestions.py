from bs4 import BeautifulSoup
from urllib.request import urlopen

def obt_preguntas(enunciados,opciones,a,b):
    preguntas = {}

    for i in range(a,b):
        preguntas[i-a] = {
            'enunciado' : enunciados[i],
            'opcionA' : opciones[i*4],
            'opcionB' : opciones[i*4+1],
            'opcionC' : opciones[i*4+2],
            'opcionD' : opciones[i*4+3]
        }
    return preguntas

def crear_archivo(preguntas,nombre):

    text = ''
    for i in range(0,20):
        text += '\n'.join([str(e) for e in preguntas[i].values()])
        if i < 19:
            text += '\n'
    

    archivo = open(nombre,'w',encoding='utf-8')
    archivo.write(text)
    archivo.close()

def main():
    url = "https://camilo-neck.github.io/Mind-Quare/"
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    enunciados = [t for t in soup.find_all(text=True) if t.parent.name in ['h3','enunciado']]
    opciones = [t for t in soup.find_all(text=True) if t.parent.name in ['h5','opcion']]
    respuestas = [t for t in soup.find_all(text=True) if t.parent.name in ['h5','respuestas']]

    #extraer las preguntas por categoria
    preguntasMatematicas = obt_preguntas(enunciados,opciones,0,20)
    preguntasHistoria = obt_preguntas(enunciados,opciones,20,40)
    preguntasGeografia = obt_preguntas(enunciados,opciones,40,60)
    preguntasCiencia = obt_preguntas(enunciados,opciones,60,80)
    preguntasEntretenimiento = obt_preguntas(enunciados,opciones,80,100)
    #extraer las respuestas por categoria
    R = ','.join([e for e in respuestas])
    print(respuestas)
    print(R)
    input()

    #crear un archivo con las preguntas por cada categoria
    crear_archivo(preguntasMatematicas,'preguntas_matematicas.txt')
    crear_archivo(preguntasHistoria,'preguntas_historia.txt')
    crear_archivo(preguntasGeografia,'preguntas_geografia.txt')
    crear_archivo(preguntasCiencia,'preguntas_ciencia.txt')
    crear_archivo(preguntasEntretenimiento,'preguntas_entretenimiento.txt')
    

if __name__=='__main__':
    main()