##inicio del gato
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
from time import sleep
import pymysql
import pygame

db=pymysql.connect(host='localhost', user='root', passwd='', db='maraton')
cursor=db.cursor()
import subprocess

pygame.init ()
pygame.mixer.music.load ("intro.mp3")
pygame.mixer.music.play (1)

x_burro=20
y_burro=540
x_juga1=20
y_juga1=340
x_juga2=20
y_juga2=440
idmateria=""

##creacion del tablero
raiz=Tk()
raiz.resizable(1,1)
raiz.config(bg="light sea green")
raiz.geometry("1332x700")
raiz.config(cursor="heart")
raiz.config(bd=25)

str_ale=StringVar()
str_ale.set("")
str_nom=StringVar()
str_id=StringVar()
str_aux=StringVar()
str_op1=StringVar()
str_op2=StringVar()
str_op3=StringVar()
str_opc=StringVar()
str_nom.set("")
str_id.set("")
str_op1.set("")
str_op2.set("")
str_op3.set("")
str_opc.set("")
maximo=0
seleccion=IntVar()
turno=1

def lista_materias():
## Combo de Usuarios
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='maraton')
    cursor = conn.cursor()
    cursor.execute('select descripcion from materia')
    mts = []

    for row in cursor:
        mts.append(row[0])
    cursor.close()
    conn.close()
    return mts

def as_lista(event):
    global idmateria
    global maximo
    men=mat.get()
    ##messagebox.showinfo(message=men)
    sql = "select id_materia from materia where descripcion='"+men+"'"
    db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
    cursor = db.cursor()
    cursor.execute(sql)
    idmateria = cursor.fetchone()[0]
    sql = "select max(id_preguntas) from pregunta"
    cursor.execute(sql)
    maximo = cursor.fetchone()[0]
    ##messagebox.showinfo(message=idmateria)



def llena_lista():
    global idmateria
    id_pre.delete(0, tk.END)
    des_pre.delete(0, tk.END)
    db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
    r = 0
    cursor = db.cursor()
    sql="select id_preguntas, Preguntas, opcion1, opcion2, opcion3, correcto, nivel from preguntas where id_materia="+str(idmateria)+" order by id_pregunta"
    cursor.execute(sql)
    for row in cursor:
        id_pre.insert(r, row[0])
        des_pre.insert(r, row[1])
        opc1.insert(r, row[2])
        opc2.insert(r, row[3])
        opc3.insert(r, row[4])
        opcc.insert(r, row[5])
        r = r + 1
    id_pre.config(height=r)
    des_pre.config(height=r)
    opc1.config(height=r)
    opc2.config(height=r)
    opc3.config(height=r)
    opcc.config(height=r)
    marco.config(height=(r+1)*20)
    cursor.close()
    db.close()
    selecciona.place(x=10, y=(r + 2) * 20 + 50)
    pregunta_u.place(x=10, y=(r + 4) * 20+ 40)
    opc1_u.place(x=10, y=(r + 5) * 20 + 50)
    opc2_u.place(x=10, y=(r + 7) * 20 + 40)
    opc3_u.place(x=10, y=(r + 9) * 20 + 30)
    opcc_u.place(x=10, y=(r + 11) * 20 + 20)
    alta.place(x=10, y=(r + 12) * 20 + 30)
    baja.place(x=105, y=(r + 12) * 20 + 30)
    modifica.place(x=200, y=(r + 12) * 20+30)



##creacion de la segunda ventana
def ventana2():
    global tcs
    subprocess.Popen(["python", "materias.py"])
    def actualizar(): ##programar la actualizacion de la base de datos cuando se agrege un nuevo usuario
        db=pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
        cursor=db.cursor()
        cursor.execute("select Nombre from maraton.materia")
        tcs=[" "]
        for row in cursor:
            tcs.append(row)
        cursor.close()
        db.close()
        tc["values"]=tcs
        bn["values"]=tcs
    
        b.destroy()

