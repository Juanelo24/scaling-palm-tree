# Ingreso de datos
# Preguntar que tipo de despensa se va a realizar
print("Bienvenido, elige la opción que realizaras a continuación")
print("1.- Elaboración despensa de abarrotes")
print("2.- Elaboración despensa de vegetales")
Elección1 = float(input('Ingrese el número de su elección: '))
Elección = int(Elección1)
#Pregunta el numero de despensas a realizar
Número_despensas = float(input('Escriba el número de despensas a realizar :'))
ND = Número_despensas

# Tabla de base de datos
import pandas as pd
ruta = r'C:/Users/juant/OneDrive/Escritorio/Ejemplo base de datos.xlsx' #Ruta del excel
df = pd.read_excel(ruta, 'Sheet1')
npu = df['Peso por unidad (g)']/1000 #pasar los gramos a kg
CP = df['Cantidad (kg)']/npu #divide el peso existente de producto que hay entre el peso por unidad para determinar la cantidad de producto
df["Cantidad de producto"] = CP 

#Abarrotes
if Elección == 1: #acciones que hará si escoge la opción de abarrotes

    np = 6; it = int(np) #número de productos

    #Elimina los que son vegetales y menores al número de despensas
    df.drop(df[(df['Categoría'] == "Vegetales")].index, inplace=True); df.drop(df[(df['Cantidad de producto'] < ND)].index, inplace=True)

    de = df.sort_values(by=["Fecha"]) #ordena los valores de columna fecha 
    list_of_products = de["Producto"].tolist(); list_of_cantidad = de["Cantidad (kg)"].tolist(); list_of_fecha = de["Fecha"].tolist(); list_of_almacenamiento = de["Almacenamiento"].tolist(); list_of_cantidadp = de["Cantidad de producto"].tolist(); list_of_pesouni = de["Peso por unidad (g)"].tolist()
    productos_elegidos = []; cantidad_elegidos = []; fecha_elegidos = []; almacenamiento_elegidos = []; cantidadp_elegidos = []; pesouni_elegidos = [] #Lista para los nuevos productos elegidos

    for m in range(it):
        productos_elegidos.append(list_of_products[m])
        cantidad_elegidos.append(list_of_cantidad[m])
        fecha_elegidos.append(list_of_fecha[m])
        almacenamiento_elegidos.append(list_of_almacenamiento[m])
        cantidadp_elegidos.append(list_of_cantidadp[m])
        pesouni_elegidos.append(list_of_pesouni[m])

    #junta la nueva fila de productos en una nueva variable
    tabla1 = pd.DataFrame((zip(productos_elegidos, cantidad_elegidos,fecha_elegidos,almacenamiento_elegidos,pesouni_elegidos,cantidadp_elegidos)), columns=["Producto", "Cantidad (kg)","Fecha","Almacenamiento","Peso por unidad (g)","Cantidad de producto"])
    producto_por_despensa = [] #nueva lista

    for fila in tabla1["Cantidad de producto"]:
        if fila/5 >= ND:
            pd1 = 5
        elif fila/4 >= ND:
            pd1 = 4
        elif fila/3 >= ND:
            pd1 = 3
        elif fila/2 >= ND:
            pd1 = 2
        elif fila/2 <= ND:
            pd1 = 1    
        producto_por_despensa.append(pd1)

    tabla1["Producto por despensa"] = producto_por_despensa
    tabla_final = pd.DataFrame((zip(productos_elegidos,producto_por_despensa)), columns = ["Producto", "Producto por despensa"])

    cantidadpro_usado = tabla1["Producto por despensa"]*ND
    cantidadpro_new = tabla1["Cantidad de producto"]-cantidadpro_usado
    tabla1["Cantidad de producto"] = cantidadpro_new
    npu1 = tabla1['Peso por unidad (g)']/1000
    tabla1['Cantidad (kg)'] = tabla1["Cantidad de producto"]*npu1
    l = []
    completa = []
    list_of_products_1 = tabla1["Producto"].tolist(); list_of_cantidad_1 = tabla1["Cantidad (kg)"].tolist(); list_of_fecha_1 = tabla1["Fecha"].tolist(); list_of_almacenamiento_1 = tabla1["Almacenamiento"].tolist(); list_of_cantidadp_1 = tabla1["Cantidad de producto"].tolist(); list_of_pesouni_1 = tabla1["Peso por unidad (g)"].tolist()
    productos_elegidos_1 = []; cantidad_elegidos_1 = []; fecha_elegidos_1 = []; almacenamiento_elegidos_1 = []; cantidadp_elegidos_1 = []; pesouni_elegidos_1 = []
    
    for m in range(it):
        productos_elegidos_1.append(list_of_products_1[m])
        cantidad_elegidos_1.append(list_of_cantidad_1[m])
        fecha_elegidos_1.append(list_of_fecha_1[m])
        almacenamiento_elegidos_1.append(list_of_almacenamiento_1[m])
        cantidadp_elegidos_1.append(list_of_cantidadp_1[m])
        pesouni_elegidos_1.append(list_of_pesouni_1[m])
    
    for i in range(it):
        l.append("Abarrotes")
        l.append(productos_elegidos_1[i])
        l.append(cantidad_elegidos_1[i])
        l.append(fecha_elegidos_1[i])
        l.append(0)
        l.append(almacenamiento_elegidos_1[i])
        l.append(pesouni_elegidos_1[i])
        completa.append(l)
        l = []
    
    #elimina los productos que fueron utilizados para la despensa
    import pandas as pd
    filas_eliminar = []
    ejemplo = pd.read_excel(ruta, 'Sheet1')
    z = 0

    for fila in ejemplo['Producto']:
        for m in productos_elegidos:
            if m == fila:
                filas_eliminar.append(z)
        z = z+1

    for n in range(it):
        data = completa[n]
        ejemplo.loc[len(ejemplo)] = data

    cantidades_finales_1 = ejemplo["Cantidad (kg)"].tolist()
    w = 0

    for t in cantidades_finales_1:
        if t == 0:
            ejemplo.drop([w], axis=0, inplace=True)
        w=w+1

    for i in filas_eliminar:
        ejemplo.drop([i], axis=0, inplace=True)

