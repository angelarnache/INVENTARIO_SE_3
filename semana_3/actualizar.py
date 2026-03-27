from agregar import inventario

condicion="false"
def actualizar_producto():
    if len(inventario["nombre"]) == 0:
        print("El inventario esta vacio")
        return

    print("\n---INVENTARIO---")
    for i in range(len(inventario["nombre"])):
        print(f"{i+1}. {inventario['nombre'][i]} - Precio: {inventario['precio'][i]} - Cantidad: {inventario['cantidad'][i]}")
    print("----------------\n")

    while condicion == "false":
        try:
            indice = int(input("Digite el numero del producto a actualizar: ")) - 1
            if 0 <= indice < len(inventario["nombre"]):
                break
            else:
                print("Numero invalido, intente de nuevo")
        except ValueError:
            print("Opcion invalida, digite un numero")

    print(f"\nProducto seleccionado: {inventario['nombre'][indice]}")
    print("(Si no desea cambiar una opcion, presiona Enter)\n")

    nuevo_nombre = input(f"Nombre actual '{inventario['nombre'][indice]}', nuevo nombre: ")
    if nuevo_nombre.strip() == "":
        pass
    elif nuevo_nombre.isalpha():
        inventario["nombre"][indice] = nuevo_nombre
    else:
        print("Nombre invalido, se deja igual")

    nuevo_precio = input(f"Precio actual '{inventario['precio'][indice]}', nuevo precio: ")
    if nuevo_precio.strip() == "":
        pass
    else:
        try:
            inventario["precio"][indice] = float(nuevo_precio)
        except ValueError:
            print("Precio invalido, se deja igual")
            
    nueva_cantidad = input(f"Cantidad actual '{inventario['cantidad'][indice]}', nueva cantidad: ")
    if nueva_cantidad.strip() == "":
        pass
    else:
        try:
            inventario["cantidad"][indice] = int(nueva_cantidad)
        except ValueError:
            print("Cantidad invalida, se deja igual")

    print(f"\nProducto actualizado:")
    print(f"  Nombre: {inventario['nombre'][indice]}")
    print(f"  Precio: {inventario['precio'][indice]}")
    print(f"  Cantidad: {inventario['cantidad'][indice]}\n")