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
ventana_principal.title ("bandera españa")
# ventana tamaño
ventana_principal.geometry("600x400")
# desabilitar boton de maximizar
ventana_principal.resizable(False,False)
# color de fondo de la ventana
ventana_principal.config(bg="salmon1")
#---------------
# frama rojo
#---------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=600, height=230)
frame_rojo.place(x=0, y=0 )

#---------------
# frama amarillo
#---------------
frame_amarillo = Frame(ventana_principal)
frame_amarillo.config(bg="yellow", width=600, height=290)
frame_amarillo.place(x=0, y=100 )

#---------------
# frama rojo
#---------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config(bg="red", width=600, height=230)
frame_rojo.place(x=0, y=300 )
#---------------
# frama azul
#---------------
frame_azul = Frame(ventana_principal)
frame_azul.config(bg="white", width=65, height=65)
frame_azul.place(x=100, y=160 )
# run
# se ejecuta el emtodo mainloop()de la clase Tk() a travez de la ventana_principal. este metodo despliega la ventana en pantalla y queda ala espera de lo que el usuario haga (click en un boton,escribir,etc). cada accion del usuario se conoce como un evento. El metodo mainloop() es un bucle infventana_principal.mainloop()es un bucle infinito.
ventana_principal.mainloop()

