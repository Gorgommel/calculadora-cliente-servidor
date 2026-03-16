
# ===============================
# CLIENTE COM INTERFACE GRÁFICA
# ===============================

import socket
import tkinter as tk
from tkinter import messagebox

HOST = "127.0.0.1"
PORT = 5001

def enviar_requisicao():

    numero1 = entrada1.get()
    numero2 = entrada2.get()
    operacao = operacao_var.get()

    try:

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        cliente.connect((HOST, PORT))

        mensagem = f"{numero1},{operacao},{numero2}"

        cliente.send(mensagem.encode())

        resposta = cliente.recv(1024).decode()

        resultado_texto.set("Resultado: " + resposta)

        cliente.close()

    except ConnectionRefusedError:

        messagebox.showerror(
            "Erro de Conexão",
            "Falha de conexão: O servidor encontra-se indisponível."
        )

    except Exception as erro:

        messagebox.showerror("Erro", str(erro))


janela = tk.Tk()
janela.title("Calculadora Cliente-Servidor")
janela.geometry("320x260")

tk.Label(janela, text="Número 1").pack()

entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Label(janela, text="Número 2").pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

operacao_var = tk.StringVar()
operacao_var.set("+")

tk.Label(janela, text="Operação").pack()

menu = tk.OptionMenu(janela, operacao_var, "+", "-", "*", "/")
menu.pack()

tk.Button(
    janela,
    text="Calcular",
    command=enviar_requisicao
).pack(pady=10)

resultado_texto = tk.StringVar()
resultado_texto.set("Resultado:")

tk.Label(janela, textvariable=resultado_texto).pack()

janela.mainloop()
