import tkinter as tk

# funções
def clicar(valor):
    if valor == "C":
        visor_var.set("")
    elif valor == "=":
        try:
            resultado = str(eval(visor_var.get()))
            visor_var.set(resultado)
        except:
            visor_var.set("Erro")
    else:
        visor_var.set(visor_var.get() + str(valor))

# janela (proporção 9:16)
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("360x640")
janela.configure(bg="black")

# visor
visor_var = tk.StringVar()
visor = tk.Entry(
    janela,
    textvariable=visor_var,
    font=("Arial", 28),
    bd=0,
    bg="black",
    fg="#FFD700",  # amarelo estilo Batman
    justify="right",
    insertbackground="#FFD700"
)
visor.pack(fill="both", ipadx=10, ipady=30, padx=10, pady=20)

# frame dos botões
frame = tk.Frame(janela, bg="black")
frame.pack()

# layout dos botões
botoes = [
    ["C", "", "", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", "0", ".", "="],
]

for i, linha in enumerate(botoes):
    for j, texto in enumerate(linha):
        if texto == "":
            continue

        # cores estilo Batman
        if texto in ["+", "-", "*", "/", "="]:
            bg_cor = "#FFD700"  # amarelo
            fg_cor = "black"
        elif texto == "C":
            bg_cor = "#FFD700"
            fg_cor = "black"
        else:
            bg_cor = "#111111"  # preto mais suave
            fg_cor = "#FFD700"

        btn = tk.Button(
            frame,
            text=texto,
            font=("Arial", 18, "bold"),
            bg=bg_cor,
            fg=fg_cor,
            activebackground="#FFC300",
            activeforeground="black",
            bd=0,
            width=5,
            height=2,
            command=lambda t=texto: clicar(t)
        )

        btn.grid(row=i, column=j, padx=5, pady=5)

# rodar
janela.mainloop()