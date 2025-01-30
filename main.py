from Repositorio import Repositorio
from Repositorio import Archivo

def main():
    # Inicializar el repositorio
    repo = Repositorio()

    # Agregar archivos
    repo.archivos.append(Archivo("archivo1.txt", "Contenido del archivo 1"))
    repo.hacer_commit("Initial commit")

    # Crear una nueva rama y trabajar en ella
    repo.crear_rama("develop")
    repo.cambiar_rama("develop")
    repo.archivos.append(Archivo("archivo2.txt", "Contenido del archivo 2"))
    repo.hacer_commit("Added new feature")

    # Cambiar a la rama principal y hacer un merge
    repo.cambiar_rama("main")
    repo.merge("develop")

    # Mostrar el historial de commits
    repo.mostrar_historial()

if __name__ == "__main__":
    main()
