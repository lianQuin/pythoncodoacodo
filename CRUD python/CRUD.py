from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

#desarrollando la interfaz gráfica.
root=Tk()
root.title ("productos")
root.geometry("600x350")

#las variables de los usuarios

productosCodigo=StringVar()
productosNombre=StringVar()
productosCategoria=StringVar()
productosCantidad=StringVar()  
productosNacionalidad=StringVar()

#la conexion con la base de datos sirve para crear y conectar con la base

def conexiondb():
    laConexion=sqlite3.connect("productos")
    elCursor=laConexion.cursor()
    
    try:
        elCursor.execute('''
            CREATE TABLE productos (
            Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
            Nombre VARCHAR NOT NULL,
            Categoria VARCHAR NOT NULL,
            Cantidad INTEGER NOT NULL,
            Nacionalidad VARCHAR NOT NULL)             
             ''')
        messagebox.showinfo("CONEXION","base de datos creada con exito")
    except:
        messagebox.showinfo("CONEXION","conexion no exitosa con db")
        
        

           
        
def eliminardb():
    laConexion=sqlite3.connect("productos")
    elCursor=laConexion.cursor()
    if messagebox.askyesno(message="¿los datos se perderan definitivamente, desea continuar?",title="Advertencia" ):
       elCursor.execute("DROP TABLE productos")
    else:
        pass
       
       
def salirAplicacion():    
    valor=messagebox.askquestion("salir","¿Esta seguro que desea salir")
    if valor=="yes":
        root.destroy()
        

#setea las cajas de texto una vez se carga           
        
def limpiarCampos():
    productosCodigo.set("")
    productosNombre.set("")
    productosCategoria.set("")
    productosCantidad.set("")
    productosNacionalidad.set("")
    
def mensaje():
    acerca='''
    Aplicacion CRUD
    version 1.0
    Tecnologia Python Tkinter
    '''
#metodos Crud

def crear():
    laConexion=sqlite3.connect("productos")
    elCursor=laConexion.cursor()
    try:
        datos= productosNombre.get().capitalize(), productosCategoria.get().capitalize(), productosCantidad.get(), productosNacionalidad.get().capitalize()
        elCursor.execute("INSERT INTO productos VALUES(NULL,?,?,?,?)",(datos))
        laConexion.commit()
    except:
        messagebox.showwarning("ADVERTENCIA","OCURRIO UN ERROR AL CREAR EL REGISTRO VERIFIQUE CONEXION CON BASE DE DATOS") 
        pass
    limpiarCampos()
    mostrar()   
    
def mostrar():
    laConexion=sqlite3.connect("productos")
    elCursor=laConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        elCursor.execute("SELECT * FROM productos ORDER BY Nombre desc")
        for row in elCursor:
            tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
    except:
        pass   
    
#crear tabla

tree=ttk.Treeview(height=10,columns=('#0','#1','#2','#3'))
tree.place(x=0, y=130)
tree.column('#0',width=100)
tree.heading('#0',text="Codigo",anchor=CENTER)
tree.heading("#1",text="Nombre",anchor=CENTER)
tree.heading("#2",text="Categoria",anchor=CENTER)
tree.heading("#3",text="Cantidad",anchor=CENTER)
tree.heading("#4",text="Nacionalidad",anchor=CENTER)



def eventoclick(event):
    item=tree.identify('item',event.x,event.y)
    productosCodigo.set(tree.item(item,"text"))
    productosNombre.set(tree.item(item,"values")[0])
    productosCategoria.set(tree.item(item,"values")[1])
    productosCantidad.set(tree.item(item,"values")[2])
    productosNacionalidad.set(tree.item(item,"values")[3])
tree.bind("<Double-1>", eventoclick)




