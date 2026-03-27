from agregar import inventario

condicion="false"
def eliminar_producto():
    if len(inventario["nombre"])==0:
        print("el inventario esta vacio")
        return
    
    print("\n---inventario--")
    for i in range(len(inventario["nombre"])):
        print(f"{i+1}.{inventario["nombre"]}[i] -precio:{inventario["precio"][i]} -cantidad {inventario["cantidad"][i]}")
        print("--------------\n")
    while condicion == "false":
        try:
            indice = int(input("Digite el numero del producto a eliminar: ")) - 1
            if 0 <= indice < len(inventario["nombre"]):
                break
            else:
                print("Numero invalido, intente de nuevo")
        except ValueError:
            print("Opcion invalida, digite un numero")
    nombre=inventario["nombre"][indice]
    while condicion == "false":
        confirmar = input(f"Esta seguro que desea eliminar '{nombre}'? si/no: ").lower()
        if confirmar == "si" or confirmar == "s":
            inventario["nombre"].pop(indice)
            inventario["precio"].pop(indice)
            inventario["cantidad"].pop(indice)
            print(f"El producto '{nombre}' se elimino correctamente\n")
            break
        elif confirmar == "no" or confirmar == "n":
            print("Eliminacion cancelada\n")
            break
        else:
            print("Opcion invalida, intente de nuevo")