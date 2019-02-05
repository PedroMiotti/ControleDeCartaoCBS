from tkinter import *
from tkinter import ttk

#Creating RootWindow
tela_cadastro = Tk()
tela_cadastro.geometry("1000x626+650+250")
tela_cadastro.title("Novo cadastro")
tela_cadastro.resizable(False, False)

#Creating Icon
tela_cadastro.iconbitmap(r'C:\\Users\Dinopc\Desktop\CBSControleDeCartao\Imagens\cbsicon.ico')

#Creating Widgets
#Nome da empresa----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
nome_empresa = Label(tela_cadastro, text = ("Nome da empresa :"), font=("Arial", 15))
nome_empresa.place(x=15, y = 5 )

nome_empresa_entry = Entry(tela_cadastro, width = 25, font=("Courier new", 18), relief = "flat")
nome_empresa_entry.place(x = 15, y = 46)

#CNPJ--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cnpj = Label(tela_cadastro, text = ("CNPJ :"), font=("Arial", 15))
cnpj.place(x = 15, y = 95)

cnpj_entry = Entry(tela_cadastro, width = 15, font=("Courier new", 18), relief = "flat" )
cnpj_entry.place(x = 15, y = 130)

#Endereco----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
endereco = Label(tela_cadastro, text = ("Endereco :"), font=("Arial", 15))
endereco.place(x= 15, y = 190 )

endereco_entry = Entry(tela_cadastro, width = 25, font=("Courier new", 18), relief = "flat" )
endereco_entry.place(x = 15, y = 230)

#Bairro-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
complemento = Label(tela_cadastro, text = ("Complemento :"), font=("Arial", 15))
complemento.place(x = 15, y = 295)

complemento_entry = Entry(tela_cadastro, width = 20, font=("Courier new", 18), relief = "flat" )
complemento_entry.place(x = 15, y = 335)

#Contato----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
contato = Label(tela_cadastro, text = ("Contato :"), font=("Arial", 15))
contato.place(x = 15, y = 395)

contato_entry = Entry(tela_cadastro, width = 20, font=("Courier new", 18), relief = "flat" )
contato_entry.place(x = 15, y = 435)

#Observacao------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
observacao = Label(tela_cadastro, text = ("Observacao :"), font=("Arial", 15))
observacao.place(x = 15, y = 495)

observacao_text = Text(tela_cadastro, width = 70,height = 5, relief = "flat" )
observacao_text.place(x = 15, y = 535)

#Numero de fucionarios----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
numero_funcionarios = Label(tela_cadastro, text = ("Nº de Funcionarios :"), font=("Arial", 15))
numero_funcionarios.place(x = 416, y = 5)

numero_funcionarios_spinbox = Spinbox(tela_cadastro, from_ = 0, to = 4000, font=("Couriew new", 15), width=5, relief = "flat")
numero_funcionarios_spinbox.place(x = 420, y = 46)

#Quantidade De Dias----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Quantidade_dias = Label(tela_cadastro, text = ("Dias parados :"), font=("Arial", 15))
Quantidade_dias.place(x = 416, y = 95)

Quantidade_dias_spinbox = Spinbox(tela_cadastro, from_ = 0, to = 2000, font=("Couriew new", 15), width=5, relief = "flat")
Quantidade_dias_spinbox.place(x = 420, y = 130)

#Vendedor----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
vendedor = Label(tela_cadastro, text = ("Vendedor :"), font=("Arial", 15))
vendedor.place(x = 660, y = 95)

vendedor_entry = Entry(tela_cadastro, width = 20, font=("Courier new", 18), relief = "flat" )
vendedor_entry.place(x = 658, y = 130)

#numero----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
numero_endereco = Label(tela_cadastro, text = ("Numero :"), font=("Arial", 15))
numero_endereco.place(x = 400, y = 190)

numero_endereco_entry = Entry(tela_cadastro, width = 8, font=("Courier new", 18), relief = "flat" )
numero_endereco_entry.place(x = 400, y = 230)

#cidade----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Populando Combobox
def cidades_sp():

    cidades_file = open("C:\\Users\Dinopc\Desktop\CBSControleDeCartao\Texto\cidadesSP.txt", "r").readlines()

    cidades = []

    for line in cidades_file:
         cidades.append(line)

    return cidades

#combobox Widget
cidade_endereco = Label(tela_cadastro, text = ("Cidade : "), font=("Arial", 15))
cidade_endereco.place(x = 400, y = 190)

cidade_endereco_combobox = ttk.Combobox(tela_cadastro,font=('arial', 14), width = 18)
cidade_endereco_combobox.place(x = 400, y = 230)

cidade_endereco_combobox['values'] = cidades_sp()

#bairro----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
bairro_endereco = Label(tela_cadastro, text = ("Bairro :"), font=("Arial", 15))
bairro_endereco.place(x = 660, y = 190)

bairro_endereco_entry = Entry(tela_cadastro, width = 15, font=("Courier new", 18), relief = "flat" )
bairro_endereco_entry.place(x = 658, y = 230)

#telefone1----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
telefone1 = Label(tela_cadastro, text = ("Telefone 1 :"), font=("Arial", 15))
telefone1.place(x = 350, y = 395)

telefone1_entry = Entry(tela_cadastro, width = 15, font=("Courier new", 18), relief = "flat" )
telefone1_entry.place(x = 350, y = 435)

#telefone2----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
telefone2 = Label(tela_cadastro, text = ("Telefone 2 :"), font=("Arial", 15))
telefone2.place(x = 600, y = 395)

telefone2_entry = Entry(tela_cadastro, width = 15, font=("Courier new", 18), relief = "flat" )
telefone2_entry.place(x = 600, y = 435)

#Adicionar Colaboradores Botao----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
adicionar_colaboradores = Button(tela_cadastro, text = "Adicionar \n Colaboradores", font = ("Arial", 11), relief = "flat", height = 3, bg = "pale green")
adicionar_colaboradores.place(x = 600 , y = 547)


#Botao Salvar----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
save_icon = PhotoImage(file = "C:\\Users\Dinopc\Desktop\CBSControleDeCartao\Imagens\saveicon.png")
save_button = Button(tela_cadastro, image = save_icon, relief = "flat")
save_button.place(x = 900, y = 547)

#Botao cancelar----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
trash_icon = PhotoImage(file = "C:\\Users\Dinopc\Desktop\CBSControleDeCartao\Imagens\cancelar_icon.png")
save_button = Button(tela_cadastro, image = trash_icon, relief = "flat")
save_button.place(x = 770, y = 547)




















tela_cadastro.mainloop()
