import customtkinter as ctk

# cor do app
cor_app = ctk.set_appearance_mode('dark')

# Pedidos e preços
cachorro_quente = 4.00
x_salada = 4.50
x_bacon = 5.00
torrada_simples = 2.00
refrigerante = 1.50

#total gasto
total = 0

# Janela principal
app = ctk.CTk()
app.geometry('500x800')
app.title('Lanchonete do Gaento')

# Variáveis para os checkboxes
cachorro_quente_var = ctk.BooleanVar()
x_salada_var = ctk.BooleanVar()
x_bacon_var = ctk.BooleanVar()
torrada_simples_var = ctk.BooleanVar()
refrigerante_var = ctk.BooleanVar()

# Função de confirmação do pedido
def confirmacao_pedido():
    global total  
    total = 0  
    pedido = ""
    
    if cachorro_quente_var.get():  
        pedido += "Cachorro Quente, "
        total += cachorro_quente
    if x_salada_var.get():  
        pedido += "X-Salada, "
        total += x_salada
    if x_bacon_var.get():  
        pedido += "X-Bacon, "
        total += x_bacon
    if torrada_simples_var.get():  
        pedido += "Torrada Simples, "
        total += torrada_simples
    if refrigerante_var.get():  
        pedido += "Refrigerante, "
        total += refrigerante
    
    # Feedback na interface do usuário
    if pedido:
        pedido = pedido.rstrip(', ')  
        feedback_pedido.configure(text=f"Pedido confirmado: {pedido}, que custou R$ {total:.2f}")
    else:
        feedback_pedido.configure(text="Nenhum item selecionado!")

# Função para limpar o pedido
def limpar_pedido():
    cachorro_quente_var.set(False)
    x_salada_var.set(False)
    x_bacon_var.set(False)
    torrada_simples_var.set(False)
    refrigerante_var.set(False)
    
    # Limpando o feedback do pedido
    feedback_pedido.configure(text="")

# Cardápio
cardapio_label = ctk.CTkLabel(app, text='CARDÁPIO GAENTO:', font=("Arial", 20, "bold"))
cardapio_label.pack(pady=10)

# Cabeçalho do cardápio
colunas = ["ID", "Pratos", "Preços"]

# Dados do cardápio
dados = [
    [1, "Cachorro Quente", "R$ 4,00"],
    [2, "X-Salada", "R$ 4,50"],
    [3, "X-Bacon", "R$ 5,00"],
    [4, "Torrada Simples", "R$ 2,00"],
    [5, "Refrigerante", "R$ 1,50"]
]

# Frame da tabela
tabela_frame = ctk.CTkFrame(app)
tabela_frame.pack(pady=10, padx=20)

# Criando o cabeçalho da tabela
for i, coluna in enumerate(colunas):
    cabecalho = ctk.CTkLabel(tabela_frame, text=coluna, font=("Arial", 14, "bold"))
    cabecalho.grid(row=0, column=i, padx=5, pady=5)

# Criando as células do cardápio (a parte da tabela)
for i, linha in enumerate(dados):
    for j, valor in enumerate(linha):
        cell = ctk.CTkLabel(tabela_frame, text=str(valor), font=("Arial", 12, "bold"))
        cell.grid(row=i + 1, column=j, padx=5, pady=5)

# Frame para centralizar os checkboxes
checkbox_frame = ctk.CTkFrame(app)
checkbox_frame.pack(pady=20)

# Checkbox para cada item do cardápio
checkbox_cachorro_quente = ctk.CTkCheckBox(checkbox_frame, text="Cachorro Quente", variable=cachorro_quente_var,
    fg_color="gray",   
    checkmark_color="green")  
checkbox_cachorro_quente.pack(pady=5, anchor="center")

checkbox_x_salada = ctk.CTkCheckBox(checkbox_frame, text="X-Salada", variable=x_salada_var,
    fg_color="gray",   
    checkmark_color="green")  
checkbox_x_salada.pack(pady=5, anchor="center")

checkbox_x_bacon = ctk.CTkCheckBox(checkbox_frame, text="X-Bacon", variable=x_bacon_var,
    fg_color="gray",   
    checkmark_color="green")  
checkbox_x_bacon.pack(pady=5, anchor="center")

checkbox_torrada_simples = ctk.CTkCheckBox(checkbox_frame, text="Torrada Simples", variable=torrada_simples_var,
    fg_color="gray",   
    checkmark_color="green")  
checkbox_torrada_simples.pack(pady=5, anchor="center")

checkbox_refrigerante = ctk.CTkCheckBox(checkbox_frame, text="Refrigerante", variable=refrigerante_var,
    fg_color="gray",   
    checkmark_color="green")  
checkbox_refrigerante.pack(pady=5, anchor="center")

# Botão para confirmar o pedido
botao_confirmar = ctk.CTkButton(app, 
    text="Confirmar Pedido", 
    command=confirmacao_pedido,
    fg_color="#696969",
    hover_color="#228B22",
    font=("Arial", 15, "bold"))
botao_confirmar.pack(pady=20)

# Botão "Outro Pedido" no canto esquerdo
botao_outro_pedido = ctk.CTkButton(
    app, 
    text="Outro Pedido", 
    command=limpar_pedido,
    font=("Arial", 12, "bold"),
    fg_color="#696969",
    hover_color="#8B0000"
    )
botao_outro_pedido.place(x=10, y=750)  

# Feedback do pedido
feedback_pedido = ctk.CTkLabel(app, text='')
feedback_pedido.pack(pady=5)

# Inicializando o App
app.mainloop()