def ventana3():
    global tcs
    subprocess.Popen(["python", "usuario.py"])
    def actualizar(): ##programar la actualizacion de la base de datos cuando se agrege un nuevo usuario
        db=pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
        cursor=db.cursor()
        cursor.execute("select Nombre from maraton.Usuario")
        tcs=[" "]
        for row in cursor:
            tcs.append(row)
        cursor.close()
        db.close()
        tc["values"]=tcs
        bn["values"]=tcs
    
        b.destroy()

def  ventana4():
    global tcs
    subprocess.Popen(["python", "preguntas.py"])
    def actualizar(): ##programar la actualizacion de la base de datos cuando se agrege un nuevo usuario
        db=pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
        cursor=db.cursor()
        cursor.execute("select Nombre from maraton.Preguntas")
        tcs=[" "]
        for row in cursor:
            tcs.append(row)
        cursor.close()
        db.close()
        tc["values"]=tcs
        bn["values"]=tcs
    
        b.destroy()                     
    ##mi computadora esta algo lenta no se si le pase lo mismo a usted maestro, pero tarda un poco de sacar la 2da ventana    

   
##crear las variables

##imprimir las imagenes

v=PhotoImage(file="v.png")
f=PhotoImage(file="f.png")
l=PhotoImage(file="l.png")
p=PhotoImage(file="p.png")
i_dado=PhotoImage(file="dado.png")
s=PhotoImage(file="s.png")
va=PhotoImage(file="va.png")
r=PhotoImage(file="r.png")
i_pregunta=PhotoImage(file="aiger.png")
## Nombre del primer usuario
def nombre1(event):
   tc.config(state=DISABLED)
## Nombre del segundo usuario
def nombre2(event):
   bn.config(state=DISABLED)

## Combo de Usuarios
cursor.execute('select Nombre from usuario')
tcs=[]

for row in cursor:
  tcs.append(row)



mat=ttk.Combobox(raiz, font='Helvetica 10', width=20)
mat.place(x=360, y = 1)
mat.bind('<<ComboboxSelected>>', as_lista)
lista=lista_materias()
mat['values']=lista


boton1=Button(raiz,width=91,height=99,relief="flat",image=f,command=ventana2)
boton1.place(x=1,y=1)
boton2=Button(raiz,width=91,height=99,relief="flat",image=v,command=ventana3)
boton2.place(x=100,y=1)
boton3=Button(raiz, width=91,height=99,relief="flat",image=l,command=ventana4)
boton3.place(x=200,y=1)





Label(raiz,image=p, bg="light sea green", fg="light sea green", width=1159, height=551).place(x=100, y=120)
#Label(raiz,image=s, bg="light sea green", fg="light sea green", width=50, height=50).place(x=1, y=120)
#Label(raiz,image=va, bg="light sea green", fg="light sea green", width=50, height=50).place(x=1, y=170)
#Label(raiz,image=r, bg="light sea green", fg="light sea green", width=50, height=50).place(x=1, y=220)

def lista_materias():
    ## Combo de Usuarios
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='maraton')
    cursor = conn.cursor()
    cursor.execute('select descripcion from materia')
    mts = []
    for row in cursor:
        mts.append(row[0])
    cursor.close()
    conn.close()
    return mts

def as_lista(event):
    global idmateria
    global maximo
    men=mat.get()
    ##messagebox.showinfo(message=men)
    sql = "select id_materia from materia where descripcion='"+men+"'"
    db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
    cursor = db.cursor()
    cursor.execute(sql)
    idmateria = cursor.fetchone()[0]
    sql = "select max(id_preguntas) from preguntas"
    cursor.execute(sql)
    maximo = cursor.fetchone()[0]
    ##messagebox.showinfo(message=idmateria)
    cursor.close()
    db.close()
    raiz.mainloop()
    ##final del codigoS
