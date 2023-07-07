
'''BIENVENIDO PODRA INGRESAR CON EL 
USUARIO=JUAN
CONTRASEÑA=1234'''



import gestion
import os
import getpass4


dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)
#Para llamar Menú de Usuario        
def menu_Usuario():
 while True:
  gestion.decorar(2)
  print("""

            :::Menú:::
          ::::Usuario::::

        [1] - Gestión de Productos 
        [2] - Reportes 
        [0] - Salir
         """)
  opcionUsuario=gestion.inputEntero("Ingrese una opción: ")
  if opcionUsuario==1:
    menuGestion()
  elif opcionUsuario==2:
    menuReportes()  
  elif opcionUsuario==0:
    gestion.decorar(2)
    print("¡Gracias por utilizar la app del Grupo A!!-PS D:\CodoACodo> Grupo A")
    exit()   
  else:
    gestion.decorar(2)
    print("Opción inválida. Intente de nuevo")

def menuGestion():
    while True:
      print("""

              :::Menú:::
            ::::Gestión::::

        [1] - Ingresar nuevo producto 
        [2] - Modificar un producto 
        [3] - Eliminar un producto   
        [4] - Ver inventario
        [0] - Volver al menú principal
        """)
      opcionGestion=gestion.inputEntero("Ingrese una opción: ")
      if opcionGestion==1:
        gestion.decorar(2)
        print("A G R E G A R  P R O D U C T O".center(40,))
        gestion.ingresarNuevoProducto()
        gestion.decorar(2)
      elif opcionGestion==2:
        gestion.decorar(2)
        print("M O D I F I C A R   P R O D U C T O".center(40,))
        gestion.modificarProducto()
        gestion.decorar(2)
      elif opcionGestion==3:
        gestion.decorar(2)
        print("E L I M I N A R  P R O D U C T O".center(40,))
        gestion.eliminarProducto()
        gestion.decorar(2)
      elif opcionGestion==4:
        gestion.decorar(2)
        print("V E R  I N V E N T A R I O".center(40,))
        gestion.verInventario()
        gestion.decorar(2)
      elif opcionGestion==0:    
         break
      else:
        print("Ingresá una opción válida![0-5]")
        gestion.decorar(2)

def menuCategorias():
  while True:
    print("""
          CATEGORIAS:
          [1]  Accesorios para el Hogar
          [2]  Contruccion
          [3]  Cerradura y Seguridad
          [4]  Ferreteria y jardin
          [5]  Electricidad
          [6]  Fontaneria
          [7]  Pintura y Accesorios
          [8]  Material de fijacion
          [9]  Equipos de Seguridad
          [10] Herramientas Electricas
          [11] Herramientas Manuales
          [0] Salir
          """)
    entero=gestion.inputEntero("Ingrese la categoria que desea buscar: ")
    if entero ==0:
      break
    elif entero >=1 and entero <=11:
      catBuscada=gestion.categoriasXNro(entero)
      gestion.verProductoPor("categoria",catBuscada)
    else:
      print("Ingrese una opción válida")

def menuReportes():
  while True:
    gestion.decorar(2)
    print("""

               :::Menú:::
            ::::Reportes::::
           
            [1] Mostrar productos nacionales
            [2] Mostrar productos importados
            [3] Mostrar productos con stock limitado
            [4] Mostrar productos sin stock
            [5] Mostrar productos por categoria
            [0] Volver al menú principal
            """)
    opcionReportes=gestion.inputEntero("Ingrese una opción: ")
    if opcionReportes==0:
      break
    elif opcionReportes==1:
      gestion.verProductoPor("nacional",True)
    elif opcionReportes==2:
      gestion.verProductoPor("nacional",False)
    elif opcionReportes==3:
      gestion.stockLim()
    elif opcionReportes==4:
      gestion.verProductoPor("cantidad",0)
    elif opcionReportes==5:
      menuCategorias()
    else:
      print("Ingrese una opción válida [0-5]")
      gestion.decorar(2)

