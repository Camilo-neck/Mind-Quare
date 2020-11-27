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
    'SELECT SCORE FROM USUARIOS WHERE NICK="'
    +nickvar
    +'" OR NICK="fercho" OR NICK="roby"'
)

score = miCursor.fetchall()
new_score = 30

print(score)

"""miCursor.execute(
    'UPDATE USUARIOS SET SCORE='
    +str((score+new_score))
    +' WHERE NICK="'
    +nickvar
    +'"'
)

miCursor.execute(
    'SELECT SCORE FROM USUARIOS WHERE NICK="'
    +nickvar
    +'" OR EMAIL="'
    +emailvar
    +'"'
)

score = miCursor.fetchall()[0][0]

print(score)"""

miConexion.commit()
miConexion.close()
