import turtle
from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import filedialog
import os
import pickle
 
ventana=Tk()
ventana.geometry("860x800")
ventana.title("Crea Dibujo")
ventana.configure(background="gray80")
st=True
grosor=""
movs=""
grados=""
color_fondo=""
 
lista_colores=[]
canvas = Canvas(master = ventana, width = 860, height = 735)
canvas.pack()
 
t = turtle.RawTurtle(canvas)
 
def color(m):
    global color_fondo
    global lista_colores
    color_selec=colorchooser.askcolor()
    if color_selec!=(None,None):
        bgrcolor=list(color_selec)
        if m == "f":
            color_fondo=bgrcolor[1]
            t.screen.bgcolor(color_fondo)
        else:
            lista_colores.append(bgrcolor[1])
            t.color(lista_colores[0])
 
def hide():
    global st
    if st==True:
        t.hideturtle()
        st=False
    else:
        t.showturtle()
        st=True
 
def abrir():
    global lista_colores
    global color_fondo
    global movs
    global grados
    clear()
    open_archive=filedialog.askopenfilename(initialdir = "/",
                 title = "Seleccione archivo",filetypes = (("all files","*.*"),
                 ("all files","*.*")))
    if open_archive!="":
        try:
            nombre=pickle.load(open(open_archive,"rb"))
            lista_colores = default_color(nombre[2])
            color_fondo = nombre[3]
            if nombre[3] == "":
                color_fondo = "white"
            movs=int(nombre[0])
            grados=int(nombre[1])
            t.screen.bgcolor(color_fondo)
            if entGrosor.get()!="":
                t.pensize(int(entGrosor.get()))
            d=1
            val = validate_data(movs,grados)
            try:
                t.speed(0)
                for i in range(movs):
                    if len(lista_colores)>1:
                        t.color(lista_colores[i%(len(lista_colores))])
                    else:
                        t.color(lista_colores[0])
                    t.left(grados)
                    t.fd(d)
                    d+=1
            except:
                if val == False:
                    messagebox.showwarning("ERROR","Datos introducidos erroneos o insuficientes")
        except:
            messagebox.showwarning("ERROR","No se pudo cargar el atchivo")
 
def validate_data(n,d):
    validate = True
    try:
        n = int(n)
        d = int(d)
    except:
        print("ERROR")
        validate = False
    return validate
 
 
def guardar():
    archivo = [entLados.get(),entGrados.get(),lista_colores,color_fondo]
    guardar = filedialog.asksaveasfilename(initialdir = "/",
              title = "Guardar", defaultextension = ".txt",
              filetypes = (("txt files","*.txt"),("pickle files","*.pickle"),
                           ("all files","*.*")))
    if guardar != "":
        pickle.dump(archivo,open(guardar,"wb"))
        messagebox.showinfo("GUARDADO","Archivo guardado satistactoriamente")
        #print(archivo)
 
def default_color(lis):
    if lis == []:
        lis.append("black")
    return lis
 
def clear():
    global lista_colores
    t.reset()
    lista_colores=[]
 
def crear():
    global lista_colores
    d=1
    if entGrosor.get()!="":
        t.pensize(int(entGrosor.get()))
    lista_colores = default_color(lista_colores)
    val = validate_data(entLados.get(),entGrados.get())
    try:
        t.speed(0)
        for i in range(int(entLados.get())):
            if len(lista_colores)>1:
                t.color(lista_colores[i%(len(lista_colores))])
            else:
                t.color(lista_colores[0])
            t.left(int(entGrados.get()))
            t.fd(d)
            d+=1
    except:
        if val == False:
            messagebox.showwarning("ERROR","Datos introducidos erroneos o insuficientes")
 
 
etiLados=Label(master=ventana,text="Numero Mov",bg="gray80")
etiLados.place(x=1,y=744)
etiGrados=Label(master=ventana,text="Grados",bg="gray80")
etiGrados.place(x=160,y=744)
entGrados=Entry(master=ventana,width=10)
entGrados.place(x=200,y=744)
entLados=Entry(master=ventana,width=10)
entLados.place(x=85,y=744)
etiGrosor=Label(master=ventana,text="Grosor",bg="gray80")
etiGrosor.place(x=267,y=744)
entGrosor=Entry(master=ventana,width=10)
entGrosor.place(x=310,y=744)
btnColor=Button(master=ventana,text="Color Pincel",bg="gray74",command=lambda:color("c"))
btnColor.place(x=403,y=740)
btnFondo=Button(master=ventana,text="Color Fondo",bg="gray74",command=lambda:color("f"))
btnFondo.place(x=490,y=740)
btnClear=Button(master=ventana,text="Clear",bg="gray74",command=clear)
btnClear.place(x=660,y=740)
btnGuardar=Button(master=ventana,text="Guardar",bg="gray74",width=10,command=guardar)
btnGuardar.place(x=778,y=740)
btnAbrir=Button(master=ventana,text="Abrir",bg="gray74",width=8,command=abrir)
btnAbrir.place(x=710,y=740)
btnHide=Button(master=ventana,text="Hide/Show",bg="gray74",command=hide)
btnHide.place(x=580,y=740)
Button(master = ventana,text="Crear",bg="spring green",width=121,command=crear).place(x=1,y=771)
 
ventana.mainloop()