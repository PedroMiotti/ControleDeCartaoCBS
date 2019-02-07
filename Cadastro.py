from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import sqlite3
import pandas as pd

#Creating RootWindow----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# tela_cadastro = Tk()
tela_cadastro = Toplevel()
tela_cadastro.geometry("1000x626+650+250")
tela_cadastro.title("Novo cadastro")
tela_cadastro.resizable(False, False)

#Creating Icon----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
tela_cadastro.iconbitmap('Imagens\cbsicon.ico')

#conectando ao banco de dados----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
conn = sqlite3.connect('BD\cadastroempresa.db')
c = conn.cursor()

#Creating Widgets

#defining StringVars----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
nome_empresa_str = StringVar()
cnpj_str = StringVar()
endereco_str = StringVar()
complemento_str = StringVar()
contato_str = StringVar()
numero_funcionarios_str = StringVar()
quantidade_dias_str = StringVar()
vendedor_str = StringVar()
numero_endereco_str = StringVar()
bairro_endereco_str = StringVar()
cidade_endereco_str = StringVar()
telefone1_str = StringVar()
telefone2_str = StringVar()

#Nome da empresa----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
nome_empresa = Label(tela_cadastro, text = ("Nome da empresa : *"), font=("Courier new", 15))
nome_empresa.place(x=15, y = 5 )

nome_empresa_entry = Entry(tela_cadastro, width = 25, font=("Courier new", 18), relief = "flat", textvariable = nome_empresa_str)
nome_empresa_entry.place(x = 15, y = 46)

#CNPJ--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cnpj = Label(tela_cadastro, text = ("CNPJ :"), font=("Courier new", 15))
cnpj.place(x = 15, y = 95)

cnpj_entry = Entry(tela_cadastro, width = 15, font=("Courier new", 18), relief = "flat", textvariable = cnpj_str )
cnpj_entry.place(x = 15, y = 130)

#Endereco----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
endereco = Label(tela_cadastro, text = ("Endereco : *"), font=("Courier new", 15))
endereco.place(x= 15, y = 190 )

endereco_entry = Entry(tela_cadastro, width = 25, font=("Courier new", 18), relief = "flat" , textvariable = endereco_str)
endereco_entry.place(x = 15, y = 230)

#Bairro-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
complemento = Label(tela_cadastro, text = ("Complemento : "), font=("Courier new", 15))
complemento.place(x = 15, y = 295)

complemento_entry = Entry(tela_cadastro, width = 20, font=("Courier new", 18), relief = "flat", textvariable = complemento_str )
complemento_entry.place(x = 15, y = 335)

#Contato----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
contato = Label(tela_cadastro, text = ("Contato : *"), font=("Courier new", 15))
contato.place(x = 15, y = 395)

contato_entry = Entry(tela_cadastro, width = 20, font=("Courier new", 18), relief = "flat" , textvariable = contato_str)
contato_entry.place(x = 15, y = 435)

#Observacao------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
observacao = Label(tela_cadastro, text = ("Observacao : "), font=("Courier new", 15))
observacao.place(x = 15, y = 495)

observacao_text = Text(tela_cadastro, width = 70,height = 5, relief = "flat" )
observacao_text.place(x = 15, y = 535)

#Numero de fucionarios----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
numero_funcionarios = Label(tela_cadastro, text = ("Nº de Funcionarios : *"), font=("Courier new", 15))
numero_funcionarios.place(x = 416, y = 5)

numero_funcionarios_spinbox = Spinbox(tela_cadastro, from_ = 0, to = 4000, font=("Couriew new", 15), width=5, relief = "flat", textvariable = numero_funcionarios_str)
numero_funcionarios_spinbox.place(x = 420, y = 46)

#Quantidade De Dias----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
quantidade_dias = Label(tela_cadastro, text = ("Dias parados : *"), font=("Courier new", 15))
quantidade_dias.place(x = 416, y = 95)

quantidade_dias_spinbox = Spinbox(tela_cadastro, from_ = 0, to = 2000, font=("Couriew new", 15), width=5, relief = "flat", textvariable =quantidade_dias_str)
quantidade_dias_spinbox.place(x = 420, y = 130)

#Vendedor----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
vendedor = Label(tela_cadastro, text = ("Vendedor : *"), font=("Courier new", 15))
vendedor.place(x = 660, y = 95)

vendedor_entry = Entry(tela_cadastro, width = 20, font=("Courier new", 18), relief = "flat", textvariable = vendedor_str )
vendedor_entry.place(x = 658, y = 130)

#cidade----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Populando Combobox
def cidades_sp():

    cidades_file = open("C:\\Users\Dinopc\Desktop\CBSControleDeCartao\Texto\cidadesSP.txt", "r").readlines()

    cidades = []

    for line in cidades_file:
         cidades.append(line)

    return cidades

#combobox Widget
cidade_endereco = Label(tela_cadastro, text = ("Cidade : *"), font=("Courier new", 15))
cidade_endereco.place(x = 400, y = 190)

cidade_endereco_combobox = ttk.Combobox(tela_cadastro,font=('arial', 14), width = 18, textvariable = cidade_endereco_str)
cidade_endereco_combobox.place(x = 400, y = 230)

cidade_endereco_combobox['values'] = cidades_sp()

#bairro----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bairro_endereco = Label(tela_cadastro, text = ("Bairro : *"), font=("Courier new", 15))
bairro_endereco.place(x = 660, y = 190)

