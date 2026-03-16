import socket
import tkinter as tk
from tkinter import ttk, messagebox

HOST = "127.0.0.1"
PORT = 5001

historico = []

def enviar_requisicao():

    numero1 = entrada1.get()
    numero2 = entrada2.get()
    operacao = operacao_var.get()

    if numero1 == "" or numero2 == "":
        messagebox.showwarning("Aviso", "Preencha os dois números")
        return

    try:

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((HOST, PORT))

        mensagem = f"{numero1},{operacao},{numero2}"

        cliente.send(mensagem.encode())

        resposta = cliente.recv(1024).decode()

        resultado_label.config(text=f"Resultado: {resposta}")

        registro = f"{numero1} {operacao} {numero2} = {resposta}"
        historico.append(registro)

        atualizar_historico()

        cliente.close()

    except ConnectionRefusedError:

        messagebox.showerror(
            "Erro de Conexão",
            "Falha de conexão: O servidor encontra-se indisponível."
        )

    except Exception as erro:

        messagebox.showerror("Erro", str(erro))


def atualizar_historico():

    lista_historico.delete(0, tk.END)

    for item in historico:
        lista_historico.insert(tk.END, item)


def limpar_historico():

    historico.clear()
    atualizar_historico()


# =========================
# INTERFACE
# =========================

janela = tk.Tk()
janela.title("Calculadora Cliente-Servidor")
janela.geometry("520x420")
janela.minsize(450, 380)

style = ttk.Style()
style.theme_use("clam")

style.configure("TButton", font=("Arial", 10))
style.configure("TLabel", font=("Arial", 10))

janela.columnconfigure(0, weight=1)
janela.rowconfigure(0, weight=1)

frame = ttk.Frame(janela, padding=20)
frame.grid(sticky="nsew")

for i in range(2):
    frame.columnconfigure(i, weight=1)

# Número 1
ttk.Label(frame, text="Número 1").grid(row=0, column=0, sticky="w")
entrada1 = ttk.Entry(frame)
entrada1.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

# Número 2
ttk.Label(frame, text="Número 2").grid(row=0, column=1, sticky="w")
entrada2 = ttk.Entry(frame)
entrada2.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

# Operação
ttk.Label(frame, text="Operação").grid(row=2, column=0, columnspan=2)

operacao_var = tk.StringVar()

operacao_menu = ttk.Combobox(
    frame,
    textvariable=operacao_var,
    values=["+", "-", "*", "/"],
    state="readonly"
)

operacao_menu.current(0)
operacao_menu.grid(row=3, column=0, columnspan=2, sticky="ew", pady=5)

# Botão calcular
botao = ttk.Button(frame, text="Calcular", command=enviar_requisicao)
botao.grid(row=4, column=0, columnspan=2, pady=10, sticky="ew")

# Resultado
resultado_label = ttk.Label(
    frame,
    text="Resultado:",
    font=("Arial", 12, "bold")
)
resultado_label.grid(row=5, column=0, columnspan=2, pady=10)

# =========================
# HISTÓRICO
# =========================

ttk.Label(frame, text="Histórico de Cálculos").grid(row=6, column=0, columnspan=2)

lista_historico = tk.Listbox(frame, height=8)
lista_historico.grid(row=7, column=0, columnspan=2, sticky="nsew", pady=5)

frame.rowconfigure(7, weight=1)

botao_limpar = ttk.Button(frame, text="Limpar Histórico", command=limpar_historico)
botao_limpar.grid(row=8, column=0, columnspan=2, pady=5, sticky="ew")

janela.mainloop()