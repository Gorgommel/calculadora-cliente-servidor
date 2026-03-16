
# ===============================
# SERVIDOR TCP - CALCULADORA
# Executado no terminal (CLI)
# ===============================

import socket

HOST = "0.0.0.0"   # aceita conexões de qualquer IP
PORT = 5001        # porta do servidor

print("===================================")
print(" SERVIDOR DE CALCULADORA REMOTA ")
print(" Porta:", PORT)
print("===================================")

# cria socket TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associa IP e porta
servidor.bind((HOST, PORT))

# começa a escutar conexões
servidor.listen(1)

print("Servidor escutando...")

while True:

    print("\nAguardando cliente...")

    # aceita conexão (bloqueante)
    conexao, endereco = servidor.accept()

    print("Cliente conectado:", endereco)

    try:

        # recebe dados
        dados = conexao.recv(1024).decode()

        print("Dados recebidos:", dados)

        numero1, operacao, numero2 = dados.split(",")

        numero1 = float(numero1)
        numero2 = float(numero2)

        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            resultado = numero1 / numero2
        else:
            resultado = "Operação inválida"

        resposta = str(resultado)

        print("Resultado enviado:", resposta)

        conexao.send(resposta.encode())

    except Exception as erro:

        print("Erro:", erro)
        conexao.send("Erro no processamento".encode())

    finally:

        conexao.close()
        print("Conexão encerrada")
