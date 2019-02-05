from tkinter import *
from tkinter import ttk


#Creating RootWindow
tela_de_inicio = Tk()
tela_de_inicio.geometry("900x500+650+250")
tela_de_inicio.title("Controle de entregas CBS")
tela_de_inicio.resizable(False, False)


#Creating Icon
tela_de_inicio.iconbitmap(r'C:\\Users\Dinopc\Desktop\CBSControleDeCartao\Imagens\cbsicon.ico')

#CBS Logo
cbs_logo = PhotoImage(file = 'C:\\Users\Dinopc\Desktop\CBSControleDeCartao\Imagens\cbscestaslogo.gif')
logo_label = Label(image=cbs_logo)
logo_label.place(x=0, y=0, relwidth=1.0, relheight=1.0)

#Pass function
def abrir_cadastro():
    import Cadastro

#Criando Menu
menu_principal = Menu(tela_de_inicio)
tela_de_inicio.config(menu = menu_principal)

#Menu Cadastro
menu_cadastro = Menu(menu_principal)
menu_cadastro.add_command(label = "Novo Cadastro", command= abrir_cadastro)
menu_cadastro.add_command(label = "Empresas Cadastradas", command = abrir_cadastro)
menu_principal.add_cascade(label = "Cadastro", menu = menu_cadastro)

#Menu consultar
menu_consultar = Menu(menu_principal)
menu_consultar.add_command(label = "Cestas Colaboradores", command= abrir_cadastro)
menu_principal.add_cascade(label = "Consultar", menu = menu_consultar)

























tela_de_inicio.mainloop()
