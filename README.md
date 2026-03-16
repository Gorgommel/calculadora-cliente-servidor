
# Calculadora Cliente‑Servidor com Sockets (Python)

Projeto desenvolvido para demonstrar comunicação **Cliente‑Servidor usando TCP/IP**.

## Tecnologias utilizadas

- Python
- Sockets TCP
- Tkinter (Interface Gráfica)

## Arquitetura

Cliente → envia requisição  
Servidor → processa cálculo  
Servidor → retorna resultado  
Cliente → exibe na interface

Sistema **síncrono (sem multithread)**.

## Estrutura do projeto

```
CalculadoraClienteServidor/
│
├── servidor.py
├── cliente.py
└── README.md
```

## Como executar

### 1 – Iniciar o servidor

```bash
python servidor.py
```

### 2 – Executar o cliente

```bash
python cliente.py
```

### 3 – Utilização

1. Digite dois números
2. Escolha a operação matemática
3. Clique em **Calcular**
4. O resultado será retornado pelo servidor

## Tratamento de erros

Caso o servidor não esteja ativo, o cliente exibirá:

```
Falha de conexão: O servidor encontra-se indisponível.
```

## Autor

Isaac Silva
