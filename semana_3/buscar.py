from agregar import inventario

def buscar_producto():
    condicion="false"
    while condicion == "false":
        opcion = input("Digite el nombre del producto a buscar: ")
        if opcion.isalpha():
            break
        else:
            print("Opcion invalida, intente de nuevo")

    if opcion in inventario["nombre"]:
        indice = inventario["nombre"].index(opcion)
        print("\n---PRODUCTO ENCONTRADO---")
        print(f"Nombre: {inventario['nombre'][indice]}")
        print(f"Precio: {inventario['precio'][indice]}")
        print(f"Cantidad: {inventario['cantidad'][indice]}")
        print("-------------------------\n")
    else:
        print(f"El producto {opcion} no existe en el inventario")
