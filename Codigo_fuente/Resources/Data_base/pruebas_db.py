import sqlite3

miConexion= sqlite3.connect("Users.db")

miCursor = miConexion.cursor()

"""miCursor.execute(
    '''CREATE TABLE USUARIOS(
        NICK VARCHAR(15) PRIMARY KEY,
        NOMBRE VARCHAR(50) NOT NULL,
        EMAIL VARCHAR(60) UNIQUE,
        PASSWORD VARCHAR(20),
        SCORE INTEGER
    )
    '''
)
miCursor.execute(
    'INSERT INTO USUARIOS VALUES("luisito","Luis","luis@gmail.com","luis1234",0)'
)"""

nickvar = input()
emailvar = input()

miCursor.execute(
    'SELECT * FROM USUARIOS WHERE NICK="'
    +nickvar
    +'" OR EMAIL="'
    +emailvar
    +'"'
)

datos = miCursor.fetchall()

print(datos)

if datos != []:
    print('existente')
else:
    print('registrado')

miConexion.commit()
miConexion.close()
