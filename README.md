# Mind Quare V.1.0 
 Juego interactivo de preguntas con tablero.
 Grupo #1
Desarrollado por:
    -Camilo Andres Cuello
    -Juan Andres Orozco
    -Santiago Ospina

Universidad Nacional de Colombia.

Objetivo: Videojuego en base a el lenguaje de programación Python :snake:, su temática será la de un juego de preguntas divididas por categorías donde los participantes deberán ir avanzando por un tablero lanzando los dados, dependiendo de la casilla en la que el jugador se sitúe habrá un efecto sobre la partida del mismo. 

En este avance se encuentra lo siguiente:
-Demo de consola "Proyecto programacion.py" que incluye la logica y funcionamiento del juego en la consola cmd.
-interfaz del tablero "tablero.py" un prototipo de la interfaz que tendra MindQuare en su version final.
-Login "LogIn.py" un prototipo junto con una base de datos en la que se puede registrar e iniciar sesion para acceder al juego.

Para el correcto funcionamiento de MindQuare se requieren la instalacion las siguientes librerias que no se encuentran instaladas por defecto:📋
_(Se requiere de sistema operativo windows puesto que se incluyen funciones especificas de la consola cmd)_

Demo de consola:
-colorama : 
pip install colorama

Interfaces:
-pygame : 
pip install pygame==2.0.0.dev18 
-tkinter : 
pip install tk
imageio :
-pip install imageio
imageio_ffmpge:
-pip install imageio_ffmpeg

(Ejecutar el archivo requirements.py para descargar estas librerias.)

INSTRUCCIONES DEL JUEGO

Este es en demo en consola de MindQuare, cuyas reglas son:
1) Se debe ingresar la cantidad de jugadores (debe ser un numero entero).
2) Se debe ingresar el nombre de los respectivos jugadores.
3) MindQuare hara que la partida sea completamente aleatoria.
3) Se lanzaran los dados mostrando sus valores, y el total de casillas.
4) Despues de lanzar los dados el jugador debera reponder una pregunta y dependiendo del tipo
   de casilla este valor afectara la posicion del jugador.
5) El tipo de casilla indica como el valor de los dados afecta al jugador.
   - Trivia Normal, avanza o retrocede normalmente.
   - Trivia Double, avanza o retrocede el doble.
   - Trivia back or advance 1, retrocede o avanza solo 1.
6) Gana el primer jugador que llegue a la casilla numero 60.
