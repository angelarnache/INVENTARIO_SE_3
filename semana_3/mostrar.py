from agregar import inventario

def mostrar_inventario():
    if len(inventario["nombre"])==0:
        print ("el inventario esta vacio")
    else:
        print("\n---inventario---")
        for i in range(len(inventario["nombre"])):
            print(f"Producto {i+1}:")
            print(f"  Nombre: {inventario['nombre'][i]}")
            print(f"  Precio: {inventario['precio'][i]}")
            print(f"  Cantidad: {inventario['cantidad'][i]}")
        print("----------------\n")
