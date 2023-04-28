from tkinter import *


ventana_principal= Tk()

ventana_principal.title("suma de enteros")

ventana_principal.geometry("500x500")

ventana_principal.resizable(False,False)

# color de la ventana
ventana_principal.config(bg=("red"))

# frame de entrada de datosf
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=10, y=10)

# logo de la app
logo=PhotoImage(file="img/escudo_colegio.png")
lb_logo=Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=70,y=40)

# titulo de la app
titulo=Label(frame_entrada, text="suma enteros 1.0")
titulo.config(bg="red", fg="white", font=("Arial",16))
titulo.place(x=240,y=10)

# etiqueta para valor de x
lb_x = Label(frame_entrada, text = "x = ")
lb_x.config(bg="white", fg="red", font=("helvetica", 18))
lb_x.place(x=240, y=60)


entry_x = Entry(frame_entrada)
entry_x.config (bg="white", fg="red", font=("tienes new roman", 18), width=6)
entry_x.focus_set()
entry_x.place(x=290, y=60)

# etiqueta para valor de y
lb_y = Label(frame_entrada, text = "y = ")
lb_y.config(bg="white", fg="red", font=("helvetica", 18))
lb_y.place(x=240, y=120)

entry_y = Entry(frame_entrada)
entry_y.config (bg="white", fg="red", font=("tienes new roman", 18), width=6)
entry_y.focus_set()
entry_y.place(x=290, y=120)

# frame de operacion
frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="white", width=480, height=100)
frame_operaciones.place(x=10, y=200)

# frame del resultado
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="white", width=480, height=180)
frame_resultado.place(x=10, y=310)

ventana_principal.mainloop()