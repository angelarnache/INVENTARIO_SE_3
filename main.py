from agregar import agregar_producto

print("------bienvenido-------")
print("---inventario celeste--")

opciones =["1 agregar","2 mostrar","3 buscar","4 actualizar","5 eliminar","6 estadisticas","7 guardar CVS","8 cargar CSV","9 salir"]

condicion="false"
while condicion == "false":
    for opcion in opciones:
        print(opcion)

    try:
        usuario=int(input("digite un numero de la lista: "))
        if 1 <= usuario <= 9:
            if usuario == 1:
                print("estas en agregar producto")
                agregar_producto()

            elif usuario == 9:
                print("hasta luego")
                break

        else:
            print("el numero no esta en la lista intente de nuevo")
    except ValueError:
        print("opcion invalida intente con numeros que esten en la lista")
  
