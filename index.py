from email.mime import image
from importlib.metadata import EntryPoint
from tkinter import *
from tkinter.messagebox import *
from turtle import width
from PIL import ImageTk
from random import randint

letrasUsadas = []
vidas = 7
letrasAcertadas = 0

def colocarLetras():
    x=50
    y=150
    contador=0
    Label(canvas, text="Letras que te quedan").place(x=50,y=100)
    for i in range(26):
        contador+=1
        letrasLabel[i].place(x=x,y=y)
        x+=30
        if contador == 5:
            y+=35
            contador = 0
            x=50
def probarLetraFuncion():
    global vidas
    global letrasAcertadas
    letrasUsadas.append(letrasObtenidas.get())
    print(letrasUsadas)
    letrasLabel[ord(letrasObtenidas.get())-97].config(text="")
    if letrasObtenidas.get() in palabra:
        if palabra.count(letrasObtenidas.get())>1:
            letrasAcertadas+=palabra.count(letrasObtenidas.get())
            for i in range(len(palabra)):
                if palabra[i]==letrasObtenidas.get():
                    guiones[i].config(text=""+letrasObtenidas.get())
        else :
            letrasAcertadas+=1
            guiones[palabra.index(letrasObtenidas.get())].config(text=""+letrasObtenidas.get())
        if letrasAcertadas == len(palabra):
            showwarning(title="Victoria", message="Ganaste el juego")            
    else:
        vidas-=1
        canvas.itemconfig(imagen_id, image=imagenes[vidas-1])
        if vidas == 0:
            showwarning(title="Derrota", message="Se te acabaron los intentos")
raiz = Tk()
archivo = open("palabras.txt","r")
conuntoPalabras = list(archivo.read().split("\n"))
palabra = conuntoPalabras[randint(0,len(conuntoPalabras)-1)].lower()
letrasObtenidas = StringVar()
raiz.config(width=900, height=500, bg="grey", relief="groove", bd=10)
raiz.geometry("900x500")
canvas = Canvas(raiz, width=900, height=500)
canvas.pack(expand=True, fill="both")
imagenes = [ 
    PhotoImage(file="img/1.png"),
    PhotoImage(file="img/2.png"),
    PhotoImage(file="img/3.png"),
    PhotoImage(file="img/4.png"),
    PhotoImage(file="img/5.png"),
    PhotoImage(file="img/6.png"),
    PhotoImage(file="img/7.png"),
]
imagen_id = canvas.create_image(750, 300, image=imagenes[6])
Label(canvas, text="Introduce una letra", font=("verdana", 24)
    ).grid(row=0, column=0, padx=10, pady=10)
letra = Entry(canvas, width=1, font=("verdana", 24), textvariable=letrasObtenidas
    ).grid(row=0, column=1, padx=10, pady=10)
probarLetra = Button(canvas, text="Probar", bg="green", command=probarLetraFuncion
    ).grid(row=1, column=2, padx=10)
letrasLabel = [Label(canvas, text=chr(j+97), font=("verdana", 20)) for j in range(26)]
colocarLetras()
guiones = [Label(canvas, text="_", font=("verdana", 28)) for _ in palabra]
inicialX = 200
for i in range(len(palabra)):
    guiones[i].place(x=inicialX,y=400)
    inicialX+=50


raiz.mainloop()