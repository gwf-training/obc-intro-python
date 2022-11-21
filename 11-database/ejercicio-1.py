#En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas: 
# la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido 
# que también será de tipo texto.

#Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos 
# a la tabla.

#Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3
import os

def getDatabasePath():
    return os.path.dirname(os.path.realpath(__file__)) + "\\ejercicio-1.db"

conn = sqlite3.connect(getDatabasePath())

def insertarAlumnos():
    alumnos = [('Lionel', 'Messi'),
                    ('Dibu', 'Martinez'),
                    ('Papu', 'Gomez'),
                    ('Leandro', 'Paredes'),
                    ('Nicolas', 'Tagliafico')]

    cursor = conn.cursor()
    query = f"insert into alumnos(nombre, apellido) values (?, ?)"
    cursor.executemany(query, alumnos)
    conn.commit()
    cursor.close()

def crearTablaAlumnos():
    cursor = conn.cursor()
    cursor.execute('''
    create table alumnos (
        id integer primary key,
        nombre text not null,
        apellido text not null
    );''')
    cursor.close()

def buscarAlumno(nombre):
    cursor = conn.cursor()
    query = f"select * from alumnos where nombre='{nombre}'"
    results = cursor.execute(query)
    alumno = results.fetchone()
    cursor.close()
    return alumno

def main():
    print("Database - SQLite - Alumnos")
    #crearTablaAlumnos()
    insertarAlumnos()
    nombre = input("Nombre de Alumno a buscar: ")
    alumno = buscarAlumno(nombre)
    if alumno != None:
        print("alumno: ", alumno)
    else:
        print("NO SE ENCONTRO AL ALUMNO", nombre)
    conn.close()

if __name__ == "__main__":
    main()