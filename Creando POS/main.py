import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.title("POS Python")
width=ventana.winfo_screenwidth()/3.5
height=ventana.winfo_screenheight()/5.4
ventana.geometry("600x500+"+str(round(width))+"+"+str(round(height)))
ventana.configure(bg="#1e90ff")

global entry_cantidad

def registro():
    registrar = tk.Tk()
    registrar.title("Registar")
    registrar.geometry("400x142")
    trabajador = ttk.Label(registrar, text="Nombre de usuario: ", padding=10)
    casillero_trabajador = ttk.Entry(registrar, width=30)
    contrasena = ttk.Label(registrar, text="Contraseña: ", padding=10)
    casillero_contrasena = ttk.Entry(registrar, width=30,show="*")
    trabajador.grid(row=0, column=0, sticky="NSWE")
    casillero_trabajador.grid(row=0, column=1, sticky="NSWE")
    contrasena.grid(row=1, column=0, sticky="NSWE")
    casillero_contrasena.grid(row=1, column=1, sticky="NSWE")

    def validar_trabajador():
        global x_trabajador
        if (casillero_trabajador.get() == "Christian" and casillero_contrasena.get() == "trabajador1"):
            x_trabajador = "Es trabajador"
            messagebox.showinfo(registrar, "Trabajador validado")
            registrar.quit()
            registrar.destroy()
        else:
            messagebox.showinfo(registrar,"No es trabajador")
            registrar.quit()
            registrar.destroy()
            ventana.quit()
            ventana.destroy()

    validacion_datos = ttk.Button(registrar,text="Enviar",command=validar_trabajador)
    vacio = ttk.Label(registrar,text="        ")
    vacio.grid(row=2,column=0)
    validacion_datos.grid(row=3,column=0,sticky="NSWE",padx=12)
    registrar.mainloop()

def productos():
    if x_trabajador == "Es trabajador":
        productos_empresa = tk.Tk()
        productos_empresa.title("Productos")
        productos_empresa.geometry("500x400")
        productos_empresa.columnconfigure(0,weight=2)
        productos_empresa.columnconfigure(1,weight=2)
        lista_productos = ("telefonos","computadoras","televisores")
        cantidad = (5,8,9)

        fila = 0
        filas = 0

        for i in lista_productos:
            Texto_producto = ttk.Label(productos_empresa, text=i, justify=tk.CENTER)
            Texto_producto.grid(row=fila,column=0)
            fila+=1

        for i in cantidad:
            cantidad_producto = ttk.Label(productos_empresa, text=i, justify=tk.CENTER)
            cantidad_producto.grid(row=filas,column=1)
            filas+=1

def clientes():
    if x_trabajador == "Es trabajador":
        clientes_empresa = tk.Tk()
        clientes_empresa.title("Base de clientes de la empresa")
        clientes_empresa.geometry("500x400")
        clientes_empresa.columnconfigure(0,weight=2)
        clientes_empresa.columnconfigure(1,weight=2)
        nombres_clientes = ("Carlos", "Pedro", "Juan", "Hector", "Oscar", "Martha")
        cantidad_compras = (14, 15, 25, 10, 18, 16)

        clte = 0
        clte_compras = 0

        for i in nombres_clientes:
            usuario = ttk.Label(clientes_empresa, text=i,justify=tk.CENTER)
            usuario.grid(row=clte, column=0,sticky="NSWE")
            clte += 1

        for i in cantidad_compras:
            compra = ttk.Label(clientes_empresa, text=i,justify=tk.CENTER)
            compra.grid(row=clte_compras, column=1,sticky="NSWE")
            clte_compras += 1

        clientes_empresa.mainloop()

menu_principal = tk.Menu(ventana)
menu_principal.add_command(label="Iniciar sesión",command=registro)
menu_principal.add_command(label="Productos (Stock)",command=productos)
menu_principal.add_command(label="Clientes",command=clientes)

