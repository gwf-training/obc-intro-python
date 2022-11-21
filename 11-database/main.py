import sqlite3
import os, getpass

def getDatabasePath():
    return os.path.dirname(os.path.realpath(__file__)) + "\\mydatabase.db"

conn = sqlite3.connect(getDatabasePath())

def verifcarCredenciales(username, password) -> bool:
    cursor = conn.cursor()
    users = cursor.execute(f"select * from users where username='{username}' and password='{password}'")
    user = users.fetchone()
    cursor.close()
    if user == None:
        return False
    return True

def crearUsuario(id, username, password) -> bool:
    cursor = conn.cursor()
    query = f"insert into users(id, username, password) values ({id},'{username}','{password}')"
    user = cursor.execute(query)
    conn.commit()
    cursor.close()

def main():
    global conn
    print("SQLite3")
    username = input("username: ")
    password = getpass.getpass("password: ")
    
    if verifcarCredenciales(username, password):
        print("login correcto")
        crearUsuario(10, "pepe", "pepe")
    else:
        print("login incorecto")
    return
    conn.close()

if __name__ == "__main__":
    main()