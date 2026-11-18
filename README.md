# Calculadora de IMC

Um projeto simples em Python com interface gráfica feita usando Tkinter.

## Como executar

1. Abra o terminal na pasta do projeto.
2. Execute:

   ```bash
   python home.py
   ```

O Tkinter geralmente já vem incluído na instalação do Python.

## Organização dos arquivos

- `home.py`: ponto de entrada; inicia o programa.
- `interface.py`: cria a janela e responde às ações do usuário.
- `calculadora.py`: calcula e classifica o IMC, sem depender da interface.

Essa separação deixa a lógica do cálculo mais fácil de localizar e testar.
