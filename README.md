# desafio_classes_de_um_jogo

## Descrição
Este projeto implementa uma aplicação simples em Python que simula um sistema de heróis com diferentes classes (Mago, Guerreiro, Monge, Ninja). Cada herói possui um nome, idade e tipo, além de um método `atacar` que exibe uma mensagem personalizada com base na classe do herói, indicando o tipo de ataque utilizado.

O objetivo é criar um herói com base nas entradas do usuário e exibir uma mensagem no formato:  
**"O {tipo} atacou usando {ataque}"**, onde o ataque varia conforme a classe do herói.

## Funcionalidades
- **Classe `hero`**:
  - Atributos: `name` (nome do herói), `age` (idade do herói), `tipo` (classe do herói).
  - Método `atacar`: Exibe uma mensagem indicando o tipo de ataque com base na classe do herói.
- **Tipos de heróis e ataques**:
  - Mago: Ataca usando *magia*.
  - Guerreiro: Ataca usando *espada*.
  - Monge: Ataca usando *artes marciais* (observação: contém um erro de digitação no código como "artes maciais").
  - Ninja: Ataca usando *shuriken*.
  - Qualquer outro tipo: Exibe "Ataque desconhecido".
- **Entrada do usuário**:
  - Solicita a classe do herói (Mago, Guerreiro, Monge ou Ninja).
  - Valida a entrada para garantir que seja uma classe válida.
- **Saída**:
  - Exibe a mensagem formatada com o tipo do herói e o ataque correspondente.

## Como Executar
1. **Pré-requisitos**:
   - Python 3.x instalado no sistema.
   - Nenhum módulo externo é necessário.

2. **Instruções**:
   - Salve o código em um arquivo com extensão `.py` (exemplo: `heroi.py`).
   - Execute o arquivo no terminal ou em um ambiente Python:
     ```bash
     python heroi.py
     ```
   - Insira a classe do herói (Mago, Guerreiro, Monge ou Ninja) quando solicitado.
   - O programa exibirá a mensagem de ataque correspondente e encerrará.

3. **Exemplo de Uso**:
    ```bash
        Informe a classe que deseja jogar (Mago, Guerreiro, Monge ou Ninja): Mago
            O mago atacou usando magia
        
## Estrutura do Código
- **Classe `hero`**:
  - `__init__(self, name, age, tipo)`: Inicializa o herói com nome, idade e tipo.
  - `atacar(self)`: Verifica o tipo do herói e define o ataque correspondente, exibindo a mensagem formatada.
- **Loop Principal**:
  - Solicita a entrada do tipo de herói.
  - Converte a entrada para minúsculas (`lower()`) para facilitar a validação.
  - Valida se o tipo está na lista de classes permitidas (`mago`, `guerreiro`, `monge`, `ninja`).
  - Cria uma instância da classe `hero` com nome fixo ("Larissa"), idade fixa (28) e o tipo informado.
  - Chama o método `atacar` e encerra o programa.