def actualizar():
    laConexion=sqlite3.connect("productos")
    elCursor=laConexion.cursor()
    if messagebox.askyesno(message="¿los datos se modificaran definitivamente, desea continuar?",title="Advertencia" ):
        datos= productosNombre.get().capitalize(), productosCategoria.get().capitalize(), productosCantidad.get(), productosNacionalidad.get().capitalize()
        elCursor.execute("UPDATE productos SET Nombre=?, Categoria=?,Cantidad=?, Nacionalidad=? WHERE Codigo="+ productosCodigo.get(),(datos))
        laConexion.commit()
    else:
        messagebox.showwarning("ADVERTENCIA","OCURRIO UN ERROR AL ACTUALIZAR EL REGISTRO VERIFIQUE CONEXION CON BASE DE DATOS") 

    mostrar()   
    
def borrar():
    laConexion=sqlite3.connect("productos")
    elCursor=laConexion.cursor()
    if messagebox.askyesno(message="¿los datos se perderan definitivamente, desea continuar?",title="Advertencia" ):
       elCursor.execute("DELETE FROM productos WHERE Codigo= "+productosCodigo.get())
       laConexion.commit()
    else:
        messagebox.showwarning("ADVERTENCIA","OCURRIO UN ERROR AL TRATAR DE ELIMINAR EL REGISTRO")  
        pass
    #cambie a IF
    limpiarCampos()
    mostrar()   
  
                   
def mostrarStockLim():
    laConexion=sqlite3.connect("productos")
    elCursor=laConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        elCursor.execute("SELECT * FROM productos WHERE Cantidad <=20 ORDER BY Nombre desc ")
        for row in elCursor:
            tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
    except:
        pass
def mostrarStockAlto():
    laConexion=sqlite3.connect("productos")
    elCursor=laConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        elCursor.execute("SELECT * FROM productos WHERE Cantidad >=100 ORDER BY Nombre desc")
        for row in elCursor:
            tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
    except:
        pass

def mostrarImportados():
    laConexion=sqlite3.connect("productos")
    elCursor=laConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        elCursor.execute("SELECT * FROM productos WHERE Nacionalidad = 'Importado' ORDER BY Nombre desc")
        for row in elCursor:
            tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
    except:
        pass
    
def mostrarNacionales():
    laConexion=sqlite3.connect("productos")
    elCursor=laConexion.cursor()
    registros=tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    try:
        elCursor.execute("SELECT * FROM productos WHERE Nacionalidad=='Nacional' ORDER BY Nombre desc ")
        for row in elCursor:
            tree.insert("",0,text=row[0],values=(row[1],row[2],row[3],row[4]))
    except:
        pass    
         
         
    
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

e1=Entry(root,textvariable=productosCodigo)

l2=Label(root,text="Nombre")
l2.place(x=20,y=10)
e2=Entry(root,textvariable=productosNombre,width=50)
e2.place(x=100,y=10) 


l3=Label(root,text="Categoria")
l3.place(x=20,y=30)
e3=Entry(root,textvariable=productosCategoria,width=50)
e3.place(x=100,y=30)

l4=Label(root,text="Cantidad")
l4.place(x=20,y=50)
e4=Entry(root,textvariable=productosCantidad,width=50)
e4.place(x=100,y=50)

l5=Label(root,text="Nacionalidad")
l5.place(x=20,y=70)
e5=Entry(root,textvariable=productosNacionalidad,width=50)
e5.place(x=100,y=70)

#botones
b1=Button(root,text="Crear",command=crear)
b1.place(x=50,y=100)
b2=Button(root,text="Modificar",command=actualizar)
b2.place(x=150,y=100)
b3=Button(root,text="Mostrar",command=mostrar)
b3.place(x=250,y=100)
b4=Button(root,text="Eliminar", bg="red",command=borrar)
b4.place(x=350,y=100)
b5=Button(root,text="Stock bajo",command= mostrarStockLim)
b5.place(x=450,y=100)
b6=Button(root,text="Stock alto",command= mostrarStockAlto)
b6.place(x=550,y=100)
b7=Button(root,text="Importados",command= mostrarImportados)
b7.place(x=650,y=100)
b8=Button(root,text="Nacionales",command= mostrarNacionales)
b8.place(x=750,y=100)


root.config(menu=menubar)
 
#esta siempre esperando, sirve para ver la tabla cuando se indique
root.mainloop()

