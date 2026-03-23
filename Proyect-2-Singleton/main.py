import sqlite3

class Singleton():

    _instances = {} #Instancia del singleton

    # Este metodo te crea una NUEVA instancia de este objeto SI NO EXISTE!! Si existe, no la crea
    def __new__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls)

        return cls._instances[cls]

obj1 = Singleton()
obj2 = Singleton()


print(obj2 is obj2) # Devuelve TRUE, son el mismo objeto.

#APLICACIONES: Imagina que solo necesitas 1 conexion a la bbdd en todo el proyecto, entonces usamos el patrón SINGLETON
# Usamos la libreria SQLite3

class DatabaseConnection(Singleton):
    connection = None

    def __init__(self):
        if self.connection is None:
            #Si no existe, la crea
            self.connection = sqlite3.connect("users.db")
    
    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()


db1 = DatabaseConnection()
db1.execute_query("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)")

db2 = DatabaseConnection()
db2.execute_query("INSERT INTO users(name) VALUES('FRANCHUTE')")

print(db1 is db2)

db1.close()
db2.close()


