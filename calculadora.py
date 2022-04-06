# Importando tkinter para fazer a interface gráfica

from tkinter import *
from tkinter import ttk
from types import NoneType

# Seleção de Cores

preto = "#1e1f1e"
branco = "#f6f6f6"
azul_cinza = "#38576b"
cinza = "#eceff1"
laranja = "#ffab40"

# Divisão do layout com frames

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.maxsize(width=235, height=310)
janela.config(bg=preto)
frame_tela = Frame(
    janela,
    width=235,
    height=50,
    bg=azul_cinza
)
frame_tela.grid(row=0, column=0)

frame_teclado = Frame(
    janela,
    width=235,
    height=268,
    bg=branco
)
frame_teclado.grid(row=1, column=0)

# Variável inicial para todos_valores

todos_valores = ''

# Função para aparecer os caracteres

valor_texto = StringVar()


def entrar_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    # passando valor para tela
    valor_texto.set(todos_valores)


# Função para calcular


def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))
    todos_valores = str(resultado)

# Função para limpar a tela


def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


# Label (Tela)
app_label = Label(frame_tela, textvariable=valor_texto, width=16,
                  height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=azul_cinza, fg=branco)
app_label.place(x=0, y=0)

# Botões

b_Clean = Button(frame_teclado, command=limpar_tela, text="Limpar", width=17, height=2,
                 bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_Clean.place(x=0, y=0)

# b_Mod = Button(frame_teclado, command=lambda: entrar_valores('%'), text="%", width=5, height=2, bg=cinza,
#             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
#b_Mod.place(x=118, y=0)

b_Div = Button(frame_teclado, command=lambda: entrar_valores('/'), text="/", width=5, height=2, bg=laranja,
               fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_Div.place(x=177, y=0)

# - Linha 2

b_7 = Button(frame_teclado, command=lambda: entrar_valores('7'), text="7", width=5, height=2, bg=cinza,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=52)
b_8 = Button(frame_teclado, command=lambda: entrar_valores('8'), text="8", width=5, height=2, bg=cinza,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=52)
b_9 = Button(frame_teclado, command=lambda: entrar_valores('9'), text="9", width=5, height=2, bg=cinza,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=52)
b_Mult = Button(frame_teclado, command=lambda: entrar_valores('*'), text="*", width=5, height=2, bg=laranja,
                fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_Mult.place(x=177, y=52)

# - Linha 3

b_4 = Button(frame_teclado, command=lambda: entrar_valores('4'), text="4", width=5, height=2, bg=cinza,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=104)
b_5 = Button(frame_teclado, command=lambda: entrar_valores('5'), text="5", width=5, height=2, bg=cinza,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=104)
b_6 = Button(frame_teclado, command=lambda: entrar_valores('6'), text="6", width=5, height=2, bg=cinza,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=104)
b_Sub = Button(frame_teclado, command=lambda: entrar_valores('-'), text="-", width=5, height=2, bg=laranja,
               fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_Sub.place(x=177, y=104)

# - Linha 4

b_1 = Button(frame_teclado, command=lambda: entrar_valores('1'), text="1", width=5, height=2, bg=cinza,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=156)
b_2 = Button(frame_teclado, command=lambda: entrar_valores('2'), text="2", width=5, height=2, bg=cinza,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=156)
b_3 = Button(frame_teclado, command=lambda: entrar_valores('3'), text="3", width=5, height=2, bg=cinza,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=156)
b_Add = Button(frame_teclado, command=lambda: entrar_valores('+'), text="+", width=5, height=2, bg=laranja,
               fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_Add.place(x=177, y=156)

# - Linha 5

b_Zero = Button(frame_teclado, command=lambda: entrar_valores('0'), text="0", width=11, height=2,
                bg=cinza, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_Zero.place(x=0, y=208)

b_Point = Button(frame_teclado, command=lambda: entrar_valores('.'), text=".", width=5, height=2, bg=cinza,
                 font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_Point.place(x=118, y=208)

b_Result = Button(frame_teclado, command=calcular, text="=", width=5, height=2, bg=laranja,
                  fg=branco, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_Result.place(x=177, y=208)


janela.mainloop()
