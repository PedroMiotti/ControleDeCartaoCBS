from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

import sqlite3
import pandas as pd

# tela_empresas = Tk()
tela_empresas = Toplevel()
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


def editar():
    #Creating RootWindow----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    tela_editar = Toplevel()
    # tela_editar = Toplevel()
    tela_editar.geometry("1000x626+650+250")
    tela_editar.title("Editar")
    tela_editar.resizable(False, False)

    #Creating Icon----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    tela_editar.iconbitmap('Imagens\cbsicon.ico')

    #conectando ao banco de dados----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    conn = sqlite3.connect('BD\cadastroempresa.db')
    c = conn.cursor()

    #Creating Widgets

    #Function to pull all the data for the user to editar(has to be at the top)
    # def pull_data():
    selection = empresas_tree.selection()
    for selection in empresas_tree.selection():
        get_data = c.execute("SELECT * FROM cadastro WHERE nomeempresa = ?", (empresas_tree.set(selection, '#1'),))
        for row in get_data:
            nomeDB = row [0]
            nfuncDB = row[1]
            cnpjDB = row[2]
            diasDB = row [3]
            vendedorDB = row[4]
            enderecoDB = row[5]
            cidadeDb = row[6]
            bairroDB = row[7]
            complementoDB = row[8]
            contatoDB = row[9]
            telefoneDB=row[10]
            telefonedoisDB = row [11]
            obsDB = row[12]
        conn.commit()

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
    nome_empresa = Label(tela_editar, text = ("Nome da empresa : *"), font=("Courier new", 15))
    nome_empresa.place(x=15, y = 5 )

    nome_empresa_entry = Entry(tela_editar, width = 25, font=("Courier new", 18), relief = "flat", textvariable = nome_empresa_str)
    nome_empresa_entry.place(x = 15, y = 46)
    nome_empresa_entry.insert(END, str(nomeDB))

    #CNPJ--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    cnpj = Label(tela_editar, text = ("CNPJ :"), font=("Courier new", 15))
    cnpj.place(x = 15, y = 95)

    cnpj_entry = Entry(tela_editar, width = 15, font=("Courier new", 18), relief = "flat", textvariable = cnpj_str )
    cnpj_entry.place(x = 15, y = 130)
    cnpj_entry.insert(END, str(cnpjDB))

    #Endereco----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    endereco = Label(tela_editar, text = ("Endereco : *"), font=("Courier new", 15))
    endereco.place(x= 15, y = 190 )

    endereco_entry = Entry(tela_editar, width = 25, font=("Courier new", 18), relief = "flat" , textvariable = endereco_str)
    endereco_entry.place(x = 15, y = 230)
    endereco_entry.insert(END, str(enderecoDB))

    #Bairro-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    complemento = Label(tela_editar, text = ("Complemento : "), font=("Courier new", 15))
    complemento.place(x = 15, y = 295)

    complemento_entry = Entry(tela_editar, width = 20, font=("Courier new", 18), relief = "flat", textvariable = complemento_str )
    complemento_entry.place(x = 15, y = 335)
    complemento_entry.insert(END, str(complementoDB))

    #Contato----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    contato = Label(tela_editar, text = ("Contato : *"), font=("Courier new", 15))
    contato.place(x = 15, y = 395)

    contato_entry = Entry(tela_editar, width = 20, font=("Courier new", 18), relief = "flat" , textvariable = contato_str)
    contato_entry.place(x = 15, y = 435)
    contato_entry.insert(END, str(contatoDB))

    #Observacao------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    observacao = Label(tela_editar, text = ("Observacao : "), font=("Courier new", 15))
    observacao.place(x = 15, y = 495)

    observacao_text = Text(tela_editar, width = 70,height = 5, relief = "flat" )
    observacao_text.place(x = 15, y = 535)
    observacao_text.insert(END, str(obsDB))

    #Numero de fucionarios----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    numero_funcionarios = Label(tela_editar, text = ("Nº de Funcionarios : *"), font=("Courier new", 15))
    numero_funcionarios.place(x = 416, y = 5)

    numero_funcionarios_spinbox = Spinbox(tela_editar, from_ = 0, to = 4000, font=("Couriew new", 15), width=5, relief = "flat", textvariable = numero_funcionarios_str)
    numero_funcionarios_spinbox.place(x = 420, y = 46)
    numero_funcionarios_str.set(nfuncDB)

    #Quantidade De Dias----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    quantidade_dias = Label(tela_editar, text = ("Dias parados : *"), font=("Courier new", 15))
    quantidade_dias.place(x = 416, y = 95)

    quantidade_dias_spinbox = Spinbox(tela_editar, from_ = 0, to = 2000, font=("Couriew new", 15), width=5, relief = "flat", textvariable =quantidade_dias_str)
    quantidade_dias_spinbox.place(x = 420, y = 130)
    quantidade_dias_str.set(diasDB)

    #Vendedor----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    vendedor = Label(tela_editar, text = ("Vendedor : *"), font=("Courier new", 15))
    vendedor.place(x = 660, y = 95)

    vendedor_entry = Entry(tela_editar, width = 20, font=("Courier new", 18), relief = "flat", textvariable = vendedor_str )
    vendedor_entry.place(x = 658, y = 130)
    vendedor_entry.insert(END, str(vendedorDB))

    #cidade----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    #Populando Combobox
    def cidades_sp():

        cidades_file = open("C:\\Users\Dinopc\Desktop\CBSControleDeCartao\Texto\cidadesSP.txt", "r").readlines()

        cidades = []

        for line in cidades_file:
             cidades.append(line)

        return cidades

    #combobox Widget
    cidade_endereco = Label(tela_editar, text = ("Cidade : *"), font=("Courier new", 15))
    cidade_endereco.place(x = 400, y = 190)

    cidade_endereco_combobox = ttk.Combobox(tela_editar,font=('arial', 14), width = 18, textvariable = cidade_endereco_str)
    cidade_endereco_combobox.place(x = 400, y = 230)

    cidade_endereco_combobox['values'] = cidades_sp()
    cidade_endereco_str.set(str(cidadeDb))


    #bairro----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    bairro_endereco = Label(tela_editar, text = ("Bairro : *"), font=("Courier new", 15))
    bairro_endereco.place(x = 660, y = 190)

    bairro_endereco_entry = Entry(tela_editar, width = 15, font=("Courier new", 18), relief = "flat" , textvariable = bairro_endereco_str)
    bairro_endereco_entry.place(x = 658, y = 230)
    bairro_endereco_entry.insert(END, str(bairroDB))

    #telefone1----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    telefone1 = Label(tela_editar, text = ("Telefone 1 :"), font=("Courier new", 15))
    telefone1.place(x = 350, y = 395)

    telefone1_entry = Entry(tela_editar, width = 15, font=("Courier new", 18), relief = "flat" , textvariable = telefone1_str)
    telefone1_entry.place(x = 350, y = 435)
    telefone1_entry.insert(END, str(telefoneDB))

    #telefone2----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    telefone2 = Label(tela_editar, text = ("Telefone 2 :"), font=("Courier new", 15))
    telefone2.place(x = 600, y = 395)

    telefone2_entry = Entry(tela_editar, width = 15, font=("Courier new", 18), relief = "flat" , textvariable = telefone2_str)
    telefone2_entry.place(x = 600, y = 435)
    telefone2_entry.insert(END, str(telefonedoisDB))


    #defining the buttons funtions----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #adicionando colaboradores---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def adicionar_colaboradores():
        nome_empresa_get = nome_empresa_str.get()

        if nome_empresa_get == '':
            messagebox.showerror("Ops !" , 'Prencha todos os dados obrigatorios !' ,parent = tela_editar)
        else:
            #Abrindo janela para escolher arquivo
            getting_excelfile = filedialog.askopenfilename(parent=tela_editar, initialdir="/",title='Selecione a planilha de colaboradores')
            # #reading Excel
            read_excel = pd.read_excel(getting_excelfile)

            c.execute('''DROP TABLE IF EXISTS {}'''.format(nome_empresa_get))
            conn.commit()

            c.execute('''CREATE TABLE {}(nome, cod ,cesta)'''.format(nome_empresa_get))
            conn.commit()

            for index, row in read_excel.iterrows():
                insert_table = '''INSERT INTO {}(nome, cod, cesta) VALUES(?,?,?)'''.format(nome_empresa_get)
                c.execute(insert_table, (row[0], row[1], row[2]),)
                conn.commit()
            messagebox.showinfo("Sucesso !" , "Colaboradores importados com sucesso !", parent = tela_editar)


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
            messagebox.showerror("Ops !" , "Prencha todos os dados obrigatorios !", parent = tela_editar)
        elif quantidade_dias_get == '' or vendedor_get == '':
            messagebox.showerror("Ops !" , "Prencha todos os dados obrigatorios !", parent = tela_editar)
        elif endereco_get == '' or cidade_endereco_get == '':
            messagebox.showerror("Ops !" , "Prencha todos os dados obrigatorios !", parent = tela_editar)
        elif  bairro_endereco_get == '' and contato_get == '':
            messagebox.showerror("Ops !" , "Prencha todos os dados obrigatorios !", parent = tela_editar)
        else:
            selection_two = empresas_tree.selection()
            #inserting into the database
            for selection_two in empresas_tree.selection():
                cadastro_sql = "UPDATE cadastro SET nomeempresa=?, nfuncionarios=?, cnpj=?,diasparado=?, vendedor=?,endereco=?,cidade=? , bairro=?, complemento=?, contato=?, telefone=?,telefonedois=?, obs=? WHERE cnpj = ?"
                c.execute(cadastro_sql, (nome_empresa_get, numero_funcionarios_get , cnpj_get, quantidade_dias_get, vendedor_get,endereco_get,cidade_endereco_get, bairro_endereco_get,complemento_get, contato_get, telefone1_get, telefone2_get, observacao_get, cnpj_get,))
                conn.commit()
            messagebox.showinfo("Sucesso !" , "A empresa " + nome_empresa_get + " foi cadastrada com sucesso", parent = tela_editar )
            tela_editar.destroy()



    #cancelando cadastro---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def cancelar_cadastro():
        Ask_msg = messagebox.askquestion("CBS", "Tem certeza que deseja cancelar o cadastro ?", parent = tela_editar)
        if Ask_msg == "yes":
            tela_editar.destroy()
        else:
            pass
    #Adicionar Colaboradores Botao----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    adicionar_colaboradores = Button(tela_editar, text = "Adicionar \n Colaboradores", font = ("Courier new", 11), relief = "flat", height = 3, bg = "PaleGreen3", fg = "white", command = adicionar_colaboradores)
    adicionar_colaboradores.place(x = 600 , y = 547)


    #Botao Salvar----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    save_icon = PhotoImage(file = "Imagens\saveicon.png")
    save_button = Button(tela_editar, image = save_icon, relief = "flat", command = salvar_cadastro)
    save_button.place(x = 900, y = 547)

    #Botao cancelar----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    trash_icon = PhotoImage(file = "Imagens\cancelar_icon.png")
    save_button = Button(tela_editar, image = trash_icon, relief = "flat", command = cancelar_cadastro)
    save_button.place(x = 770, y = 547)

    tela_editar.mainloop()


