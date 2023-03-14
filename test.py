from tkinter import *
from tkinter import Tk, ttk, messagebox
from Registro import Registros


def regis():
    nome =nome_E.get()
    senha = senha_E.get()
    print(f'nome: {nome}\nSenha: {senha}')
    
    
    r = Registros(nome, senha)
    r.le_Regis()
    if r.user_exiten is False and r.cadas is False:
        r.Cadastra_user()
        if r.senha_perfeita:
            for widget in FC.winfo_children():
                widget.destroy()
            for widget in f_b.winfo_children():
                widget.destroy()
        elif r.senha_perfeita is False:
            messagebox.showwarning('Erro', 'Senha esta 6 a 12 digitos')
    else:
        messagebox.showwarning('Erro', 'Usuário já existe')



win = Tk()
win.title('Registro')
win.geometry('310x300')
win.configure(background='#feffff')
#dividi win
FC = Frame(win, width=310, height=50, bg='#dee3de', relief='flat')
FC.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

f_b = Frame(win, width=310, height=250, bg='#e8ede8', relief='flat')
f_b.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# configura FC

nome = Label(FC, text='Registro', anchor=NE, font=('Ivy 25'), bg='#dee3de', fg='#000500')
nome.place(x=5, y=5)

linha = Label(FC, text='', width=275, anchor=NW, bg='#1459d9')
linha.place(x=10, y=46)

nome_Lb = Label(f_b, text='Usuário', anchor=NW, font=('Ivy 15'), bg='#e8ede8', fg='#000500')
nome_Lb.place(x=10, y=20)
nome_E = Entry(f_b, width=25, justify='left', font=("", 15), highlightthickness=1, relief=SOLID)
nome_E.place(x=14, y=50)

senha_Lb= Label(f_b, text='Senha', anchor=NW, font=('Ivy 15'), bg='#e8ede8', fg='#000500')
senha_Lb.place(x=10, y=95)

senha_E = Entry(f_b, width=25, justify='left',show="*", font=("", 15), highlightthickness=1, relief=SOLID)
senha_E.place(x=14, y=130)

button = Button(f_b, command=regis, text='Cadastra', width=30, height=2, font=('Ivy 9'), bg='#1459d9', fg='#e8ede8', relief=SOLID, overrelief=RIDGE)
button.place(x=35, y=180)

win.mainloop() 