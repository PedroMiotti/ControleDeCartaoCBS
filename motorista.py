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

#conectando ao banco de dados----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
conn = sqlite3.connect('BD\cadastroempresa.db')
c = conn.cursor()

#CBS Logo
cbs_logo = PhotoImage(file = 'Imagens\cbscestaslogo.gif')
cbs_logo = cbs_logo.subsample(2,2)
logo_label = Label(image=cbs_logo)
logo_label.place(x=150, y=0)

#Widgets
#Populating combobox
def empresas():
    c.execute( "SELECT nomeempresa FROM cadastro")

    empresa = []

    for row in c.fetchall():
        empresa.append(row[0])

    return empresa
    conn.commit()
#combobox
pick_cbx_str = StringVar()
pick_cbx = ttk.Combobox(tela_motorista, font=('Courier new', 14), width = 16, textvariable = pick_cbx_str)
pick_cbx.place(x = 115, y = 90)
pick_cbx['values'] = empresas()


#defining escolher function
def escolher_colaborador():
    if pick_cbx_str.get() == "":
        messagebox.showerror("Ops !", "Selecione uma empresa", parent = tela_motorista)
    else:
        tela_colaborador = Toplevel()
        tela_colaborador.geometry("380x180+650+250")
        tela_colaborador.title("Cestas Basicas Sorocaba")
        tela_colaborador.resizable(False, False)

        #Creating Icon
        tela_colaborador.iconbitmap('Imagens\cbsicon.ico')

        #CBS Logo
        cbs_logo2 = PhotoImage(file = 'Imagens\cbscestaslogo.gif')
        cbs_logo2 = cbs_logo2.subsample(2,2)
        logo_label2 = Label(tela_colaborador,image=cbs_logo2)
        logo_label2.place(x=130, y=0)

        nome_empresalb = Label(tela_colaborador, text='Empresa : ', font =('courier new', 13))
        nome_empresalb.place(x = 0, y = 75)

        nome_empresadb_str = StringVar()
        nome_empresadb = Label(tela_colaborador, text='', font =('courier new', 13), textvariable = nome_empresadb_str)
        nome_empresadb_str.set(pick_cbx_str.get())
        nome_empresadb.place(x = 105, y = 75)

        pick_empresa_str = StringVar()
        pick_empresa = Entry(tela_colaborador, font=('Courier new', 16), width = 16, relief ="flat",textvariable = pick_empresa_str)
        pick_empresa.place(x = 60, y = 120)

        def consultar_cartao():
            consultar_wind = Tk()
            consultar_wind.geometry('380x180+650+250')
            consultar_wind.title("Consultar Cartao")
            #Creating Icon
            consultar_wind.iconbitmap('Imagens\cbsicon.ico')
#Stoped here +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
            fetching_data = ("SELECT nome FROM {} WHERE cod = ?".format(nome_empresadb_str.get()))
            c.execute(fetching_data, (pick_empresa_str.get()))
            get_data = c.fetchall()

            print(get_data)
            conn.commit()



        consultar_btt = Button(tela_colaborador, text = 'Consultar', font=("courier new", 10), width = 8, relief = 'flat', bg = "PaleGreen3", fg= "white", command = consultar_cartao)
        consultar_btt.place(x = 260, y = 120)

        tela_colaborador.mainloop()

escolher_btt = Button(tela_motorista, text = 'Escolher', font=("courier new", 13), width = 8, relief = 'flat', bg = "PaleGreen3", fg= "white", command = escolher_colaborador)
escolher_btt.place(x = 165, y = 140)




def sair_motorista():
    msg = messagebox.askquestion('CBS', "Tem certeza que deseja sair do sistema ?", parent = tela_motorista)

    if msg == "yes":
        tela_motorista.destroy()
        import LoginCBS

    else:
        pass


exit_btt = Button(tela_motorista, text= 'Sair', font=("courier new", 11), relief = 'flat', command = sair_motorista)
exit_btt.place(x = 0, y = 0)




tela_motorista.mainloop()