bairro_endereco_entry = Entry(tela_cadastro, width = 15, font=("Courier new", 18), relief = "flat" , textvariable = bairro_endereco_str)
bairro_endereco_entry.place(x = 658, y = 230)

#telefone1----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
telefone1 = Label(tela_cadastro, text = ("Telefone 1 :"), font=("Courier new", 15))
telefone1.place(x = 350, y = 395)

telefone1_entry = Entry(tela_cadastro, width = 15, font=("Courier new", 18), relief = "flat" , textvariable = telefone1_str)
telefone1_entry.place(x = 350, y = 435)

#telefone2----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
telefone2 = Label(tela_cadastro, text = ("Telefone 2 :"), font=("Courier new", 15))
telefone2.place(x = 600, y = 395)

telefone2_entry = Entry(tela_cadastro, width = 15, font=("Courier new", 18), relief = "flat" , textvariable = telefone2_str)
telefone2_entry.place(x = 600, y = 435)


#defining the buttons funtions----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#adicionando colaboradores---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def adicionar_colaboradores():
    nome_empresa_get = nome_empresa_str.get()

    if nome_empresa_get == '':
        messagebox.showerror("Ops !" , 'Prencha todos os dados obrigatorios !' ,parent = adicionar_colaboradores)
    else:
        #Abrindo janela para escolher arquivo
        getting_excelfile = filedialog.askopenfilename(parent=tela_cadastro, initialdir="/",title='Selecione a planilha de colaboradores')
        # #reading Excel
        read_excel = pd.read_excel(getting_excelfile)

        c.execute('''CREATE TABLE {}(nome, cod ,cesta)'''.format(nome_empresa_get))
        conn.commit()

        for index, row in read_excel.iterrows():
            insert_table = '''INSERT INTO {}(nome, cod, cesta) VALUES(?,?,?)'''.format(nome_empresa_get)
            c.execute(insert_table, (row[0], row[1], row[2]),)
            conn.commit()
        messagebox.showinfo("Sucesso !" , "Colaboradores importados com sucesso !", parent = tela_cadastro)


#Salvando cadastro---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def salvar_cadastro():
    #getting the data grom the cadastro form
    nome_empresa_get = nome_empresa_str.get()
    cnpj_get = cnpj_str.get()
    endereco_get = endereco_str.get()
    complemento_get = complemento_str.get()
    contato_get = contato_str.get()
    observacao_get = observacao_text.get("1.0","end-1c" )
    numero_funcionarios_get = numero_funcionarios_str.get()
    quantidade_dias_get = quantidade_dias_str.get()
    vendedor_get = vendedor_str.get()
    numero_endereco_get =  numero_endereco_str.get()
    bairro_endereco_get = bairro_endereco_str.get()
    cidade_endereco_get = cidade_endereco_str.get()
    telefone1_get = telefone1_str.get()
    telefone2_get = telefone2_str.get()



    if nome_empresa_get == '' or numero_funcionarios_get == '':
        messagebox.showerror("Ops !" , "Prencha todos os dados obrigatorios !", parent = save_button)
    elif quantidade_dias_get == '' or vendedor_get == '':
        messagebox.showerror("Ops !" , "Prencha todos os dados obrigatorios !", parent = save_button)
    elif endereco_get == '' or cidade_endereco_get == '':
        messagebox.showerror("Ops !" , "Prencha todos os dados obrigatorios !", parent = save_button)
    elif  bairro_endereco_get == '' and contato_get == '':
        messagebox.showerror("Ops !" , "Prencha todos os dados obrigatorios !", parent = save_button)
    else:
        #inserting into the database
        cadastro_sql = "INSERT INTO cadastro (nomeempresa, nfuncionarios, cnpj,diasparado, vendedor,endereco,cidade , bairro, complemento, contato, telefone,telefonedois, obs) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
        c.execute(cadastro_sql, (nome_empresa_get, numero_funcionarios_get , cnpj_get, quantidade_dias_get, vendedor_get,endereco_get,cidade_endereco_get, bairro_endereco_get,complemento_get, contato_get, telefone1_get, telefone2_get, observacao_get))
        conn.commit()
        messagebox.showinfo("Sucesso !" , "A empresa " + nome_empresa_get + " foi cadastrada com sucesso", parent = save_button )



#cancelando cadastro---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def cancelar_cadastro():
    Ask_msg = messagebox.askquestion("CBS", "Tem certeza que deseja cancelar o cadastro ?", parent = tela_cadastro)
    if Ask_msg == "yes":
        tela_cadastro.destroy()
    else:
        pass
#Adicionar Colaboradores Botao----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
adicionar_colaboradores = Button(tela_cadastro, text = "Adicionar \n Colaboradores", font = ("Courier new", 11), relief = "flat", height = 3, bg = "PaleGreen3", fg = "white", command = adicionar_colaboradores)
adicionar_colaboradores.place(x = 600 , y = 547)


#Botao Salvar----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
save_icon = PhotoImage(file = "Imagens\saveicon.png")
save_button = Button(tela_cadastro, image = save_icon, relief = "flat", command = salvar_cadastro)
save_button.place(x = 900, y = 547)

#Botao cancelar----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
trash_icon = PhotoImage(file = "Imagens\cancelar_icon.png")
save_button = Button(tela_cadastro, image = trash_icon, relief = "flat", command = cancelar_cadastro)
save_button.place(x = 770, y = 547)




tela_cadastro = tela_de_inicio()
# tela_cadastro.mainloop()