def facturacion():

    productos = {'telefono': 900, 'computadora': 2800, 'televisor': 3685}

    # Función que se ejecuta cuando se hace clic en el botón "Calcular"
    def calcular():
        # Obtener la cantidad de productos a comprar
        cantidad = int(entry_cantidad.get())

        # Inicializar una lista para almacenar los productos seleccionados
        seleccion = []

        # Pedir al usuario que ingrese los productos y agregarlos a la lista de selección
        for i in range(cantidad):
            producto = entry_productos[i].get()
            if producto in productos:
                seleccion.append(producto)

        # Imprimir los productos seleccionados y su precio
        text_resultado.delete('1.0', tk.END)
        text_resultado.insert(tk.END, 'Productos seleccionados:\n')
        total = 0
        for producto in seleccion:
            precio = productos[producto]
            text_resultado.insert(tk.END, f'{producto}: ${precio}\n')
            total += precio

        # Imprimir el precio total a pagar
        text_resultado.insert(tk.END, f'\nPrecio total a pagar: ${total}')

    # Crear la ventana principal y sus widgets
    ventana = tk.Tk()
    ventana.title('Calculadora de precios')
    label_cantidad = tk.Label(ventana, text='Cantidad de productos:')
    label_cantidad.grid(row=0, column=0)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.grid(row=0, column=1)
    boton_calcular = tk.Button(ventana, text='Calcular', command=calcular)
    boton_calcular.grid(row=0, column=2)
    label_productos = tk.Label(ventana, text='Ingrese los productos:')
    label_productos.grid(row=1, column=0)
    entry_productos = []
    for i in range(10):
        entry_producto = tk.Entry(ventana)
        entry_producto.grid(row=i + 2, column=0)
        entry_productos.append(entry_producto)
    text_resultado = tk.Text(ventana)
    text_resultado.grid(row=2, column=1, rowspan=10, columnspan=2)

def costo_unitario():
    un = 1
    pr = 1
    price = 1
    productos_empresa = ("telefono", "computadora", "TV")
    precio_producto = ("$ 900", "$ 2,800", "$ 3,685")
    title1 = ttk.Label(ventana,text="Cantidad")
    title1.grid(row=0,column=0,sticky="NSWE")
    title1 = ttk.Label(ventana, text="Productos")
    title1.grid(row=0, column=1, sticky="NSWE")
    title1 = ttk.Label(ventana, text="Precio de la unidad")
    title1.grid(row=0, column=2, sticky="NSWE")
    ventana.columnconfigure(0,weight=2)
    ventana.columnconfigure(1,weight=3)
    ventana.columnconfigure(2,weight=2)

    for i in productos_empresa:
        unidad_product = ttk.Label(ventana,text="1")
        unidad_product.grid(row=un,column=0,sticky="NSWE")
        un += 1

    for i in productos_empresa:
        mostrar = ttk.Label(ventana,text=i)
        mostrar.grid(row=pr,column=1,sticky="NSWE")
        pr +=1

    for i in precio_producto:
        presentar = ttk.Label(ventana,text=i)
        presentar.grid(row=price,column=2,sticky="NSWE")
        price += 1

def descuento():
    descuentos = tk.Tk()
    descuentos.title("Descuentos")
    descuentos.geometry("500x310")
    productos_rebajados = ("telefonos","computadora")
    rebaja = ("No hay descuento","No hay descuento")
    titulo_rebaja = ttk.Label(descuentos,text="Producto",justify=tk.CENTER)
    titulo_rebaja.grid(row=0,column=0)
    porcentaje_rebaja = ttk.Label(descuentos,text="Porcentaje de rebaja",justify=tk.CENTER)
    porcentaje_rebaja.grid(row=0,column=1)
    descuentos.columnconfigure(0,weight=2)
    descuentos.columnconfigure(1,weight=2)

    reb = 1
    porcent = 1

    for i in productos_rebajados:
        product_rebaja = ttk.Label(descuentos,text=i)
        product_rebaja.grid(row=reb,column=0)
        reb += 1

    for i in rebaja:
        porcentajes_descuento = ttk.Label(descuentos,text=i)
        porcentajes_descuento.grid(row=porcent,column=1)
        porcent += 1

    descuentos.geometry("500x300")
    descuentos.mainloop()

