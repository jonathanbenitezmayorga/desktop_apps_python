# se importa la libreria tkinter con todoas sus fnciones
from tkinter import *

#-----------------------
# funciones de la app
#-----------------------

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_pricipal,que aquiere las carateristicas de un objeto TK[]
ventana_principal = Tk () 

# titulo de la ventana
ventana_principal.title ("bandera de noruega ")
# ventana tamaño
ventana_principal.geometry("600x400")
# desabilitar boton de maximizar
ventana_principal.resizable(False,False)
# color de fondo de la ventana
ventana_principal.config(bg="red")

#---------------
# frama azul
#---------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=80, height=400)
frame_azul.place(x=200, y=0 )

#---------------
# frama azul
#---------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="blue", width=600, height=80)
frame_azul.place(x=0, y=160 )

#---------------
# frama blanco
#---------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="white", width=200, height=20)
frame_azul.place(x=0, y=150 )

#---------------
# frama blanco
#---------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="white", width=400, height=20)
frame_azul.place(x=280, y=150 )

# run
# se ejecuta el emtodo mainloop()de la clase Tk() a travez de la ventana_principal. este metodo despliega la ventana en pantalla y queda ala espera de lo que el usuario haga (click en un boton,escribir,etc). cada accion del usuario se conoce como un evento. El metodo mainloop() es un bucle infventana_principal.mainloop()es un bucle infinito.
ventana_principal.mainloop() 