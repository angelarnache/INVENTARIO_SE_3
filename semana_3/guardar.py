from agregar import inventario
import csv


def guardar_inventario():
    if len(inventario["nombre"])==0:
        print ("el inventario esta vacio")
        return

    with open('inventario.csv','w',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(inventario.keys())

        for i in range(len(inventario["nombre"])):
            fila=[inventario[clave][i] for clave in inventario]
            writer.writerow(fila)

    print("inventaro guardado con exito en inventario.csv")