#Accion que va a realizar si escoge verduras
elif Elección == 2:

    #Pregunta si desea una despensa pequeña o grande
    print("1.- Despensa pequeña")
    print("2.- Despensa grande")
    tipo_de_despensas = float(input('Escriba el tipo de despensa que se va a realizar'))
    tdp = tipo_de_despensas
    df.drop(df[(df['Categoría'] == "Abarrotes")].index, inplace=True)
    de = df.sort_values(by=["Prioridad"])
    producto = []; producto_p1 = []; producto_p2 = []; producto_p3 = []; producto_p4 = []; producto_p5 = []
    cantidades = []; cantidades_p1 = []; cantidades_p2 = []; cantidades_p3 = []; cantidades_p4 = []; cantidades_p5 = []
    prioridad = []; prioridad_p1 = [];  prioridad_p2 = [];   prioridad_p3 = [];   prioridad_p4 = []; prioridad_p5 = []
    almacenamiento = []; almacenamiento_p1 = []; almacenamiento_p2 = []; almacenamiento_p3 = []; almacenamiento_p4 = []; almacenamiento_p5 = []
    x=0
    for fila in de['Producto']:
        producto.append(fila)
    for fila in de['Cantidad (kg)']:
        cantidades.append(fila)
    for fila in de['Prioridad']:
        prioridad.append(fila)
    for fila in de['Almacenamiento']:
        almacenamiento.append(fila)
    for fila in de['Prioridad']:
        if fila == 1:
            producto_p1.append(producto[x])
            cantidades_p1.append(cantidades[x])
            prioridad_p1.append(prioridad[x])
            almacenamiento_p1.append(almacenamiento[x])
        elif fila == 2:
            producto_p2.append(producto[x])
            cantidades_p2.append(cantidades[x])
            prioridad_p2.append(prioridad[x])
            almacenamiento_p2.append(almacenamiento[x])
        elif fila == 3:
            producto_p3.append(producto[x])
            cantidades_p3.append(cantidades[x])
            prioridad_p3.append(prioridad[x])
            almacenamiento_p3.append(almacenamiento[x])
        elif fila == 4:
            producto_p4.append(producto[x])
            cantidades_p4.append(cantidades[x])
            prioridad_p4.append(prioridad[x])
            almacenamiento_p4.append(almacenamiento[x])
        elif fila == 4:
            producto_p4.append(producto[x])
            cantidades_p4.append(cantidades[x])
            prioridad_p4.append(prioridad[x])
            almacenamiento_p4.append(almacenamiento[x])
        x=x+1

    tabla1 = pd.DataFrame((zip(producto_p1, cantidades_p1,prioridad_p1,almacenamiento_p1)), columns=["Producto", "Cantidad (kg)","Prioridad","Almacenamiento"]) 
    tabla_prioridad1 = tabla1.sort_values(by=["Cantidad (kg)"], ascending=True)
    tabla2 = pd.DataFrame((zip(producto_p2, cantidades_p2,prioridad_p2,almacenamiento_p2)), columns=["Producto", "Cantidad (kg)","Prioridad","Almacenamiento"]) 
    tabla_prioridad2 = tabla2.sort_values(by=["Cantidad (kg)"], ascending=True)
    tabla3 = pd.DataFrame((zip(producto_p3, cantidades_p3,prioridad_p3,almacenamiento_p3)), columns=["Producto", "Cantidad (kg)","Prioridad","Almacenamiento"]) 
    tabla_prioridad3 = tabla3.sort_values(by=["Cantidad (kg)"], ascending=True)
    tabla4 = pd.DataFrame((zip(producto_p4, cantidades_p4,prioridad_p4,almacenamiento_p4)), columns=["Producto", "Cantidad (kg)","Prioridad","Almacenamiento"]) 
    tabla_prioridad4 = tabla4.sort_values(by=["Cantidad (kg)"], ascending=True)
    tabla5 = pd.DataFrame((zip(producto_p5, cantidades_p5,prioridad_p5,almacenamiento_p5)), columns=["Producto", "Cantidad (kg)","Prioridad","Almacenamiento"]) 
    tabla_prioridad5 = tabla5.sort_values(by=["Cantidad (kg)"], ascending=True)
    tabla_prioridades = pd.concat([tabla_prioridad1, tabla_prioridad2, tabla_prioridad3, tabla_prioridad4, tabla_prioridad5], axis=0)
    kilo_por_producto = []
    kpd1 = 7; kpd2 = 14
    x1 = 0; x2 = 0

    if tdp == 1:
        for t in tabla_prioridades['Cantidad (kg)']:
            b = t//ND
            if b >= 1:
                x1_1 = x1 + b
                if x1_1 < 7:
                    kilo_por_producto.append(b)
                    x1 = x1 + b
                elif x1_1 >= 7:
                    e = 7 - x1
                    kilo_por_producto.append(e)
                    x1 = x1 + e
            else:
                kilo_por_producto.append(0)

    if tdp == 2:
        for t in tabla_prioridades['Cantidad (kg)']:
            b = t//ND
            if b >= 1:
                x1_1 = x1 + b
                if x1_1 < 14:
                    kilo_por_producto.append(b)
                    x1 = x1 + b
                elif x1_1 >= 14:
                    e = 14 - x1
                    kilo_por_producto.append(e)
                    x1 = x1 + e
            else:
                kilo_por_producto.append(0)

    tabla_prioridades["Kilo por producto"]=kilo_por_producto
    tabla_final = pd.DataFrame((zip(tabla_prioridades["Producto"],tabla_prioridades["Kilo por producto"])), columns=["Producto", "Kilos por producto"]) 
    tabla_final["Unidad"]="Kg"
    w = 0; d = 0
    for t in tabla_final["Kilos por producto"]:
            if t == 0:
                tabla_final.drop([w],axis=0, inplace=True)
            w=w+1
    for t in tabla_final["Kilos por producto"]:
        d = d+1
    cantidadpro_usado = tabla_prioridades["Kilo por producto"]*ND
    cantidadpro_new = tabla_prioridades["Cantidad (kg)"]-cantidadpro_usado
    tabla_prioridades["Cantidad (kg)"] = cantidadpro_new
    l = []
    completa = []
    list_of_products_elegidos = tabla_final["Producto"].tolist()
    list_of_products_1 = tabla_prioridades["Producto"].tolist(); list_of_cantidad_1 = tabla_prioridades["Cantidad (kg)"].tolist(); list_of_prioridad_1 = tabla_prioridades["Prioridad"].tolist(); list_of_almacenamiento_1 = tabla_prioridades["Almacenamiento"].tolist()
    productos_elegidos_1 = []; cantidad_elegidos_1 = []; prioridad_elegidos_1 = []; almacenamiento_elegidos_1 = []; cantidadp_elegidos_1 = []
    
    for m in range(d):
        productos_elegidos_1.append(list_of_products_1[m])
        cantidad_elegidos_1.append(list_of_cantidad_1[m])
        prioridad_elegidos_1.append(list_of_prioridad_1[m])
        almacenamiento_elegidos_1.append(list_of_almacenamiento_1[m])
    
    for i in range(d):
        l.append("Vegetales")
        l.append(productos_elegidos_1[i])
        l.append(cantidad_elegidos_1[i])
        l.append(0)
        l.append(prioridad_elegidos_1[i])
        l.append(almacenamiento_elegidos_1[i])
        l.append(0)
        completa.append(l)
        l = []

    #elimina los productos que fueron utilizados para la despensa
    import pandas as pd
    filas_eliminar = []
    ejemplo = pd.read_excel(ruta, 'Sheet1')
    z = 0

    for fila in ejemplo['Producto']:
        for m in list_of_products_elegidos:
            if m == fila:
                filas_eliminar.append(z)
        z = z+1

    for n in range(d):
        data = completa[n]
        ejemplo.loc[len(ejemplo)] = data

    cantidades_finales_1 = ejemplo["Cantidad (kg)"].tolist()
    w = 0

    for t in cantidades_finales_1:
        if t == 0:
            ejemplo.drop([w],axis=0, inplace=True)
        w=w+1

    for i in filas_eliminar:
        ejemplo.drop([i], axis=0, inplace=True)

print(tabla_final)



