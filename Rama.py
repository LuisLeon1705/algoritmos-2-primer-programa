# Clase que representa una rama en el repositorio
class Rama:
    # Constructor de la clase Rama. Inicializa la rama con un nombre y opcionalmente un commit inicial
    def __init__(self, nombre, commit_inicial=None):
        self.nombre = nombre
        self.ultimo_commit = commit_inicial

    # Método especial para representar la información de la rama en formato string
    # Útil para depuración y mostrar el estado de la rama
    def __repr__(self):
        return f"Rama(nombre='{self.nombre}')"
