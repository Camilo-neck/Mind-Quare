import sqlite3

miConexion= sqlite3.connect("Ingreso Datos.db")

miCursor = miConexion.cursor()

#miCursor.execute(
#    '''CREATE TABLE USUARIOS(
#        DNI INTEGER PRIMARY KEY,
#        NOMBRE VARCHAR(50) NOT NULL,
#        APELLIDO VARCHAR(50) NOT NULL,
#        EMAIL VARCHAR(60) UNIQUE,
#        PASSWORD VARCHAR(20)
#    )    
#    '''
#)

#miCursor.execute('INSERT INTO USUARIOS VALUES(NULL,"Carlos","Cruz",1001184562,"carlos@gmail.com","carlos1234")')

miConexion.commit()
miConexion.close()