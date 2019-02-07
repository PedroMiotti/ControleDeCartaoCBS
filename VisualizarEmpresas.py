from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import sqlite3

tela_empresas = Tk()
tela_empresas.geometry("680x370+650+250")
tela_empresas.title("Empresas Cadastradas")
tela_empresas.resizable(False, False)

#Creating Icon----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tela_empresas.iconbitmap('Imagens\cbsicon.ico')


#conectando ao banco de dados----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
conn = sqlite3.connect('BD\cadastroempresa.db')
c = conn.cursor()

#Creating Widgets

#Treeview----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

empresas_tree = ttk.Treeview(tela_empresas, show ="headings", height= 14)
empresas_tree.place(x = 10, y = 55)
empresas_tree["columns"] = ("one", "two")
empresas_tree.column("one", width = 450)
empresas_tree.column("two", width = 210)
empresas_tree.heading("one", text = "Empresa", anchor = "w")
empresas_tree.heading("two", text = "Vendedor", anchor = "w")

#Defining functions----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def mostrar_empresas():
    selecionar_empresas = "SELECT nomeempresa, vendedor FROM cadastro "
    c.execute(selecionar_empresas)
    exe = c.fetchall()

    for exe in exe:
        empresas_tree.insert('', END, values = exe)



mostrar_empresas()


#Buttons----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
editar_btt = Button(tela_empresas, text = 'Editar', font = ("Courier new", 11), relief = "flat", height = 2,width = 9 , bg = "PaleGreen3", fg = "white" )
editar_btt.place(x = 585, y = 5)

delete_btt = Button(tela_empresas, text = 'Excluir', font = ("Courier new", 11), relief = "flat", height = 2,width = 9 , bg = "tomato", fg = "white" )
delete_btt.place(x = 490, y = 5)


















tela_empresas.mainloop()
