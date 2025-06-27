# solar-system-sim-pygame

Uma simulação simples do sistema solar desenvolvida em Python com a biblioteca Pygame para renderizar e animar os componentes gráficos. Este projeto foi criado como trabalho final para a disciplina de Computação Gráfrica.

## Funcionalidades

A simulação conta com uma série de funcionalidades que a tornam uma experiência rica e interativa:

* **Representação do Sistema Solar:** Simulação dos 8 planetas do sistema solar, cada um com sua própria velocidade orbital, tamanho e cor.
* **Hierarquia Orbital:** Luas orbitam seus respectivos planetas, enquanto os planetas orbitam o Sol central, demonstrando um sistema de coordenadas aninhado.
* **Luas Implementadas:**
    * A Lua da Terra.
    * Phobos e Deimos de Marte.
    * As quatro luas galileanas de Júpiter: Io, Europa, Ganímedes e Calisto.
* **HUD Interativa:** Ao passar o mouse sobre qualquer corpo celeste (Sol, planetas ou luas), uma caixa de informações (HUD) aparece, exibindo o nome e uma breve descrição do objeto.
* **Controle de Velocidade Dinâmico:** O usuário pode acelerar ou desacelerar o tempo da simulação em tempo real, com um controle mais fino para velocidades mais lentas.
* **Função de Pausa:** A simulação pode ser pausada e resumida a qualquer momento.
* **Efeitos Visuais Avançados:**
    * **Rastros Orbitais:** Planetas e luas deixam um rastro que se desvanece suavemente.
    * **Anéis de Saturno:** Saturno é representado com um sistema de anéis inclinado.
    * **Fundo Dinâmico:** O fundo é composto por centenas de estrelas que "piscam" sutilmente.
    * **Brilho Interativo:** Corpos celestes apresentam um brilho sutil ao passar o mouse sobre eles.

## Pré-requisitos

Para executar este projeto, você precisará ter instalado:

* Python 3.7 ou superior
* Biblioteca Pygame

## Instalação

1.  Clone este repositório para a sua máquina local.
2.  Navegue até o diretório do projeto pelo terminal.
3.  Instale as dependências a partir do arquivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Como Executar

Após a instalação das dependências, execute o arquivo `main.py` a partir da raiz do diretório do projeto:

```bash
python main.py
```

## Controles

* **Seta para Cima:** Aumenta a velocidade da simulação.
* **Seta para Baixo:** Diminui a velocidade da simulação.
* **Barra de Espaço:** Pausa ou resume a simulação.
* **Mouse:** Mova o cursor sobre os planetas, luas ou o Sol para exibir informações detalhadas.
* **Fechar Janela:** Encerra a aplicação.

---

## Estrutura do Projeto

O código é modularizado para garantir organização e legibilidade:

* `main.py`: Ponto de entrada da aplicação. Gerencia o loop principal, os eventos do usuário e a renderização geral.
* `celestial.py`: Contém as definições de classes para todos os corpos celestes (`Sun`, `Planet`, `Moon`).
* `background.py`: Define a classe `StarBackground`, responsável por gerar e animar o fundo estrelado.