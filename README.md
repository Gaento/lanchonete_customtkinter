
Lanchonete do Gaento
![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-Completed-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-%E2%9C%94-brightgreen.svg)


Este código cria um aplicativo simples de pedidos para uma lanchonete utilizando a biblioteca `customtkinter` para a interface gráfica.

## Funcionalidades:
- O aplicativo possui uma interface gráfica com opções de itens do cardápio, como "Cachorro Quente", "X-Salada", "X-Bacon", "Torrada Simples" e "Refrigerante".
- O usuário pode selecionar os itens desejados por meio de checkboxes e confirmar o pedido.
- O total do pedido é calculado automaticamente com base nos itens selecionados e exibido ao usuário.
- Há também a opção de limpar o pedido atual e fazer um novo pedido.

## Estrutura do Código:
1. **Configuração da Aparência e Cores**
   - A cor de fundo da interface é configurada como modo escuro utilizando `ctk.set_appearance_mode('dark')`.
   
2. **Itens e Preços**
   - São definidos os preços de cada item do cardápio:
     - Cachorro Quente: R$ 4,00
     - X-Salada: R$ 4,50
     - X-Bacon: R$ 5,00
     - Torrada Simples: R$ 2,00
     - Refrigerante: R$ 1,50

3. **Funções do Pedido**
   - **`confirmacao_pedido()`**: Calcula o total com base nos itens selecionados e exibe um feedback ao usuário.
   - **`limpar_pedido()`**: Limpa a seleção de todos os itens e o feedback do pedido.

4. **Interface Gráfica**
   - **Janela Principal**: A janela do aplicativo é configurada com tamanho de 500x800 pixels e o título "Lanchonete do Gaento".
   - **Tabela de Cardápio**: Exibe o cardápio com os itens e seus preços.
   - **Checkboxes**: Cada item do cardápio possui um checkbox para que o usuário possa selecionar os itens desejados.
   - **Botões**: Dois botões são criados, um para confirmar o pedido e outro para limpar o pedido atual.