def reporte():
    vent=tk.Tk()
    vent.geometry("500x400")
    vent.title("Reporte de Ventas")
    title_mensaje=ttk.Label(vent,text="Próximamente disponible :)")
    title_mensaje.grid(row=0,column=1)
    vent.configure(bg="#08EE85")

def validacion():
    if validar_supervisor.get() == "Oscar":
        if validar_cargo.get() == "Ingeniero de planta":
            if validar_contraseña_supervisor.get() == "ING9413":
                datos_nuevo_trabajador = tk.Tk()
                datos_nuevo_trabajador.geometry("600x320")
                datos_nuevo_trabajador.title("Agregar datos del nuevo trabajador")
                title_nombre = ttk.Label(datos_nuevo_trabajador, text="Ingrese el nombre del nuevo trabajador")
                title_nombre.grid(row=0, column=0)
                nombre_nuevo_usuario = ttk.Entry(datos_nuevo_trabajador, width=20)
                nombre_nuevo_usuario.grid(row=0, column=1)
                title_cargo = ttk.Label(datos_nuevo_trabajador, text="Ingrese el cargo")
                title_cargo.grid(row=1, column=0)
                cargo_asignado = ttk.Entry(datos_nuevo_trabajador, width=20)
                cargo_asignado.grid(row=1, column=1)
                title_contraseña = ttk.Label(datos_nuevo_trabajador, text="Contraseña nuevo trabajador")
                title_contraseña.grid(row=2, column=0)
                contraseña_nueva = ttk.Entry(datos_nuevo_trabajador, width=20, show="●")
                contraseña_nueva.grid(row=2, column=1)

                def sms_registrado():
                    messagebox.showinfo(datos_nuevo_trabajador, "Registro exitoso")

                btn_final = ttk.Button(datos_nuevo_trabajador, text="Registrar", command=sms_registrado)
                btn_final.grid(row=3, column=0)

def nuevo_trabajador():
    global validar_supervisor
    global validar_cargo
    global validar_contraseña_supervisor

    if x_trabajador == "Es trabajador":
        ventana_trabajador = tk.Tk()
        ventana_trabajador.geometry("500x320")
        ventana_trabajador.title("Validar datos del superior/jefe")
        superior = ttk.Label(ventana_trabajador, text="Ingrese datos del superior/jefe")
        superior.grid(row=0, column=0)
        nombre_superior = ttk.Label(ventana_trabajador, text="Ingrese el nombre del superior")
        nombre_superior.grid(row=1, column=0)
        validar_supervisor = ttk.Entry(ventana_trabajador,width=20)
        validar_supervisor.grid(row=2,column=0)
        cargo_superior = ttk.Label(ventana_trabajador, text="Ingrese el cargo que desempeña")
        cargo_superior.grid(row=3, column=0)
        validar_cargo = ttk.Entry(ventana_trabajador,width=20)
        validar_cargo.grid(row=4,column=0)
        contraseña_superior = ttk.Label(ventana_trabajador, text="Ingrese la contraseña asignada")
        contraseña_superior.grid(row=5, column=0)
        validar_contraseña_supervisor = ttk.Entry(ventana_trabajador,width=20,show="●")
        validar_contraseña_supervisor.grid(row=6,column=0)
        btn_envio_ = ttk.Button(ventana_trabajador, text="Validar datos", command=validacion)
        btn_envio_.grid(row=8, column=0)


submenu = tk.Menu(menu_principal, tearoff=0)
submenu.add_command(label="Sistema de Facturación",command=facturacion)
submenu.add_command(label="Costo unitario de productos",command=costo_unitario)
submenu.add_command(label="Descuentos",command=descuento)
submenu.add_command(label="Reporte de ventas e inventario",command=reporte)
submenu.add_command(label="Agregar nuevo trabajador",command=nuevo_trabajador)

menu_principal.add_cascade(label="Centro de Operaciones",menu=submenu)

ventana.config(menu=menu_principal)
ventana.mainloop()