def selec_pregunta():
    global idmateria
    global maximo
    db = pymysql.connect(host="localhost", user="root", passwd="", db="maraton")
    cursor = db.cursor()
    registros=0
    while registros==0:
        str_ale.set(str(randint(0,maximo)))
        sql = "select count(*) from pregunta where id_materia="+str(idmateria)
        + " and id_pregunta=" + str_ale.get()
        cursor.execute(sql)
        registros=cursor.fetchone()[0]
    sql="select id_pregunta, Pregunta, opcion1, opcion2, opcion3, correcto, nivel from pregunta where id_materia="
    sql=sql+str(idmateria)+" and id_pregunta="+str_ale.get()
    cursor.execute(sql)
    for row in cursor:
        ##(row)
        str_nom.set(row[1])
        str_op1.set(row[2])
        str_op2.set(row[3])
        str_op3.set(row[4])
        str_opc.set(row[5])
    e_pregunta.config(width=20)
    e_pregunta.place(x=690, y=60)
 
    pregunta_u.config(width=50)
    pregunta_u.place(x=690, y=90)
 
    r_opc1.config(width=2)
    r_opc1.place(x=665, y=120)
    opc1_u.config(width=50)
    opc1_u.place(x=690, y=120)
    r_opc2.config(width=2)
    r_opc2.place(x=665, y=150)
    opc2_u.config(width=50)
    opc2_u.place(x=690, y=150)
    r_opc3.config(width=2)
    r_opc3.place(x=665, y=180)
    opc3_u.config(width=50)
    opc3_u.place(x=690, y=180)
    opcc_u = Entry(raiz, textvariable=str_opc, font='Helvetica 8', width=1)
    opcc_u.place(x=690, y=210)
    ##print(sql)
    cursor.close()
    db.close()

def man_usu():
    subprocess.Popen(['python', 'catalogo.py'])

def man_mat():
    subprocess.Popen(['python', 'cat_materia.py'])

def man_pre():
    subprocess.Popen(['python', 'cat_pregunta.py'])

def sel_prgunta():    
    b_pregunta.config(height=3)
    b_pregunta.config(width=3)
    pregunta.config(height=400)
    pregunta.config(width=550)
    selec_pregunta()
    ##raiz.update()

def avanza1():
    global turno
    global x_juga1
    global y_juga1
    x_juga1 = x_juga1 + 50
    juga1.place(x=x_juga1, y=y_juga1)
    if x_juga1>=1000:
        messagebox.showinfo(message="Gano jugador 1")
    turno = 2
def avanza2():
    global turno
    global x_juga2
    global y_juga2
    x_juga2 = x_juga2 + 100
    juga2.place(x=x_juga2, y=y_juga2)
    if x_juga2>=1000:
        messagebox.showinfo(message="Gano jugador 2")
    turno = 1
def avanza_burro():
    global turno
    global x_burro
    global y_burro
    x_burro = x_burro + 50
    #burro.place(x=1, y=220)
    if turno==1:
        turno = 2
    else:
        turno = 1
    if x_burro>=1000:
        messagebox.showinfo(message="Gano la ignorancia")

def seleccionado():
    global turno
    global x_burro
    global y_burro
    global x_juga2
    global y_juga2
    if str(seleccion.get())==str_opc.get():
        messagebox.showinfo(message="Muy bien!!!!!!!!")
        if turno==1:
            avanza1()
        else:
            avanza2()
    else:
         messagebox.showinfo(message="Respuesta incorrecta")
         avanza_burro()
    b_pregunta.config(height=180)
    b_pregunta.config(width=180)
    pregunta.config(height=3)
    pregunta.config(width=3)
    e_pregunta.config(width=0)
    e_pregunta.place(x=620, y=60)
    pregunta_u.config(width=0)
    pregunta_u.place(x=650, y=90)
    r_opc1.config(width=0)
    r_opc1.place(x=655, y=120)
    opc1_u.config(width=0)
    opc1_u.place(x=650, y=120)
    r_opc2.config(width=0)
    r_opc2.place(x=655, y=150)
    opc2_u.config(width=0)
    opc2_u.place(x=650, y=150)
    r_opc3.config(width=0)
    r_opc3.place(x=655, y=180)
    opc3_u.config(width=0)
    opc3_u.place(x=650, y=180)
    str_nom.set("")
    str_id.set("")
    str_op1.set("")
    str_op2.set("")
    str_op3.set("")
    str_opc.set("")


