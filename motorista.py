from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3

#Creating window
#Creating Window
tela_motorista = Tk()
tela_motorista.geometry("425x200+650+250")
tela_motorista.title("Cestas Basicas Sorocaba")
tela_motorista.resizable(False, False)

#Creating Icon
tela_motorista.iconbitmap('Imagens\cbsicon.ico')

#CBS Logo
cbs_logo = PhotoImage(file = 'Imagens\cbscestaslogo.gif')
cbs_logo = cbs_logo.subsample(2,2)
logo_label = Label(image=cbs_logo)
logo_label.place(x=150, y=0)

#Widgets



tela_motorista.mainloop()
