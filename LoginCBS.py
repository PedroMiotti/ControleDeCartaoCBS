from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Creating Window
tela_login = Tk()
tela_login.geometry("425x230+650+250")
tela_login.title("Login")
tela_login.resizable(False, False)

#Creating Icon
tela_login.iconbitmap('Imagens\cbsicon.ico')

#CBS Logo
cbs_logo = PhotoImage(file = 'Imagens\cbscestaslogo.gif')
cbs_logo = cbs_logo.subsample(2,2)
logo_label = Label(image=cbs_logo)
logo_label.place(x=160, y=0)

#Creating Widgets

#StringVar
usuario_str = StringVar()
senha_pws = StringVar()

usuario_lbl = Label(tela_login, text = 'Usuário :', font=("courier new", 16))
usuario_lbl.place(x = 30, y = 90)

usuario_lbl_e = Entry(tela_login, font=("courier new", 13), width = 15, relief = 'solid', textvariable = usuario_str)
usuario_lbl_e.place(x = 160, y = 92)

usuario_pws = Label(tela_login, text = 'Senha :', font=("courier new", 16))
usuario_pws.place(x = 55, y = 150)

usuario_pws_e = Entry(tela_login, font=("courier new", 13), width = 15, relief = 'solid', show = "*",textvariable = senha_pws)
usuario_pws_e.place(x = 160, y = 152)


def log():
    #Se o codigo e a senha estao corretos abra o sistema
    if usuario_str.get() == "cbsadmin" and senha_pws.get() == "cbsadmin":
        tela_login.destroy()
        import TelaDeInicio

    elif usuario_str.get() == "cbsoperador" and senha_pws.get() == "cbsoperador":
        tela_login.destroy()
        import motorista
    #Se não mostre essa mensagem
    else:
        messagebox.showerror('Ops !', "Usuário não encontrado " , parent= tela_login)

entrar_btt = Button(tela_login, text = 'Entrar', font=("courier new", 13), width = 8, relief = 'flat', bg = "PaleGreen3", fg= "white", command = log)
entrar_btt.place(x = 330, y = 185)












tela_login.mainloop()
