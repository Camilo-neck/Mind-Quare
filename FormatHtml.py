preguntas = '''¿Cómo se llama el componente mínimo que forma a los seres vivos?
Tejido
Particula
Celula
Corazon
El proceso por el que una célula se divide para formar dos células hijas se llama:
Segregacion
Mitosis
Meiosis
Fotosintesis
La información genética en las células se localiza:
Nucleo
Membrana
Citoplasma
Ribosoma
¿Con qué respira una ballena?
Por la piel
Pulmones
aletas
Branquias
La fuerza física que la tierra ejerce sobre los cuerpos hacia su centro es la:
Gravedad
Normal
Rozamiento
Tension
¿Cómo se llama la teoría que considera que todos los organismos descendemos del mismo ancestro?
Creacionismo
Darwinismo
Gradualismo
Existencialismo
El proceso mediante el cual se generan moléculas orgánicas a partir de sustancias inorgánicas usando como fuente de energía el sol es:
Catabolismo
Anabolismo
Fotosintesis
Germinacion
La  columna más a la derecha de la tabla periódica esta compuesta por:
Haluros
Metales
Minerales
Gases Nobles
La velocidad a la que viaja la luz es
300,000 m/s
300,000 km/s
30,000 m/s
30,000 km/s
¿Cómo se llaman las partículas subatómicas con carga eléctrica negativa?
Neutrones
Protones
Electrones
Ninguna de las anteriores
El sol es:
Un planeta
Una estrella
Estrella y satelite
Un satelite
¿Que invento Alfred Nobel, el que da nombre alos famosos premios?
Dinamita
Penicilina
Bomba atomica
Telefono
El teorema que dice que "en todo triángulo rectángulo, el cuadrado de la hipotenusa es igual a la suma de los cuadrados de los catetos" es el:
Teorema de Arquimedes
Teorema de Pitagoras
Teorema de Tales
Ninguno de los anteriores
Para el pan y para la cerveza se utilizan para fermentar:
Microbios
Bacterias
Levaduras
Sales
¿Cuál es la principal función de los globulos rojos?
Combatir enfermedades
Coagular la sangre
Llevar oxigeno
Pigmentar la piel
¿Qué tipo de radiación te produce quemaduras?
Ultravioleta
Rayos X
Rayos Gamma
Infrarroja
¿Cuantos planetas hay en el sistema solar?
9
8
6
5
¿Que particulas son mas pequeñas que los atomos?
Aniones
Electrones
Fotones
Todas las anteriores
Cual es el tercer planeta en el sistema solar:
Tierra
Mercurio
Urano
Marte
Como se llama la galaxia en la que se encuentra el sistema solar:
Andromeda I
Centaurus A
Enana de Acuario
Via Lactea
'''
preguntas = [e for e in (preguntas.split('\n'))]
respuestas = [' ','C', 'B', 'A', 'B', 'A', 'B', 'C', 'D', 'B', 'C', 'B', 'A', 'B', 'C', 'C', 'A', 'B', 'B', 'A', 'D']

for i in range(len(preguntas)):
    cont=0
    if i % 5 ==0: 
        preguntas[i] = '    <br></br><h3 class="enunciado">'+preguntas[i].strip(' ')+'</h3>'
    else:
        preguntas[i] = '    <h6 class="opcion">'+preguntas[i].strip(' ')+'</h6>'  
        
cont = 8
cont2 = 0
for i in range(len(preguntas)+60):
    if cont == 8 :
        preguntas.insert(i, '    <h5 class="respuesta">'+respuestas[cont2]+'</h5>')
        preguntas.insert(i+1,'</div>')
        preguntas.insert(i+2,'<div class="pregunta">')
        cont = 0
        cont2+=1
    cont+=1
    print(preguntas[i])