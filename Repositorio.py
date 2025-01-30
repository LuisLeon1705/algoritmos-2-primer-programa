# Importaciones del resto de clases necesarias para la función del programa
from Archivo import Archivo # Importa la clase Archivo desde Archivo.py
from Commit import Commit # Importa la clase Commit desde Commit.py
from Rama import Rama # Importa la clase Rama desde Rama.py

# Clase de Repositorio que permite gestionar las funciones y el estado global del sistema Git simplificado
class Repositorio:
    # Constructor de la clase Repositorio, que inicializa las estructuras básicas del repositorio
    # - Crea un diccionario de ramas
    # - Define la rama actual, los archivos del repositorio y establece la rama principal por defecto
    def __init__(self):
        self.ramas = {} # Diccionario para almacenar las ramas por nombre
        self.rama_actual = None # Referencia a la rama en la que se está trabajando actualmente
        self.archivos = [] # Lista que contiene los archivos del área de preparación

        # Crear rama principal (main) como rama inicial del repositorio
        rama_principal = Rama("main")
        self.ramas["main"] = rama_principal
        self.rama_actual = rama_principal

    # Método que crea un commit en la rama actual con un mensaje específico y los archivos actuales
    def hacer_commit(self, mensaje):
        nuevo_commit = Commit(mensaje, self.archivos[:], self.rama_actual.ultimo_commit) # Crea un nuevo commit
        self.rama_actual.ultimo_commit = nuevo_commit # Actualiza el último commit en la rama actual
        print(f"Commit creado en la rama '{self.rama_actual.nombre}': {nuevo_commit}")

    # Método para crear una nueva rama con un nombre específico
    def crear_rama(self, nombre):
        if nombre in self.ramas:
            print(f"La rama '{nombre}' ya existe")
            return
        nueva_rama = Rama(nombre, self.rama_actual.ultimo_commit) # La nueva rama apunta al último commit de la rama actual
        self.ramas[nombre] = nueva_rama # Agrega la nueva rama al diccionario de ramas
        print(f"Rama creada: {nueva_rama}")

    # Método para cambiar a una rama existente por su nombre
    def cambiar_rama(self, nombre):
        if nombre not in self.ramas:
            print(f"La rama '{nombre}' no existe")
            return
        self.rama_actual = self.ramas[nombre] # Cambia la rama actual a la rama especificada
        print(f"Cambiado a la rama: {self.rama_actual}")

    # Método para fusionar otra rama con la rama actual
    def merge(self, nombre_rama_origen):
        if nombre_rama_origen not in self.ramas:
            print(f"La rama '{nombre_rama_origen}' no existe")
            return
        rama_origen = self.ramas[nombre_rama_origen]
        if not rama_origen.ultimo_commit:
            print(f"La rama '{nombre_rama_origen}' no tiene commits")
            return

        # Combina los archivos del último commit de la rama origen con los de la rama actual
        archivos_origen = rama_origen.ultimo_commit.archivos
        self.archivos.extend(archivos_origen) # Agrega los archivos fusionados al área de preparación

        # Crea un commit de merge que indica el origen de la fusión
        self.hacer_commit(f"Merge de '{nombre_rama_origen}' a '{self.rama_actual.nombre}'")

    # Método para mostrar el historial de commits en la rama actual
    def mostrar_historial(self):
        print(f"Historial de commits en la rama '{self.rama_actual.nombre}':")
        commit_actual = self.rama_actual.ultimo_commit # Inicia desde el último commit de la rama actual
        while commit_actual:
            print(commit_actual) # Muestra la información del commit
            commit_actual = commit_actual.anterior # Avanza al commit anterior
