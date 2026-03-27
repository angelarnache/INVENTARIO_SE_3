from agregar import agregar_producto
from mostrar import mostrar_inventario
from buscar import buscar_producto
from actualizar import actualizar_producto
from eliminar import eliminar_producto
from estadistica import estadisticas

opciones =["1 agregar","2 mostrar","3 buscar","4 actualizar","5 eliminar","6 estadisticas","7 guardar CVS","8 cargar CSV","9 salir"]

condicion="false"
while condicion == "false":
    print("------bienvenido-------")
    print("---inventario celeste--")
    for opcion in opciones:
        print(opcion)

    try:
        usuario=int(input("digite un numero de la lista: "))
        if 1 <= usuario <= 9:
            if usuario == 1:
                print("---agregar producto---")
                agregar_producto()
            elif usuario == 2:
                mostrar_inventario()
            elif usuario == 3:
                print("--buscar_producto--")
                buscar_producto()
            elif usuario == 4:
                actualizar_producto()
            elif usuario == 5:
                eliminar_producto()
            elif usuario == 6:
                estadisticas()

            elif usuario == 9:
                print("hasta luego")
                break

        else:
            print("el numero no esta en la lista intente de nuevo")
    except ValueError:
        print("opcion invalida intente con numeros que esten en la lista")
  
