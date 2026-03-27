from agregar import inventario

def estadisticas():
    if len(inventario["nombre"]) == 0:
        print("El inventario esta vacio")
        return

    unidades_totales = sum(inventario["cantidad"])

    valor_total = sum(inventario["precio"][i] * inventario["cantidad"][i] 
                        for i in range(len(inventario["nombre"])))

    indice_mas_caro = inventario["precio"].index(max(inventario["precio"]))
    producto_mas_caro = inventario["nombre"][indice_mas_caro]
    precio_mas_caro = inventario["precio"][indice_mas_caro]

    indice_mayor_stock = inventario["cantidad"].index(max(inventario["cantidad"]))
    producto_mayor_stock = inventario["nombre"][indice_mayor_stock]
    cantidad_mayor_stock = inventario["cantidad"][indice_mayor_stock]

    print("\n---ESTADISTICAS---")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total: {valor_total}")
    print(f"El producto mas caro: {producto_mas_caro} - Precio: {precio_mas_caro}")
    print(f"El producto con mayor stock: {producto_mayor_stock} - Cantidad: {cantidad_mayor_stock}")
    print("------------------\n")