def menu_Cliente(): 
  import random
  while True:
    gestion.decorar(2)
    print('''

              :::Menú:::
          :::::Clientes:::::

      [1] - Ver producto y stock
      [2] - Generar una compra
      [0] - Salir''')
    opcion=gestion.inputEntero("Ingrese una opción: ")
    if opcion==0:
      break
    elif opcion==1:
      print("Ver que puedo comprar")
      repuesto=input("ingrese el nombre del producto que necesita: ")
      print("Contamos con stock continue para realizar su compra")
      print("por favor proceda a consultar las diferentes formas de pago!!")
    elif opcion==2:
      mercaderia=input("ingrese el nombre de el producto que necesita: ")
      cantidad=input("ingrese cantidad de producto que necesita: ")
      valor=random.randint(3000,12000)
      valor=round(valor)
      print("su compra de ",cantidad,mercaderia," tiene un  valor total de" ,valor," pesos, a continuación le brindaremos las diferentes formas de pagos. ")
      while True:
        gestion.decorar(2)
        print("""

                  :::METODOS:::
                 ::::DE PAGO::::

              [1] - EFECTIVO
              [2] - 3 CUOTAS SIN INTERES 
              [3] - 12 CUOTAS CON 10% DE INTERES
              [0] - SALIR
          """)
        opcion=gestion.inputEntero("Ingrese una opción: ")
        if opcion==0:
          break
        elif opcion==1:
          descuentoAzar=random.randint(15,25)
          descuento=valor*(descuentoAzar/100)
          precioFinal=round(valor-descuento)
          print("Descuento del dia del", descuentoAzar,"% , Ud debe abonar ",precioFinal,"pesos ")
          print("Si desea realizar la compra por favor comuniquese al 12345666 con el área de compras")
          print("Gracias por elegirnos!!")
          break
        elif opcion==2:
          cuotas=round( valor/3)
          print("El valor de cada cuota es" ,cuotas, "pesos")
          print("Si desea realizar la compra por favor comuniquese al 12345666 con el área de compras")
          print("Gracias por elegirnos!!")
          break
        elif opcion==3:
          cuotasConInteres=round((valor*1.10)/12)
          print("Ud debera pagar 12 cuotas de", cuotasConInteres," pesos")
          print("Si desea realizar la compra por favor comuniquese al 12345666 con el área de compras")
          print("Gracias por elegirnos!!")
          break
     
