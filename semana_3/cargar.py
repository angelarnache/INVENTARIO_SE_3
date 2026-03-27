from agregar import inventario
import csv

def cargar_inventario():
    try:
        with open('inventario.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            filas = list(reader)

        if len(inventario["nombre"]) > 0:
            print("Ya existe un inventario cargado.")
            print("¿Qué deseas hacer?")
            print("1. Sobreescribir")
            print("2. Fusionar")
            opcion = input("Elige una opción (1/2): ").strip()

            if opcion == "1":
                for clave in inventario:
                    inventario[clave] = []
                print("Inventario sobreescrito.")

            elif opcion == "2":
                print("Fusionando con el inventario actual...")

            else:
                print("Opción no válida. Operación cancelada.")
                return
        
        for fila in filas:
            for clave in inventario:
                inventario[clave].append(fila[clave])

        print("Inventario cargado correctamente.")

    except FileNotFoundError:
        print("No se encontró el archivo inventario.csv")

    except KeyError as e:
        print(f"Error: la columna {e} no existe en el CSV")