cat_usu = Button(raiz, cursor="mouse", bg="white", relief="ridge",text="Usuarios", command=man_usu,
width=10, height=1)
cat_usu.place(x=10, y=1)
cat_mat = Button(raiz, cursor="mouse", bg="white", relief="ridge",text="Materias", command=man_mat,
width=10, height=1)
cat_mat.place(x=90, y=1)
cat_pre = Button(raiz, cursor="mouse", bg="white", relief="ridge",text="Preguntas", command=man_pre,
width=10, height=1)
cat_pre.place(x=170, y=1)

mate=Label(raiz, bg="LightSteelBlue2", fg="black", font='Helvetica 12 bold',
text="Materia").place(x=300, y=1)
mat=ttk.Combobox(raiz, font='Helvetica 10', width=20)
mat.place(x=360, y = 1)
mat.bind('<<ComboboxSelected>>', as_lista)
lista=lista_materias()

mat['values']=lista
#i_dado = PhotoImage(file="dado.png")
#i_burro = PhotoImage(file="burro.png")
#i_pista = PhotoImage(file="pista.png")
#i_juga1 = PhotoImage(file="arabela.png")
#i_juga2 = PhotoImage(file="matute.png")
#i_pregunta = PhotoImage(file="pregunta.png")

#pista= Label(raiz, bg='SkyBlue1', image=i_pista)
#pista.place(x=1, y=30)
pregunta= Label(raiz, bg='SkyBlue1', image=i_pregunta, height=3,width=3)
pregunta.place(x=640, y=1)

aleatorio = Entry(raiz, textvariable=str_ale, font='Helvetica 8', width=2)
aleatorio.place(x=20, y=30)

e_pregunta= Label(raiz, bg='brown', fg="white", text="Pregunta", font='Helvetica 8 bold', width=0)
e_pregunta.place(x=620, y=60)

pregunta_u = Entry(raiz, textvariable=str_nom, font='Helvetica 8', width=0)
pregunta_u.place(x=650, y=90)

r_opc1=Radiobutton(raiz, value=1, variable=seleccion, command=seleccionado,width=0)
r_opc1.place(x=655, y=120)

opc1_u = Entry(raiz, textvariable=str_op1, font='Helvetica 8', width=0)
opc1_u.place(x=650, y=120)

r_opc2=Radiobutton(raiz, value=2, variable=seleccion, command=seleccionado,width=0)
r_opc2.place(x=655, y=150)

opc2_u = Entry(raiz, textvariable=str_op2, font='Helvetica 8', width=0)
opc2_u.place(x=650, y=150)

r_opc3=Radiobutton(raiz, value=3, variable=seleccion, command=seleccionado, width=0)
r_opc3.place(x=655, y=180)

opc3_u = Entry(raiz, textvariable=str_op3, font='Helvetica 8', width=0)
opc3_u.place(x=650, y=180)

opcc_u = Entry(raiz, textvariable=str_opc, font='Helvetica 8', width=1)
opcc_u.place(x=650, y=210)

juga1= Label(raiz, bg='SkyBlue1',image=s, width=50, height=50).place(x=1, y=120)

juga2= Label(raiz, bg='SkyBlue1', image=va, width=50, height=50).place(x=1, y=170)

burro= Label(raiz, bg='SkyBlue1', image=r, width=50, height=50).place(x=1, y=220)


b_pregunta = Button(raiz, cursor="mouse", bg="white", relief="ridge", image=i_dado,command=sel_prgunta, width=180, height=180)
b_pregunta.place(x=500, y=50)
raiz.mainloop()