def apagar_cadastro():
    apagar_selection = empresas_tree.selection()

    msg_delete = messagebox.askquestion('CBS', "Tem certeza que deseja excluir essa empresa ?", parent = tela_empresas)
    if msg_delete == "yes":
        c.execute('DELETE FROM cadastro WHERE nomeempresa = ?', (empresas_tree.set(apagar_selection, '#1'),))
        c.execute('''DROP TABLE IF EXISTS {}'''.format(empresas_tree.set(apagar_selection, '#1')))
        conn.commit()
        empresas_tree.delete(apagar_selection)

        messagebox.showinfo("Sucesso", "Excluido com sucesso", parent = tela_empresas)

    else:
        pass



#Defining the consultar functions
def consultar_colaboradores():
    tela_consulta = Toplevel()
    tela_consulta.geometry('680x370+650+250')
    tela_consulta.title("Consultar Colaboradores")

    #Creating Icon
    tela_consulta.iconbitmap('Imagens\cbsicon.ico')



    #Treeview
    tree_funcionarios = ttk.Treeview(tela_consulta, show ="headings", height= 14)
    tree_funcionarios.place(x = 10, y = 55)
    tree_funcionarios["columns"] = ("one", "two")
    tree_funcionarios.column("one", width = 450)
    tree_funcionarios.column("two", width = 210)
    tree_funcionarios.heading("one", text = "Nome", anchor = "w")
    tree_funcionarios.heading("two", text = "Cestas Disponiveis", anchor = "w")




    #populating Treeview
    selection_funcionarios = empresas_tree.selection()

    for selection_funcionarios in empresas_tree.selection():
        c.execute("SELECT nome, cesta FROM {} ORDER  BY nome ASC".format((empresas_tree.set(selection_funcionarios, '#1'))))
        row = c.fetchall()
        conn.commit()


        for row in row:
            tree_funcionarios.insert("", END, values = row)
    #defining functions



    exportar = Button(tela_consulta, text = 'Exportar', font = ("Courier new", 11), relief = "flat", height = 2,width = 9 , bg = "PaleGreen3", fg = "white")
    exportar.place(x = 585, y = 5)

    recarregar = Button(tela_consulta, text = ' Recarregar \n Todos', font = ("Courier new", 11), relief = "flat", height = 2,width = 9 , bg = "light sky blue", fg = "white")
    recarregar.place(x = 490, y = 5)

    editar_funcionario = Button(tela_consulta, text = 'Editar', font = ("Courier new", 11), relief = "flat", height = 2, width = 9 , bg = "tomato", fg = "white" )
    editar_funcionario.place(x = 395, y = 5)







#Buttons----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
editar_btt = Button(tela_empresas, text = 'Editar', font = ("Courier new", 11), relief = "flat", height = 2,width = 9 , bg = "PaleGreen3", fg = "white", command = editar )
editar_btt.place(x = 585, y = 5)

delete_btt = Button(tela_empresas, text = 'Excluir', font = ("Courier new", 11), relief = "flat", height = 2,width = 9 , bg = "tomato", fg = "white", command = apagar_cadastro )
delete_btt.place(x = 490, y = 5)

consultar_btt = Button(tela_empresas, text = 'Consultar', font = ("Courier new", 11), relief = "flat", height = 2, width = 9 , bg = "light sky blue", fg = "white" , command = consultar_colaboradores)
consultar_btt.place(x = 395, y = 5)


tela_empresas = Root()
# tela_empresas.mainloop()
