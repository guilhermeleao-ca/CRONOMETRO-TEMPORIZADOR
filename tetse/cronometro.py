import tkinter as tk

# Variáveis globais
tempo = 0
rodando = False

# Função que atualiza o tempo
def atualizar():
    global tempo

    if rodando:
        tempo += 1

        horas = tempo // 3600
        minutos = (tempo % 3600) // 60
        segundos = tempo % 60

        tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}"
        label.config(text=tempo_formatado)

    janela.after(1000, atualizar)

# Funções dos botões
def iniciar():
    global rodando
    rodando = True
    janela.configure(bg="#003300")  # verde escuro

def pausar():
    global rodando
    rodando = False
    janela.configure(bg="#333300")  # amarelo escuro

def resetar():
    global tempo, rodando
    tempo = 0
    rodando = False
    label.config(text="00:00:00")
    janela.configure(bg="black")

# Atalhos do teclado (acessibilidade)
def tecla(event):
    if event.keysym == "space":
        iniciar()
    elif event.keysym.lower() == "r":
        resetar()

# Janela principal
janela = tk.Tk()
janela.title("Cronômetro Acessível")
janela.geometry("320x350")
janela.configure(bg="black")

# Tempo (bem grande)
label = tk.Label(
    janela,
    text="00:00:00",
    font=("Arial", 40),
    fg="white",
    bg="black"
)
label.pack(pady=20)

# Frame dos botões
frame = tk.Frame(janela, bg="black")
frame.pack()

btn_iniciar = tk.Button(
    frame,
    text="Iniciar",
    command=iniciar,
    width=10,
    height=2
)
btn_iniciar.grid(row=0, column=0, padx=5, pady=5)

btn_pausar = tk.Button(
    frame,
    text="Pausar",
    command=pausar,
    width=10,
    height=2
)
btn_pausar.grid(row=0, column=1, padx=5, pady=5)

btn_reset = tk.Button(
    janela,
    text="Reiniciar",
    command=resetar,
    width=22,
    height=2
)
btn_reset.pack(pady=10)

# Ativar atalhos do teclado
janela.bind("<Key>", tecla)

# Iniciar atualização
atualizar()

# Rodar app
janela.mainloop()