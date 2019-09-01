from Tkinter import *
from tkMessageBox import *
from tkFileDialog   import askopenfile
from tkSimpleDialog import *
import winsound

#ventana 
ventana = Tk()
ventana.title("Examen practico")
ventana.geometry('730x510+200+200')
img = PhotoImage(file='fondo.gif')
widget = Label(ventana, image=img).place(x=0,y=0)
winsound.PlaySound('Ill Factor.wav',winsound.SND_FILENAME|winsound.SND_ASYNC)

 
def abrirArchivo():
    fa=0
    fv=0
    figurasA = ['paralelogramo','trapecio','circulo','triangulo','cuadrado','rombo']
    figurasV= ['prisma','piramide','cilindro','esfera','tetraedro','cubo']
    frecuencia=askinteger('Datos', 'Digite la Frecuencia')
    frecuencia=frecuencia*(10**9)
    nombre = askopenfile()
    f=nombre.read()
    print f
    lista=f.split("\n")
    lista2=[]
    mostrarA(lista)
    Label (ventana, text="Figuras Area").place(x=3,y=50)
    Label (ventana, text="Figuras Volumen").place(x=558,y=50)
    mostrarB(figurasA)
    mostrarC(figurasV)
    area=askstring('Area', 'Digite el nombre de la Figura')
    volumen=askstring('Volumen', 'Digite el nombre de la Figura')
    
    while fa == 0 or fv ==0:
        for i in figurasA:
            if i == area:
                fa=1
        for a in figurasV:
            if a== volumen:
                fv=1
        if fa == 0:
            area=askstring('Area', 'Digite el nombre de la Figura')
        if fv == 0:
            volumen=askstring('Volumen', 'Digite el nombre de la Figura')
    for i in lista:
        lista1=i.replace(',',' ').split(" ")
        lista2.append(lista1)
    cpr=CPR(lista2,area,volumen)
    Label (ventana, text="numero ciclos").pack()
    Label (ventana, text=str(cpr)).pack()
    ventana.update()
    Tcpu=calcularT(cpr,frecuencia)
    a='Tcpu del codigo original:'
    listb3.insert(END,a)
    listb3.insert(END,Tcpu)  

    nombre.close()
    
    
def mostrarA(lista): #interfaz
       for item in lista:                 
            listb1.insert(END,item)
            
def mostrarB(lista): #interfaz
       for item in lista:                 
            listb4.insert(END,item)
            
def mostrarC(lista): #interfaz
       for item in lista:                 
            listb5.insert(END,item)
    
def CPR(lista,area,volumen):
    l = [""]
    contar=0
    flag=0
    salto = 0
    guardar = 0
    for i in lista:
        r= 0
        if i[0] == salto:
            flag=0
        for a in i:
            
            if a == area and r == 0:
                flag = 0
                
            if a == volumen and r == 0:
                flag = 0
            
            if a == 'lw' or a =='Lw':
                if flag == 0:
                    contar = contar + 4
                    
            if a == 'sw' or a =='Sw':
                if flag == 0:
                    contar = contar + 3
                    
                    
            if a == 'mult' or a=='div' or a == 'Mult' or a=='Div' or a == 'Add' or a == 'add':
                    if flag == 0:
                        contar =contar+4
                        
                        
            if a == 'j' or a=='J':
                    if flag == 0:
                        contar=contar+3
                        flag = 1
                        salto = i[1]
                        
                        
                    
            if a == 'In' or a=='in':
                    if flag == 0:
                        contar=contar+4
                        
            if a == 'ot' or a=='Ot':
                if flag == 0:
                    contar = contar + 4
            if a =='addi' or a == 'Addi':
                if flag == 0:
                    contar = contar +4
                    
                    
            if a == 'beq' or a == 'Beq':
                if flag == 0:
                    contar=contar +3
                    if area == i[4]:
                        flag = 1
                        r=1
                    if volumen == i[4]:
                        flag =1
                        r =1
        #print contar
        #print i
        
                
    
    return contar
def calcularT(cpr,f):
    resultado=(cpr*1.0)/f
    return resultado
    
    
listb1 = Listbox(ventana,width=40, height=19)
listb3 = Listbox(ventana,width=28, height=5)
listb4 = Listbox(ventana,width=28, height=8)
listb5 = Listbox(ventana,width=28, height=8)
errmsg = 'Error!'
Button(text='Abrir archivo', command=abrirArchivo).pack(fill=X)
listb3.pack(side=BOTTOM)
listb1.place(x=250,y=80)
listb4.place(x=3,y=80)
listb5.place(x=558,y=80)

#para que se mantenga la ventana
ventana.mainloop()
winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
 

