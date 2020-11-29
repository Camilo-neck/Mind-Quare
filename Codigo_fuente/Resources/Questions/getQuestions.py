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
    opciones = [t for t in soup.find_all(text=True) if t.parent.name in ['h6','opcion']]

    preguntasMatematicas = obt_preguntas(enunciados,opciones,0,20)
    preguntasHistoria = obt_preguntas(enunciados,opciones,20,40)

    crear_archivo(preguntasMatematicas,'preguntas_matematicas.txt')
    crear_archivo(preguntasHistoria,'preguntas_historia.txt')

if __name__=='__main__':
    main()