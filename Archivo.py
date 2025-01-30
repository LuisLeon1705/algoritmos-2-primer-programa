# Clase que representa un archivo dentro del repositorio
class Archivo:
    # Constructor de la clase Archivo
    # Parámetros:
    # - nombre: El nombre del archivo
    # - contenido: El contenido del archivo
    def __init__(self, nombre, contenido):
        self.nombre = nombre # Nombre del archivo
        self.contenido = contenido # Contenido asociado al archivo

    # Método que devuelve una representación del archivo en forma de cadena
    # Incluye el nombre y el contenido del archivo
    def __repr__(self):
        return f"Archivo(nombre='{self.nombre}', contenido='{self.contenido}')"
