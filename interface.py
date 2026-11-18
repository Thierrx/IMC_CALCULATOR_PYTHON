import tkinter as tk

from calculadora import calcular_imc, classificar_imc


def abrir_janela():
    janela = tk.Tk()
    janela.title("Calculadora de IMC")
    janela.geometry("400x620")
    janela.resizable(False, False)
    janela.configure(bg="#eef2ff")

    cartao = tk.Frame(janela, bg="white", padx=28, pady=28)
    cartao.pack(padx=24, pady=24, fill="both", expand=True)

    tk.Label(
        cartao,
        text="Calculadora de IMC",
        font=("Arial", 21, "bold"),
        bg="white",
        fg="#1e293b",
    ).pack(pady=(0, 8))

    tk.Label(
        cartao,
        text="Preencha seus dados para calcular",
        font=("Arial", 10),
        bg="white",
        fg="#64748b",
    ).pack(pady=(0, 22))

    tk.Label(
        cartao,
        text="Seu nome",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#334155",
    ).pack(anchor="w")
    campo_nome = tk.Entry(cartao, font=("Arial", 12), relief="solid", bd=1)
    campo_nome.pack(fill="x", ipady=7, pady=(5, 14))

    tk.Label(
        cartao,
        text="Peso (kg)",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#334155",
    ).pack(anchor="w")
    campo_peso = tk.Entry(cartao, font=("Arial", 12), relief="solid", bd=1)
    campo_peso.pack(fill="x", ipady=7, pady=(5, 14))

    tk.Label(
        cartao,
        text="Altura (metros, por exemplo 1,70)",
        font=("Arial", 10, "bold"),
        bg="white",
        fg="#334155",
    ).pack(anchor="w")
    campo_altura = tk.Entry(cartao, font=("Arial", 12), relief="solid", bd=1)
    campo_altura.pack(fill="x", ipady=7, pady=(5, 18))

    resultado = tk.Label(
        cartao,
        text="Seu resultado aparecerá aqui.",
        font=("Arial", 12),
        bg="white",
        fg="#475569",
        justify="center",
        wraplength=300,
    )

    def calcular():
        nome = campo_nome.get().strip()

        if not nome:
            resultado.config(text="Digite seu nome.", fg="#b91c1c")
            return

        try:
            peso = float(campo_peso.get().replace(",", "."))
            altura = float(campo_altura.get().replace(",", "."))
            imc = calcular_imc(peso, altura)
        except ValueError as erro:
            resultado.config(text=str(erro), fg="#b91c1c")
            return

        classificacao = classificar_imc(imc)
        resultado.config(
            text=f"Olá, {nome}!\nSeu IMC é {imc:.2f}\n{classificacao}.",
            fg="#166534",
        )

    tk.Button(
        cartao,
        text="Calcular IMC",
        command=calcular,
        font=("Arial", 12, "bold"),
        bg="#4f46e5",
        fg="white",
        activebackground="#4338ca",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        pady=10,
    ).pack(fill="x")
    resultado.pack(pady=(18, 0))

    tk.Label(
        cartao,
        text="O IMC é uma referência geral, não um diagnóstico.",
        font=("Arial", 8),
        bg="white",
        fg="#94a3b8",
        wraplength=300,
    ).pack(side="bottom", pady=(16, 0))

    janela.mainloop()
