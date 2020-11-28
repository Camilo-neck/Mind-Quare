preguntas = '''¿Cómo se llamó durante más de 50 años San Petersburgo?
Petroburgo
Leningrado   
Trostskigrado
Stalingrado
¿En que isla murió Napoleón?
Cerdeña
Santa Elena     
Elba
Corcega
¿Cuál de estos cuatro hechos históricos es más antiguo?
Nacimiento de Confucio      
Nacimiento de Buda Gautama
Nacimiento de Mahoma
Nacimiento de Jesucristo
¿Cuál de estas no es una las 7 maravillas del mundo antiguo?
Partenon     
Gran pirámide de guiza
Templo de artemisa
Jardines colgantes de babilonia
¿Cómo se llamaba el primer Presidente de los Estados Unidos?
John Adams
George Washintong       
Abraham Lincoln
Thomas Jefferson
¿En qué año cayó el Imperio Romano de Occidente?
456
476       
501
496
¿Cómo se llama la Reina del Reino Unido?
Isabel I
Lady Jane Gray
Isabel II      
Margarita
¿Dónde originaron los juegos olímpicos?
Grecia     
Japon
Noruega
Roma
¿Cuándo acabó la II Guerra Mundial?
1930
1945      
1950
1939
¿Quién pintó “la última cena”?
Pablo Picasso
Monet
Miguel Angel
Leonardo Da Vinci      
¿Quién es el famoso Rey de Rock en los Estados Unidos?
Freddy Mercurie
Elvis Presley       
Michael Jackson
John Lennon
¿Cuál es la moneda del Reino Unido?
La Libra      
El Euro
El Dólar
El Yen
'''
preguntas = [e for e in (preguntas.split('\n'))]

for i in range(len(preguntas)):
    if i % 5 ==0:
        preguntas[i] = '<br></br><h3>'+preguntas[i].strip(' ')+'</h3>'
    else:
        preguntas[i] = '<h6>'+preguntas[i].strip(' ')+'</h6>'

    print(preguntas[i])

input()