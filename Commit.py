#Importamos un generador de ID's
import uuid

# Clase que representa un commit en el repositorio
class Commit:
    # Constructor de la clase Commit
    # Parámetros:
    # - mensaje: Descripción del commit, generalmente indicando los cambios realizados
    # - archivos: Lista de objetos Archivo que forman parte del commit
    # - anterior: Referencia al commit previo 
    def __init__(self, mensaje, archivos, anterior=None):
        self.id = str(uuid.uuid4())[:8]  # ID único generado automáticamente (primeros 8 caracteres del UUID)
        self.mensaje = mensaje           # Mensaje asociado al commit
        self.archivos = archivos         # Archivos que se incluyen en este commit
        self.anterior = anterior         # Referencia al commit anterior, si existe

    # Método que retorna una representación en formato string del commit
    # Esto facilita mostrar información básica, como el ID y el mensaje del commit
    def __repr__(self):
        return f"Commit(id='{self.id}', mensaje='{self.mensaje}')"

