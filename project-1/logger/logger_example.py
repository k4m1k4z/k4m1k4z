# Logger -> sirve para manejar y guardar datos de tu aplicación en determinado momento
# Ejemplo: guardar peticiones con el método GET, POST...
# Ejemplo: guardar mensajes de error.
# Guardar excepciones
# Guardar capturas dentro de bloques..
import traceback  #Paquete que nos permite sacar toda la trazabilidad hasta llegar al error

from utils.Logger import Logger

#Test
a = 20
b = 0

def main():
    try:
        result = a / b
        print("El resultado es: {}".format(result))
    except Exception as ex:
        Logger.add_to_log("error",str(ex))
        Logger.add_to_log("error", traceback.format_exc())
        print("No se puede dividir entre 0")


main()