while True:
  gestion.decorar(1)
  print("Bienvenido al programa de gestión de stock del grupo A".center(60,))
  print('''

            :::Menú:::
          ::::Inicial::::

        [1] Crear usuario
        [2] Iniciar sesión
        [0] Salir''')
  
  gestion.decorar(2)
  opcion=gestion.inputEntero("Ingrese una opción: ")
  if opcion==0:
    print("¡Gracias por utilizar nuestra app!PS D:\CodoACodo>Grupo A")
    break
  elif opcion==1:
    gestion.decorar(2)
    from tkinter import *
    from tkinter import messagebox
    from tkinter import ttk
    import sqlite3

    #desarrollando la interfaz gráfica.
    root=Tk()
    root.title ("usuarios")
    root.geometry("600x350")

    #las variables de los usuarios

    elID=StringVar()
    elNombre=StringVar()
    elCorreo=StringVar()
    elUsuario=StringVar()
    laContraseña=StringVar()

    #la conexion con la base de datos sirve para crear y conectar con la base

    def conexiondb():
        laConexion=sqlite3.connect("usuarios")
        elCursor=laConexion.cursor()
        try:
          elCursor.execute('''
                CREATE TABLE  usuarios (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE VARCHAR NOT NULL,
                CORREO VARCHAR NOT NULL,
                USUARIO VARCHAR NOT NULL,
                CONTRASEÑA VARCHAR NOT NULL)             
                 ''')
          messagebox.showinfo("CONEXION","base de datos creada con exito")
        except:
            messagebox.showinfo("CONEXION","conexion m exitosa con db")
        
        

           
        
    def eliminardb():
        laConexion=sqlite3.connect("usuarios")
        elCursor=laConexion.cursor()
        if messagebox.askyesno(message="¿los datos se perderan definitivamente, desea continuar?",title="Advertencia" ):
           elCursor.execute("DROP TABLE usuarios")
        else:
            pass
       
       
    def salirAplicacion():    
        valor=messagebox.askquestion("salir","¿Esta seguro que desea salir")
        if valor=="yes":
            root.destroy()
            menu_Cliente()
            
        

    #setea las cajas de texto una vez se carga           
        
    def limpiarCampos():
        elID.set("")
        elNombre.set("")
        elCorreo.set("")
        elUsuario.set("")
        laContraseña.set("")
    
    def mensaje():
        acerca='''
        Aplicacion CRUD
        version 1.0
        Tecnologia Python Tkinter
        '''
    #metodos Crud

    def crear():
        laConexion=sqlite3.connect("usuarios")
        elCursor=laConexion.cursor()
        try:
            datos=elNombre.get(),elCorreo.get(),elUsuario.get(),laContraseña.get()
            elCursor.execute("INSERT INTO usuarios VALUES(NULL,?,?,?,?)",(datos))
            laConexion.commit()
        except:
            messagebox.showwarning("ADVERTENCIA","OCURRIO UN ERROR AL CREAR EL REGISTRO VERIFIQUE CONEXION CON BASE DE DATOS") 
            pass
        limpiarCampos()
        mostrar()   
    
    def mostrar():
        laConexion=sqlite3.connect("usuarios")
        elCursor=laConexion.cursor()
        registros=tree.get_children()
        for elemento in registros:
            tree.delete(elemento)
        try:
            elCursor.execute("SELECT * FROM usuarios")
            for row in elCursor:
               tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
        except:
           pass
    
    #crear tabla

    tree=ttk.Treeview(height=10,columns=('#0','#1','#2','#3'))
    tree.place(x=0, y=130)
    tree.column('#0',width=100)
    tree.heading('#0',text="ID",anchor=CENTER)
    tree.heading("#1",text="Nombre",anchor=CENTER)
    tree.heading("#2",text="Correo electronico",anchor=CENTER)
    tree.heading("#3",text="Usuario",anchor=CENTER)
    tree.heading("#4",text="Contraseña",anchor=CENTER)



    def eventoclick(event):
        item=tree.identify('item',event.x,event.y)
        elID.set(tree.item(item,"text"))
        elNombre.set(tree.item(item,"values")[0])
        elCorreo.set(tree.item(item,"values")[1])
        elUsuario.set(tree.item(item,"values")[2])
        laContraseña.set(tree.item(item,"values")[3])
    tree.bind("<Double-1>", eventoclick)




    def actualizar():
        laConexion=sqlite3.connect("usuarios")
        elCursor=laConexion.cursor()
        try:
            datos=elNombre.get(),elCorreo.get(),elUsuario.get(),laContraseña.get()
            elCursor.execute("UPDATE usuarios SET NOMBRE=?,CORREO=?,USUARIO=?,CONTRASEÑA=? WHERE ID="+ elID.get(),(datos))
            laConexion.commit()
        except:
            messagebox.showwarning("ADVERTENCIA","OCURRIO UN ERROR AL ACTUALIZAR EL REGISTRO VERIFIQUE CONEXION CON BASE DE DATOS") 
            pass
        limpiarCampos()
        mostrar()   
    
    def borrar():
        laConexion=sqlite3.connect("usuarios")
        elCursor=laConexion.cursor()
        if messagebox.askyesno(message="¿los datos se perderan definitivamente, desea continuar?",title="Advertencia" ):
          elCursor.execute("DELETE FROM usuarios WHERE ID= "+elID.get())
          laConexion.commit()
        else:
            messagebox.showwarning("ADVERTENCIA","OCURRIO UN ERROR AL TRATAR DE ELIMINAR EL REGISTRO")  
            pass
    #cambie a IF
        limpiarCampos()
        mostrar()          
         
    
    #colocar widget

    #creacion de menu
    menubar=Menu (root)
    menubasedat=Menu(menubar,tearoff=0) 
    menubasedat.add_command(label="crear/conectar base de datos", command=conexiondb) 
    menubasedat.add_command(label="Eliminar base de datos", command=eliminardb)

    menubasedat.add_command(label="salir de base de datos", command=salirAplicacion) 
    menubar.add_cascade(label="Inicio", menu=menubasedat)

    ayudamenu=Menu(menubar,tearoff=0)
    ayudamenu.add_command(label="resetear campos", command=limpiarCampos) 
    ayudamenu.add_command(label="acerca", command=mensaje) 
    menubar.add_cascade(label="ayuda",menu=ayudamenu)

    #etiquetas y cajas de texto

    e1=Entry(root,textvariable=elID)

    l2=Label(root,text="Nombre")
    l2.place(x=50,y=10)
    e2=Entry(root,textvariable=elNombre,width=50)
    e2.place(x=100,y=10) 


    l3=Label(root,text="Correo electronico")
    l3.place(x=50,y=30)
    e3=Entry(root,textvariable=elCorreo,width=50)
    e3.place(x=150,y=30)

    l4=Label(root,text="usuario")
    l4.place(x=50,y=50)
    e4=Entry(root,textvariable=elUsuario,width=50)
    e4.place(x=100,y=50)

    l5=Label(root,text="contraseña")
    l5.place(x=90,y=70)
    e5=Entry(root,textvariable=laContraseña,width=50)
    e5.place(x=150,y=70)

    #botones
    b1=Button(root,text="crear registro",command=crear)
    b1.place(x=50,y=90)
    b2=Button(root,text="modificar registro",command=actualizar)
    b2.place(x=180,y=90)
    b3=Button(root,text="mostrar lista",command=mostrar)
    b3.place(x=320,y=90)
    b4=Button(root,text="eliminar registro", bg="red",command=borrar)
    b4.place(x=450,y=90)



    root.config(menu=menubar)
 
    #esta siempre esperando, sirve para ver la tabla cuando se indique
    root.mainloop()
    
    '''from tkinter import *
    from tkinter. ttk import *
  
    root=Tk()
    root.title ("formulario")
    
    root.geometry("550x450+300+300")
    root.config(bg="pink")
    
    Lbel1=Label(root,text="Nombre")
    Lbel1.place(x=10,y=10,width=100,height=30)
    Txt1=Entry(root)
    Txt1.place(x=10,y=120,width=100,height=30)
    
    contraseña=Label(root,text="ingrese una contraseña para nuestro sistema:")
    contraseña.pack()
    
    contra=StringVar()
    contra1=Entry(root,width=60,textvariable=contra,show="*")
    contra1.pack()
    def ingresar():
        root.title("bienvenido")
    menu_Cliente()

    
    bt=Button(root,text="Ingresar",command=ingresar)
    bt.pack(side=BOTTOM)
    root.mainloop()     
     
    print("Crear Usuario")
        
    logins=[]
    usuario=input("Ingrese nombre de usuario: ")
    contrasena=input("Ingrese contraseña: ")

    logins={
    "usuario":usuario,
    "contraseña":contrasena,}
   '''
    print("Hola", usuario, "tu contraseña sera", contraseña, "por favor recorda anotar los datos para no olvidarte") 
    gestion.decorar(3)   

  elif opcion==2:
    gestion.decorar(2)
    print("Iniciar sesión")
    from tkinter import *
    from tkinter. ttk import *
    
    root=Tk()
    root.title ("Logins usuarios grupo A")
    
    root.geometry("350x250+300+300")
    root.config(bg="pink")
    
    usuario=Label(root, text="Ingrese su nombre:")
    usuario.pack()
    
    usuario1=StringVar()
    usu=Entry(root,width=30,textvariable=usuario1)
    usu.pack()
    
    contraseña=Label(root,text="contraseña:")
    contraseña.pack()
    
    contra=StringVar()
    contra1=Entry(root,width=30,textvariable=contra,show="*")
    contra1.pack()
    def ingresar():
      if usuario1.get()=="Juan" and contra.get()=="1234":
        root.title("bienvenido")
        print("Hola juan bienvenid@ al menú de la empresa")
        menu_Usuario()
      else:
        root.title("cliente")
        print("usted es un cliente por lo tanto podra ver los productos que tenemos y el stock con el que cuenta para realizar su compra")
        menu_Cliente()
    bt=Button(root,text="Ingresar",command=ingresar)
    bt.pack(side=BOTTOM)
    root.mainloop()     
    
    
    
    
    
    


        
        
        
        
        
        
        
        
 
              

     
         

  

    









        

    

