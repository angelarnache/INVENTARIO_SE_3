inventario={"nombre":[], 
            "precio":[],
            "cantidad":[]}

def agregar_producto():
    condicion = "false"
    while condicion == "false":
        while condicion == "false":
            opcion = input("Digite el nombre del producto: ")
            if opcion.isalpha():
                print("guardado")
                inventario["nombre"].append(opcion)
                break
            else:
                print("Opcion invalida, intente de nuevo")

        while condicion == "false":
            try:
                opcion_2=float(input("digite el precio: "))
                inventario["precio"].append(opcion_2)
                print("guardado")
                break
            except ValueError:
                print("opcion invalida,digite un numero")
                continue

        while condicion == "false":
            try:
                opcion_3=int(input("digite la cantidad: "))
                inventario["cantidad"].append(opcion_3)
                print("guardado")
                break
            except ValueError:
                print("opcion invalida,digite un numero")
                continue
        
        opcion_4 = input("Deseas agregar mas productos? si/no: ").lower()
        if opcion_4 == "si" or opcion_4 == "s":
            continue
        elif opcion_4 == "no" or opcion_4 == "n":
            return  
        else:
            print("Opcion invalida, intente de nuevo")
