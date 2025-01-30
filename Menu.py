# Importaciones necesarias para el programa principal
from Repositorio import Repositorio  # Importa la clase Repositorio desde repositorio.py
from Repositorio import Archivo # Importa la clase Archivo desde Repositorio.py

# Función principal del programa, que permite interactuar con el sistema Git simplificado
def main():
    # Crear una instancia del repositorio, representando el sistema Git simplificado
    repo = Repositorio()

    while True:
        # Menú principal para que el usuario seleccione opciones
        print("\n=== Sistema Git Simplificado ===")
        print("1. Agregar archivo")  # Opción para agregar un archivo al repositorio
        print("2. Hacer commit")  # Opción para realizar un commit
        print("3. Crear rama")  # Opción para crear una nueva rama
        print("4. Cambiar rama")  # Opción para cambiar entre ramas
        print("5. Fusionar ramas")  # Opción para fusionar una rama con la rama actual
        print("6. Mostrar historial de commits")  # Opción para mostrar el historial de commits
        print("7. Salir")  # Opción para salir del sistema

        # Solicitar entrada del usuario
        opcion = input("Selecciona una opción: ")

        # Agregar un archivo al repositorio
        if opcion == "1":
            nombre = input("Nombre del archivo: ")  # Nombre del archivo
            contenido = input("Contenido del archivo: ")  # Contenido del archivo
            repo.archivos.append(Archivo(nombre, contenido))  # Se agrega el archivo a la lista de archivos del repositorio
            print(f"Archivo '{nombre}' agregado.")

        # Realizar un commit
        elif opcion == "2":
            mensaje = input("Mensaje del commit: ")  # Mensaje del commit
            repo.hacer_commit(mensaje)  # Se realiza un commit con el mensaje proporcionado

        # Crear una nueva rama
        elif opcion == "3":
            nombre_rama = input("Nombre de la nueva rama: ")  # Nombre de la nueva rama
            repo.crear_rama(nombre_rama)  # Se crea la nueva rama

        # Cambiar a otra rama
        elif opcion == "4":
            nombre_rama = input("Nombre de la rama a cambiar: ")  # Nombre de la rama a la que se desea cambiar
            repo.cambiar_rama(nombre_rama)  # Cambia a la rama especificada

        # Fusionar una rama con la rama actual
        elif opcion == "5":
            nombre_rama = input("Nombre de la rama a fusionar con la rama actual: ")  # Nombre de la rama a fusionar
            repo.merge(nombre_rama)  # Realiza la fusión

        # Mostrar el historial de commits
        elif opcion == "6":
            repo.mostrar_historial()  # Muestra el historial de commits de la rama actual

        # Salir del programa
        elif opcion == "7":
            print("Saliendo del sistema Git.")  # Mensaje de despedida
            break  # Termina el bucle while para salir del programa

        # Opción no válida
        else:
            print("Opción no válida. Intenta de nuevo.")  # Mensaje de error para opciones no reconocidas

# Ejecutar la función principal cuando el archivo se ejecute directamente
if __name__ == "__main__":
    main()
